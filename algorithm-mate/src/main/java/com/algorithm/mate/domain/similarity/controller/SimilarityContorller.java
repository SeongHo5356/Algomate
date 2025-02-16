package com.algorithm.mate.domain.similarity.controller;

import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.service.SimilarityService;
import com.algorithm.mate.domain.similarity.service.SimilarityService2;
import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import de.jplag.exceptions.ExitException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/v1/similarity")
public class SimilarityContorller {

    @Autowired
    private SimilarityService2 similarityService;
    @Autowired
    private SubmissionRepository submissionRepository;
    @Autowired
    private SolutionRepository solutionRepository;

    // bkId는 물론 language와 problem_id도 같이 요청을 받음
    // => bkId를 통해서 submission 테이블에서 language, problem_id를 조회하는 과정이 생략됨
    // => 그러나 bkId를 통해서 있는지 없는 지 먼저 조회해보면 될듯?
    @PostMapping("/compare")
    public String similarityCalculate(String bkId, String problemId, String language) throws CustomExitException {

        // 제출물을 존재하는지 조회
        Submission submission = submissionRepository.findByBkId(bkId);
        // 비교할 데이터가 존재하는 지 조회

        if (submission != null) { // 존재할때
            List<Solution> solutions = solutionRepository.findByProblemIdAndLanguage(problemId, language);
            if(!solutions.isEmpty()){
                log.info("submission 조회 성공 및 solutions 존재");
                similarityService.compareWithBaseFile(bkId, problemId, language);
            }
            else{
                System.out.println("solutions가 없습니다.");
            }

        } else { // 존재하지 않을 때
            System.out.println("submission 조회 실패");
        }

        return "1";
    }

    @GetMapping("/select5")
    public ResponseEntity<List<String>> getTopSimilarities(@RequestParam String bkId) throws CustomExitException {
        List<Similarity> topSimilarities = similarityService.getTop10SimilaritiesByBkId(bkId);

        System.out.println("==== 유사 코드 목록 ====");
        List<String> filePaths = new ArrayList<>();

        for (Similarity similarity : topSimilarities) {
            long problemId = similarity.getProblemId(); // 문제 번호
            String fileName = similarity.getAnswerId(); // 파일 이름

            // 🔹 상대 경로로 변환
            String relativePath = String.format("%d/py/%s", problemId, fileName);
            Path absolutePath = Paths.get("/Users/sungho/Documents/study/Algomate/algorithm-mate/src/main/resources/solutions", relativePath);

            // 🔹 파일이 존재하는 경우만 추가
            if (Files.exists(absolutePath)) {
                filePaths.add(relativePath);
                System.out.println("파일 경로: " + relativePath);
            } else {
                System.out.println("❌ 파일 없음: " + relativePath);
            }

            System.out.println("---------------------");
        }

//        /Users/sungho/Documents/study/Algomate/algorithm-mate/src/main/resources/solutions/1027/py/gbyeo31.py
        return ResponseEntity.ok(filePaths);
    }

}
