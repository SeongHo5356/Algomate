package com.algorithm.mate.domain.submission.service;

import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import org.springframework.stereotype.Service;

@Service
public class SubmissionService {

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
            return submissionRepository.save(existingSubmission);
        } else {
            // 새 데이터 삽입
            return submissionRepository.save(submission);
        }
    }
    public Submission saveSubmission(Submission submission) {
        return submissionRepository.save(submission);
    }
}
