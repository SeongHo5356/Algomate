package com.algorithm.mate.domain.submission.service;

import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

@Service
public class SubmissionService {

    //파일 저장 경로
    private static final String BASE_PATH = "resources/solutions";

    private final SubmissionRepository submissionRepository;

    public SubmissionService(SubmissionRepository submissionRepository) {
        this.submissionRepository = submissionRepository;
    }

    public Submission saveOrUpdateSubmission(Submission submission) {
        // 복합 기본키로 데이터 조회
        Submission existingSubmission = submissionRepository
                .findByBkId(submission.getBkId());

        if (existingSubmission != null) {
            System.out.println("존재하는 것");
            // 기존 데이터 업데이트
            existingSubmission.setProblemId(submission.getProblemId());
            existingSubmission.setLanguage(submission.getLanguage());
            existingSubmission.setUserId(submission.getUserId());
            existingSubmission.setCode(submission.getCode());
            existingSubmission.setCreatedAt(submission.getCreatedAt());
            return saveSubmission(existingSubmission);
        } else {
            // 새 데이터 삽입
            return saveSubmission(submission);
        }
    }

    public Submission saveSubmission(Submission submission) {
        return submissionRepository.save(submission);
    }

    public void saveCodeToFile(String problemId, String language, String bkId, String code) throws IOException {
        // 확장자 결정
        String extension = getFileExtension(language);

        // 파일 경로 생성
        String filePath = BASE_PATH + problemId + "/base/" + bkId + "." + extension;

        // 디렉토리 생성
        File directory = new File(BASE_PATH + problemId + "/base");
        if (!directory.exists()) {
            directory.mkdirs();
        }

        // 파일에 코드 저장
        try (FileWriter writer = new FileWriter(filePath)) {
            writer.write(code);
        }
    }

    public String getFileExtension(String language) {
        switch(language.toLowerCase()){
            case "java":
                return "java";
            case "python":
                return "py";
            case "c++":
                return "cpp";
            case "c":
                return "c";
            default:
                throw new IllegalArgumentException("Unsupported language: " + language);
        }
    }

}
