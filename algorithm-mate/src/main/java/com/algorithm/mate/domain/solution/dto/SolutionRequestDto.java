package com.algorithm.mate.domain.solution.dto;

import com.algorithm.mate.domain.solution.entity.Solution;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class SolutionRequestDto {
    private String problemId;
    private String filePath;
    private String language;
    private String userId;
    private String code;
    private String mimeType;

    // DTO 내부에서 엔티티로 변환하는 메서드 구현
    public Solution toSolution() {
        return new Solution(
                this.problemId,
                this.filePath,
                this.language,
                this.userId
                // 필요 시 this.code, this.mimeType 등을 추가
        );
    }
}
