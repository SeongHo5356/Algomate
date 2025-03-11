package com.algorithm.mate.domain.crawling.controller;

import com.algorithm.mate.domain.crawling.infrastructure.WebClientService;
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

    private final WebClientService webClientService;

    public CrawlingController(WebClientService webClientService) {
        this.webClientService = webClientService;
    }
    @GetMapping("/task-status/{taskId}")
    public Mono<ResponseEntity<String>> getTaskStatus(@PathVariable("taskId") String taskId) {
        return webClientService.getTaskStatus(taskId)
                .map(ResponseEntity::ok)
                .onErrorResume(e -> Mono.just(ResponseEntity.status(502)
                        .body("FastAPI 서버 응답 실패: " + e.getMessage())));
    }

}
