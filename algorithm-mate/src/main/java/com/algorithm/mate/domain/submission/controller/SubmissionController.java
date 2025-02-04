package com.algorithm.mate.domain.submission.controller;

import com.algorithm.mate.domain.problemData.dto.ProblemDataRequestDto;
import com.algorithm.mate.domain.submission.dto.SubmissionRequestDto;
import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.service.SubmissionService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/submission")
public class SubmissionController {

    private final SubmissionService submissionService;

    public SubmissionController(SubmissionService submissionService) {
        this.submissionService = submissionService;
    }

    @PostMapping("/submit-code")
    public String handleProblemData(@RequestBody SubmissionRequestDto request){

        // DTO를 entity로 변환
        Submission submission = new Submission(
                request.getBkId(),
                request.getProblemId(),
                request.getLanguage(),
                request.getUserId(),
                request.getCode()
        );

        // 데이터베이스에 저장
        submissionService.saveOrUpdateSubmission(submission);

        return "Code submitted successfully!";
    }
}
