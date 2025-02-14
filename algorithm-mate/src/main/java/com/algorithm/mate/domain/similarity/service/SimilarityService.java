package com.algorithm.mate.domain.similarity.service;

import com.algorithm.mate.domain.similarity.entity.Language;
import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.repository.SimilarityRepository;
import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import com.algorithm.mate.domain.submission.service.SubmissionService;
import de.jplag.JPlag;
import de.jplag.JPlagComparison;
import de.jplag.JPlagResult;
import de.jplag.exceptions.ExitException;
import de.jplag.options.JPlagOptions;
import de.jplag.options.LanguageOption;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.time.LocalDateTime;
import java.util.List;


@Slf4j
@Service
public class SimilarityService {

    private final SimilarityRepository similarityRepository;
    private final SubmissionService submissionService;
    private final SubmissionRepository submissionRepository;

    @Autowired
    public SimilarityService(SimilarityRepository similarityRepository, SubmissionService submissionService, SubmissionRepository submissionRepository) {
        this.similarityRepository = similarityRepository;
        this.submissionService = submissionService;
        this.submissionRepository = submissionRepository;
    }

    public List<JPlagComparison> compareSoltions(String solutionPath, String language) throws CustomExitException {
        // 언어에 따른 LanguageOption 설정
        LanguageOption languageOption;
        switch (language.toLowerCase()) {
            case "java":
                languageOption = LanguageOption.JAVA;
                break;
            case "c++":
                languageOption = LanguageOption.C_CPP;
                break;
            case "c":
                languageOption = LanguageOption.C_CPP;
                break;
            case "python":
                languageOption = LanguageOption.PYTHON_3;
                break;
            default:
                throw new CustomExitException("Unsupported language: " + language);
        }

        // jplag 옵션 설정
        try{
            JPlagOptions options = new JPlagOptions(
                    solutionPath, // 비교할 폴더 경로
                    languageOption  // 언어 설정
            );

            // jplag 실행
            JPlag jplag = new JPlag(options);
            JPlagResult result = jplag.run();

            // 유사도 비교 결과 확인
            return result.getComparisons();

        } catch (ExitException e){
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        }
    }

    //base 폴더 안에 특정 파일과 정답들을 유사도 검사
    public void compareWithBaseFile(String bkId, String problemId, String language ) throws CustomExitException {
        try{
            String fileExtension = submissionService.getFileExtension(language);
            String baseFilePath = String.format("src/main/resources/solutions/%s/base/%s.%s", problemId, bkId, fileExtension); // 이후 변경
            String solutionsPath = String.format("src/main/resources/solutions/%s/%s", problemId, fileExtension); //c,c++,java,python
            log.info("0");

            // 파일 접근 시도 전에 로그 추가
            log.info("현재 작업 디렉토리: " + new File("").getAbsolutePath());
            log.info("찾으려는 파일 절대 경로: " + new File(baseFilePath).getAbsolutePath());
            log.info("파일 존재 여부: " + new File(baseFilePath).exists());
            // 기준 파일 선택: bkId.language 파일 찾기
            File baseFile = new File(baseFilePath);
            if (!baseFile.exists()){
                throw new CustomExitException("Base file not found: " + baseFilePath);
            }
            log.info("1");
            // 임시 디렉토리 생성
            Path tempDir = createTempDirectory();
            // 기준 파일 복사
            log.info("2");
            Path baseFileCopyPath = tempDir.resolve(baseFile.getName());
            Files.copy(baseFile.toPath(), baseFileCopyPath, StandardCopyOption.REPLACE_EXISTING);
            // 비교할 파일 복사 : solutions/문제번호/language 폴더의 모든 파일
            log.info("3");
            copyFilesFromDirectory(solutionsPath, tempDir);
            // JPlag를 사용하여 비교
            log.info("4");
            List<JPlagComparison> comparisons = compareSoltions(tempDir.toString(), language);
            // 결과를 데이터베이스에 저장
            log.info("5");
            for (JPlagComparison comparison : comparisons) {
                String baseFileName = baseFile.getName();
                String comparedFileName1 = comparison.getFirstSubmission().getName();
                String comparedFileName2 = comparison.getSecondSubmission().getName();
                double similarity = comparison.similarity();

                // 기준 파일에 대한 비교 결과만 저장
                if (baseFileName.equals(comparedFileName1)) {
                    saveComparisonResult(baseFileName, comparedFileName2, similarity, Integer.parseInt(problemId));
                } else if (baseFileName.equals(comparedFileName2)) {
                    saveComparisonResult(baseFileName, comparedFileName1, similarity, Integer.parseInt(problemId));
                }
            }
        } catch (CustomExitException e){
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        } catch (Exception e){
            throw new CustomExitException("Unexpected error: "+e.getMessage());
        }
    }

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
                    Path targetPath = targetDir.resolve(file.getName());
                    Files.copy(file.toPath(), targetPath, StandardCopyOption.REPLACE_EXISTING);
                }
            }
        } catch (Exception e) {
            throw new CustomExitException("Failed to copy files: " + e.getMessage());
        }
    }

    private void saveComparisonResult(String baseFileName, String comparedFileName, double similarity, long problemId) throws CustomExitException {
        //파일 경로에서 bkId를 구해옴
        String bkId = baseFileName.substring(0, baseFileName.lastIndexOf("."));
        log.info("bkId: " + bkId);
        // Submission 엔티티 조회
        Submission submission = submissionRepository.findByBkId(bkId);
        log.info("Found submission: " + submission);

        // 중복 체크
        if (similarityRepository.existsByAnswerIdAndSubmission(comparedFileName,submission)){
            log.info("Similarity result already exists for answerId: {} and submission: {}", comparedFileName, submission.getBkId());
            return;
        }

        Similarity result = new Similarity();
        result.setSimilarityScore(similarity);
        result.setCreatedAt(LocalDateTime.now());
        result.setLanguage(Language.PYTHON_3);
        result.setAnswerId(comparedFileName); // 비교한 정답
        result.setSubmissionId(baseFileName); // 제출된 정답
        result.setProblemId(problemId);
        result.setSubmission(submission);

        log.info("Saving Similarity result: " + result);
        similarityRepository.save(result);
    }

    public List<Similarity> getTop10SimilaritiesByBkId(String bkId) throws CustomExitException {
        return similarityRepository.findBySubmission_BkIdOrderBySimilarityScoreDesc(
                bkId,
                PageRequest.of(0,10)
        );
    }
}
