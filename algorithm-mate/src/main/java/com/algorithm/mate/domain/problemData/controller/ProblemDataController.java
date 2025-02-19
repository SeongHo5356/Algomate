package com.algorithm.mate.domain.problemData.controller;

import com.algorithm.mate.domain.problemData.dto.ProblemDataRequestDto;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@Slf4j
@Controller
public class ProblemDataController {

    @PostMapping("api/v1/problemData/submit-data")
    public String handleProblemData(@RequestBody ProblemDataRequestDto request){
        // 데이터 처리 로직
        log.info("문제 페이지 접근: problem_id : {}, userId : {}", request.getTitle(), request.getUserId());
        // 응답
        return "Data received successfully!";
    }
}
