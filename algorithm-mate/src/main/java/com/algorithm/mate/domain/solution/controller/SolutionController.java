package com.algorithm.mate.domain.solution.controller;

import com.algorithm.mate.domain.solution.dto.SolutionRequestDto;
import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.service.SolutionService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
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
    public ResponseEntity<String> saveSolution(@RequestBody SolutionRequestDto request) throws IOException {

        log.info("📌 문제 ID: {}", request.getProblemId());
        log.info("📌 파일 경로: {}", request.getFilePath());
        log.info("📌 언어: {}", request.getLanguage());
        log.info("📌 유저 ID: {}", request.getUserId());
//        log.info("📌 코드 내용: \n{}", request.getCode());  // ✅ 코드 출력

        // DTO를 entity로 변환
        Solution solution = new Solution(
                request.getProblemId(),
                request.getFilePath(),
                request.getLanguage(),
                request.getUserId()
        );

        // 파일로 저장
        solutionService.saveCodeToFile(request.getProblemId(), request.getFilePath(), request.getLanguage(), request.getCode());

        // 데이터베이스에 저장
        solutionService.saveOrUpdateSolution(solution);

        return ResponseEntity.ok("✅ Code submitted successfully!");
    }
}
