package com.algorithm.mate.domain.crawling.infrastructure;

import reactor.core.publisher.Mono;

public interface WebClientService {
    Mono<String> getTaskStatus(String taskId);
}
