package com.algorithm.mate.domain.problemData.controller;

import com.algorithm.mate.domain.problemData.dto.ProblemDataRequestDto;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@Controller
public class ProblemDataController {

    @PostMapping("api/v1/submit-data")
    public String handleProblemData(@RequestBody ProblemDataRequestDto request){
        // 데이터 처리 로직
        System.out.println("Received title: " + request.getTitle());
        System.out.println("Received userId: " + request.getUserId());

        // 응답
        return "Data received successfully!";
    }
}
