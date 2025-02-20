package com.algorithm.mate.domain.similarity.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@AllArgsConstructor
@NoArgsConstructor
// JSON Body를 받을 DTO 클래스 추가
public class SimilarityCalculateRequestDto {
    private String bkId;
    private String problemId;
    private String language;
}
