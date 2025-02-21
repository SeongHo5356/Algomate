package com.algorithm.mate.domain.crawling.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/api/v1/crawling")
public class CrawlingController {

    private final WebClient webClient;

    public CrawlingController(WebClient.Builder webClientBuilder, @Value("${fastapi.base-url}") String fastApiBaseUrl) {
        this.webClient = webClientBuilder.baseUrl("http://localhost:8080").build();
    }

    @GetMapping("/task-status/{taskId}")
    public Mono<ResponseEntity<String>> getTaskStatus(@PathVariable("taskId") String taskId) {
        return webClient.get()
                .uri("/api/task-status/{taskId}", taskId)
                .retrieve()
                .bodyToMono(String.class)
                .map(ResponseEntity::ok)
                .onErrorResume(e
                        -> Mono.just(ResponseEntity.status(502)
                        .body("FastAPI 서버 응답 실패: " + e.getMessage())));
    }

}
