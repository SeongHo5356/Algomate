package com.algorithm.mate.domain.similarity.controller;

import com.algorithm.mate.domain.similarity.dto.SimilarityCalculateRequestDto;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.service.SimilarityService2;
import com.algorithm.mate.domain.solution.service.SolutionService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.reactive.function.client.WebClient;

import java.net.URI;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@RestController
@RequestMapping("/api/v2/similarity")
public class SimilarityController2 {

    @Autowired
    private SimilarityService2 similarityService;

    @Autowired
    private SolutionService solutionService;

    private WebClient.Builder webClientBuilder;

    @Autowired
    public SimilarityController2(WebClient.Builder webClientBuilder) {
        this.webClientBuilder = webClientBuilder;
    }

    // 유사도 계산 요청 처리
    @PostMapping("/compare")
    public ResponseEntity<String> triggerCrawlingAndCalculate(@RequestBody SimilarityCalculateRequestDto requestDto) throws CustomExitException {

        // 크롤링 검증
        // 100개 이상 솔루션이 있는지 확인
        boolean hasEnoughSolutions = solutionService.hasAtLeast100Solutions(requestDto.getProblemId(), requestDto.getLanguage());

        if (!hasEnoughSolutions) {   // 크롤링 돼 있음 -> 크롤링

            // 크롤링 API 엔드포인트 호출
            String crawlApiUrl = "http://fastapi_app:8000/api/scrape";
            System.out.println("crawlApiUrl: " + crawlApiUrl);
            System.out.println("requestDto: " + requestDto.getProblemId());
            System.out.println("language_id: " + requestDto.getLanguage());

            // 요청 바디 생성 (JSON 형식)
            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("problem_id", requestDto.getProblemId());
            requestBody.put("language_id", requestDto.getLanguage());

            // WebClient 요청 보내기 (POST + JSON Body)
            String response = webClientBuilder.build()
                    .post() // ✅ POST 요청
                    .uri(URI.create(crawlApiUrl)) // ✅ 직접 URL 지정
                    .contentType(MediaType.APPLICATION_JSON) // ✅ JSON 데이터 전송
                    .bodyValue(requestBody) // ✅ JSON 바디 설정
                    .retrieve()
                    .bodyToMono(String.class)
                    .block(); // 동기 요청 (필요하면 비동기로 변경 가능)

            System.out.println("Response from FastAPI: " + response);

            if (response != null) {
                return ResponseEntity.ok("Crawling triggered: " + response);
            } else {
                return ResponseEntity.status(500).body("Crawling failed: No response from FastAPI");
            }
        }

        similarityService.similarityCalculate(requestDto.getBkId(), requestDto.getProblemId(), requestDto.getLanguage());
        return ResponseEntity.ok("✅ code similarity Calculated Successfully!");
        // -> 프론트에서 해당 문제에 대한 유사코드 준비가 완료됐습니다.
    }

    // 유사 코드 목록 조회
    @GetMapping("/select5")
    public ResponseEntity<List<String>> getTopSimilarities(@RequestParam String bkId) throws CustomExitException {
        List<String> filePaths = similarityService.getTopSimilarityFiles(bkId);
        return ResponseEntity.ok(filePaths);
    }
}
