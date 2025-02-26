package com.algorithm.mate.domain.similarity.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class SolutionFilePathResolver {

    private final String solutionsBasePath;

    public SolutionFilePathResolver(@Value("${solutions.base-path}") String solutionsBasePath) {
        this.solutionsBasePath = solutionsBasePath;
    }

    public String getBaseFilePath(String problemId, String bkId, String fileExtension) {
        return String.format("%s/%s/base/%s.%s", solutionsBasePath, problemId, bkId, fileExtension);
    }

    public String getSolutionsPath(String problemId, String fileExtension) {
        return String.format("%s/%s/%s", solutionsBasePath, problemId, fileExtension);
    }

    // 추가: 베이스 경로를 직접 반환하는 메서드
    public String getSolutionsBasePath() {
        return solutionsBasePath;
    }
}