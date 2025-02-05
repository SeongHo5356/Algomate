package com.algorithm.mate.domain.solution.dto;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class SolutionRequestDto {
    private String problemId;
    private String filePath;
    private String language;
    private String userId;
}
