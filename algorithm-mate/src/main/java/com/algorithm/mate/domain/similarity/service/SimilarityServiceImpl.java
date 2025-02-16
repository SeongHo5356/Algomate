package com.algorithm.mate.domain.similarity.service;

import com.algorithm.mate.domain.similarity.entity.Language;
import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.repository.SimilarityRepository;
import com.algorithm.mate.domain.similarity.service.SimilarityService;
import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import com.algorithm.mate.domain.submission.service.SubmissionService;
import com.algorithm.mate.util.FileUtil;
import de.jplag.JPlag;
import de.jplag.JPlagComparison;
import de.jplag.JPlagResult;
import de.jplag.exceptions.ExitException;
import de.jplag.options.JPlagOptions;
import de.jplag.options.LanguageOption;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.io.File;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class SimilarityServiceImpl implements SimilarityService {

    private final SimilarityRepository similarityRepository;
    private final SubmissionService submissionService;
    private final SubmissionRepository submissionRepository;

    private static final String BASE_PATH = "src/main/resources/solutions/";

    @Override
    public List<Similarity> getTop10SimilaritiesByBkId(String bkId) throws CustomExitException {
        return similarityRepository.findBySubmission_BkIdOrderBySimilarityScoreDesc(bkId, PageRequest.of(0,10));
    }

    @Override
    public void compareWithBaseFile(String bkId, String problemId, String language) throws CustomExitException {
        try {
            String fileExtension = submissionService.getFileExtension(language);
            String baseFilePath = String.format("%s%s/base/%s.%s", BASE_PATH, problemId, bkId, fileExtension);
            String solutionsPath = String.format("%s%s/%s", BASE_PATH, problemId, fileExtension);

            File baseFile = new File(baseFilePath);
            if (!baseFile.exists()) {
                throw new CustomExitException("Base file not found: " + baseFilePath);
            }

            Path tempDir = FileUtil.createTempDirectory();
            FileUtil.copyFile(baseFile.toPath(), tempDir.resolve(baseFile.getName()));
            FileUtil.copyFilesFromDirectory(solutionsPath, tempDir);

            List<JPlagComparison> comparisons = compareSolutions(tempDir.toString(), language);

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
        } catch (Exception e) {
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        }
    }

    @Override
    public List<JPlagComparison> compareSolutions(String solutionPath, String language) throws CustomExitException {
        try {
            LanguageOption languageOption = switch (language.toLowerCase()) {
                case "java" -> LanguageOption.JAVA;
                case "c++", "c" -> LanguageOption.C_CPP;
                case "python" -> LanguageOption.PYTHON_3;
                default -> throw new CustomExitException("Unsupported language: " + language);
            };

            JPlagOptions options = new JPlagOptions(solutionPath, languageOption);
            JPlag jplag = new JPlag(options);
            JPlagResult result = jplag.run();

            return result.getComparisons();
        } catch (ExitException e) {
            throw new CustomExitException("Error during comparison: " + e.getMessage());
        }
    }

    private void saveComparisonResult(String baseFileName, String comparedFileName, double similarity, long problemId) throws CustomExitException {
        String bkId = baseFileName.substring(0, baseFileName.lastIndexOf("."));
        Submission submission = submissionRepository.findByBkId(bkId);

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
}
