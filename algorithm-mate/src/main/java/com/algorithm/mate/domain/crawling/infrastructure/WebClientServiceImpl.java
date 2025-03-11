package com.algorithm.mate.domain.crawling.infrastructure;

import io.swagger.v3.oas.annotations.servers.Server;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@Service
public class WebClientServiceImpl implements WebClientService {

    private final WebClient webClient;

    public WebClientServiceImpl(WebClient.Builder webClientBuilder,
                                @Value("${fastapi.base-url}") String fastApiBaseUrl) {
        this.webClient = webClientBuilder.baseUrl(fastApiBaseUrl).build();
    }

    @Override
    public Mono<String> getTaskStatus(String taskId){
        return webClient.get()
                .uri("/api/task-status/{taskId}", taskId)
                .retrieve()
                .bodyToMono(String.class);
    }
}
