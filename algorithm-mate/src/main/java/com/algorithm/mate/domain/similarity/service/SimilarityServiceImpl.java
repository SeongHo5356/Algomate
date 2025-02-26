package com.algorithm.mate.domain.similarity.service;

import com.algorithm.mate.domain.similarity.entity.Language;
import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.repository.SimilarityRepository;
import com.algorithm.mate.domain.similarity.service.SimilarityService;
import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import com.algorithm.mate.domain.submission.service.SubmissionService;
import de.jplag.JPlag;
import de.jplag.JPlagComparison;
import de.jplag.JPlagResult;
import de.jplag.exceptions.ExitException    ;
import de.jplag.options.JPlagOptions;
import de.jplag.options.LanguageOption;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Slf4j
@Service
public class SimilarityServiceImpl implements SimilarityService2 {

    private final SimilarityRepository similarityRepository;
    private final SubmissionService submissionService;
    private final SubmissionRepository submissionRepository;
    private final SolutionRepository solutionRepository;
    private final SolutionFilePathResolver pathResolver;

    @Autowired
    public SimilarityServiceImpl(SimilarityRepository similarityRepository, SubmissionService submissionService, SubmissionRepository submissionRepository, SolutionRepository solutionRepository, SolutionFilePathResolver pathResolver) {
        this.similarityRepository = similarityRepository;
        this.submissionService = submissionService;
        this.submissionRepository = submissionRepository;
        this.solutionRepository = solutionRepository;
        this.pathResolver = pathResolver;
    }

    @Override
    public List<JPlagComparison> compareSoltions(String solutionPath, String language) throws CustomExitException {
        LanguageOption languageOption;
        switch (language.toLowerCase()) {
            case "java":
                languageOption = LanguageOption.JAVA;
                break;
            case "c++":
            case "c":
                languageOption = LanguageOption.C_CPP;
                break;
            case "python":
                languageOption = LanguageOption.PYTHON_3;
                break;
            default:
                throw new CustomExitException("Unsupported language: " + language);
        }

        try {
            JPlagOptions options = new JPlagOptions(solutionPath, languageOption);
            JPlag jplag = new JPlag(options);
            JPlagResult result = jplag.run();
            return result.getComparisons();
        } catch (ExitException e) {
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        }
    }

    @Override
    public void compareWithBaseFile(String bkId, String problemId, String language) throws CustomExitException {
        try {
            String fileExtension = submissionService.getFileExtension(language);
            // 환경 변수 기반 경로 사용
            String baseFilePath = pathResolver.getBaseFilePath(problemId, bkId, fileExtension);
            String solutionsPath = pathResolver.getSolutionsPath(problemId, fileExtension);

            log.info("현재 작업 디렉토리: " + new File("").getAbsolutePath());
            log.info("찾으려는 파일 절대 경로: " + new File(baseFilePath).getAbsolutePath());
            log.info("파일 존재 여부: " + new File(baseFilePath).exists());

            File baseFile = new File(baseFilePath);
            if (!baseFile.exists()){
                throw new CustomExitException("Base file not found: " + baseFilePath);
            }

            // 임시 디렉토리 생성 및 파일 복사
            Path tempDir = createTempDirectory();
            Path baseFileCopyPath = tempDir.resolve(baseFile.getName());
            Files.copy(baseFile.toPath(), baseFileCopyPath, StandardCopyOption.REPLACE_EXISTING);
            copyFilesFromDirectory(solutionsPath, tempDir);

            // JPlag 비교 실행
            List<JPlagComparison> comparisons = compareSoltions(tempDir.toString(), language);

            // 비교 결과 저장 (기준 파일과 비교된 파일에 대해서만)
            for (JPlagComparison comparison : comparisons) {
                String baseFileName = baseFile.getName();
                String comparedFileName1 = comparison.getFirstSubmission().getName();
                String comparedFileName2 = comparison.getSecondSubmission().getName();
                double similarity = comparison.similarity();

                if (baseFileName.equals(comparedFileName1)) {
                    saveComparisonResult(baseFileName, comparedFileName2, similarity, Integer.parseInt(problemId));
                } else if (baseFileName.equals(comparedFileName2)) {
                    saveComparisonResult(baseFileName, comparedFileName1, similarity, Integer.parseInt(problemId));
                }
            }
        } catch (CustomExitException e) {
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        } catch (Exception e) {
            throw new CustomExitException("Unexpected error: " + e.getMessage());
        }
    }

