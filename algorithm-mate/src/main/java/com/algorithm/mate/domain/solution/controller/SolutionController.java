package com.algorithm.mate.domain.solution.controller;

import com.algorithm.mate.domain.solution.dto.SolutionRequestDto;
import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.service.SolutionService;
import com.algorithm.mate.domain.submission.dto.SubmissionRequestDto;
import com.algorithm.mate.domain.submission.entity.Submission;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/v1/solution")
public class SolutionController {

    private final SolutionService solutionService;

    @Autowired
    public SolutionController(SolutionService solutionService){
        this.solutionService = solutionService;
    }

    @GetMapping("/solutions")
    public List<Solution> getSolution(@RequestParam String problemId){
        return solutionService.getSolutionsByProblemId(problemId);
    }

    @PostMapping("/save")
    public String handleSolution(@RequestBody SolutionRequestDto request){

        log.info("handle problemID: {}", request.getProblemId());
        log.info(request.getFilePath());
        log.info(request.getLanguage());
        log.info("handle userId: {}", request.getUserId());
        // DTO를 entity로 변환
        Solution solution = new Solution(
                request.getProblemId(),
                request.getFilePath(),
                request.getLanguage(),
                request.getUserId()
        );

        // 데이터베이스에 저장
        solutionService.saveOrUpdateSolution(solution);

        return "Code submitted successfully!";
    }
}
