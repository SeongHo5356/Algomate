package com.algorithm.mate.domain.similarity.controller;

import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.service.SimilarityService;
import com.algorithm.mate.domain.similarity.service.SimilarityService2;
import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/v2/similarity")
public class SimilarityController2 {

    @Autowired
    private SimilarityService2 similarityService;

    @Autowired
    private SubmissionRepository submissionRepository;

    @Autowired
    private SolutionRepository solutionRepository;

    // 유사도 계산 요청 처리
    @PostMapping("/compare")
    public String similarityCalculate(@RequestParam String bkId,
                                      @RequestParam String problemId,
                                      @RequestParam String language) throws CustomExitException {

        return similarityService.similarityCalculate(bkId, problemId, language);
    }

    // 유사 코드 목록 조회
    @GetMapping("/select5")
    public ResponseEntity<List<String>> getTopSimilarities(@RequestParam String bkId) throws CustomExitException {
        List<String> filePaths = similarityService.getTopSimilarityFiles(bkId);
        return ResponseEntity.ok(filePaths);
    }
}