    @Override
    public List<Similarity> getTop10SimilaritiesByBkId(String bkId) throws CustomExitException {
        return similarityRepository.findBySubmission_BkIdOrderBySimilarityScoreDesc(bkId, PageRequest.of(0, 10));
    }

    // ─── Private Helper Methods ──────────────────────────────────────────────

    private Path createTempDirectory() throws CustomExitException {
        try {
            return Files.createTempDirectory("jplag");
        } catch (Exception e) {
            throw new CustomExitException("Failed to create temp directory: " + e.getMessage());
        }
    }

    private void copyFilesFromDirectory(String sourceDir, Path targetDir) throws CustomExitException {
        try {
            File[] files = new File(sourceDir).listFiles();
            if (files != null) {
                for (File file : files) {
                    Files.copy(file.toPath(), targetDir.resolve(file.getName()), StandardCopyOption.REPLACE_EXISTING);
                }
            }
        } catch (Exception e) {
            throw new CustomExitException("Failed to copy files: " + e.getMessage());
        }
    }

    private void saveComparisonResult(String baseFileName, String comparedFileName, double similarity, long problemId) throws CustomExitException {
        String bkId = baseFileName.substring(0, baseFileName.lastIndexOf("."));
        log.info("bkId: " + bkId);
        Submission submission = submissionRepository.findByBkId(bkId);
        log.info("Found submission: " + submission);

        if (similarityRepository.existsByAnswerIdAndSubmission(comparedFileName, submission)) {
            log.info("Similarity result already exists for answerId: {} and submission: {}", comparedFileName, submission.getBkId());
            return;
        }

        Similarity result = new Similarity();
        result.setSimilarityScore(similarity);
        result.setCreatedAt(LocalDateTime.now());
        result.setLanguage(Language.PYTHON_3);
        result.setAnswerId(comparedFileName);
        result.setSubmissionId(baseFileName);
        result.setProblemId(problemId);
        result.setSubmission(submission);

        log.info("Saving Similarity result: " + result);
        similarityRepository.save(result);
    }

    @Override
    public String similarityCalculate(String bkId, String problemId, String language) throws CustomExitException {

        // 제출물을 존재하는지 조회
        Submission submission = submissionRepository.findByBkId(bkId);

        if (submission != null) {
            // 비교할 데이터가 존재하는지 조회
            List<Solution> solutions = solutionRepository.findByProblemIdAndLanguage(problemId, language);
            if (!solutions.isEmpty()) {
                // 유사도 계산
                compareWithBaseFile(bkId, problemId, language);
            } else {
                throw new CustomExitException("No solutions found for the given problemId and language.");
            }
        } else {
            throw new CustomExitException("Submission not found for bkId: " + bkId);
        }

        return "1"; // 성공 응답
    }

    @Override
    public List<String> getTopSimilarityFiles(String bkId) throws CustomExitException {
        // 유사도 상위 파일 목록을 가져오는 로직
        List<Similarity> topSimilarities = getTop10SimilaritiesByBkId(bkId);

        List<String> filePaths = new ArrayList<>();
        for (Similarity similarity : topSimilarities) {
            String fileName = similarity.getAnswerId(); // 파일 이름
            long problemId = similarity.getProblemId();

            // 상대 경로로 변환
            String relativePath = String.format("%d/py/%s", problemId, fileName);
            Path absolutePath = Paths.get(pathResolver.getSolutionsBasePath(), relativePath);
//            Path absolutePath = Paths.get("/Users/sungho/Documents/study/Algomate/algorithm-mate/src/main/resources/solutions", relativePath);

            // 파일 존재 여부 체크
            if (Files.exists(absolutePath)) {
                filePaths.add(relativePath);
            } else {
                throw new CustomExitException("File not found: " + relativePath);
            }
        }

        return filePaths;
    }




}
