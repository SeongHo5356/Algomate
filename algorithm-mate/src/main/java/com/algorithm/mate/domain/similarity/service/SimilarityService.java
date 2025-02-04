package com.algorithm.mate.domain.similarity.service;

import com.algorithm.mate.domain.similarity.entity.Language;
import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.repository.SimilarityRepository;
import de.jplag.JPlag;
import de.jplag.JPlagComparison;
import de.jplag.JPlagResult;
import de.jplag.exceptions.ExitException;
import de.jplag.options.JPlagOptions;
import de.jplag.options.LanguageOption;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
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

    @Autowired
    public SimilarityService(SimilarityRepository similarityRepository) {
        this.similarityRepository = similarityRepository;
    }

    public List<JPlagComparison> compareSoltions(String solutionPath) throws CustomExitException {
        // jplag 옵션 설정
        try{
            JPlagOptions options = new JPlagOptions(
                    solutionPath, // 비교할 폴더 경로
                    LanguageOption.PYTHON_3  // 언어 설정
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

    public void compareWithBaseFile(String baseFilePath, String solutionsPath) throws CustomExitException {
        try {

            // 문제 번호 추출
            String parts[] = baseFilePath.split("/");
            long problemId = Integer.parseInt(parts[4]);

            // 기준 파일 1개 선택
            File baseDir = new File(baseFilePath);
            File[] baseFiles = baseDir.listFiles();
            if (baseFiles == null || baseFiles.length == 0) {
                throw new CustomExitException("No base file found in: " + baseFilePath);
            }
            File baseFile = baseFiles[0]; // 첫 번째 파일을 기준 파일로 선택

            // 임시 디렉토리 생성
            Path tempDir = createTempDirectory();

            // 기준 파일을 임시 디렉토리로 복사
            Path baseFileCopyPath = tempDir.resolve(baseFile.getName());
            Files.copy(baseFile.toPath(), baseFileCopyPath, StandardCopyOption.REPLACE_EXISTING);

            // 비교할 파일들을 임시 디렉토리로 복사
            copyFilesFromDirectory(solutionsPath, tempDir);

            // JPlag를 사용하여 비교
            List<JPlagComparison> comparisons = compareSoltions(tempDir.toString());

            // 결과를 데이터베이스에 저장
            for (JPlagComparison comparison : comparisons) {
                String baseFileName = baseFile.getName();
                String comparedFileName1 = comparison.getFirstSubmission().getName();
                String comparedFileName2 = comparison.getSecondSubmission().getName();
                double similarity = comparison.similarity();

                // 비교하고자 하는 파일에 대한 결과만 가져와서 저장
                if (baseFileName.equals(comparedFileName1)) {
                    saveComparisonResult(baseFileName, comparedFileName2, similarity, problemId);
                }
                else if(baseFileName.equals(comparedFileName2)){
                    saveComparisonResult(baseFileName, comparedFileName1, similarity, problemId);
                }
            }
        } catch (CustomExitException e) {
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        } catch (Exception e) {
            throw new CustomExitException("Unexpected error: " + e.getMessage());
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
        Similarity result = new Similarity();
        result.setSimilarityScore(similarity);
        result.setCreatedAt(LocalDateTime.now());
        result.setLanguage(Language.PYTHON_3);
        result.setAnswerId(comparedFileName); // 비교한 정답
        result.setSubmissionId(baseFileName); // 제출된 정답
        result.setProblemId(problemId);
        similarityRepository.save(result);
    }
}
