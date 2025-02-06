package com.algorithm.mate.domain.similarity.controller;

import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.service.SimilarityService;
import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import com.algorithm.mate.domain.submission.dto.SubmissionRequestDto;
import com.algorithm.mate.domain.submission.entity.Submission;
import com.algorithm.mate.domain.submission.repository.SubmissionRepository;
import de.jplag.JPlagComparison;
import de.jplag.exceptions.ExitException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/v1/similarity")
public class SimilarityContorller {

    @Autowired
    private SimilarityService similarityService;

    @Autowired
    private SubmissionRepository submissionRepository;
    @Autowired
    private SolutionRepository solutionRepository;

    @PostMapping("/compare2")
    public String compareSolutions2(String problemId, String language){

        String baseFilePath = System.getProperty("user.dir") + "/src/main/resources/solutions/" +problemId+ "/base";
        String solutionsPath = System.getProperty("user.dir") + "/src/main/resources/solutions/" + problemId + "/" + language;

        try{
            similarityService.compareWithBaseFiles(baseFilePath, solutionsPath);
            return "Comparison completed and results saved to database.";
        } catch (ExitException e){
            return "Error during comparison: " + e.getMessage();
        }
    }

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
}
