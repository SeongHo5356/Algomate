package com.algorithm.mate.domain.similarity.service;

import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import de.jplag.JPlagComparison;

import java.util.List;

public interface SimilarityService2 {
    /**
     * 특정 문제 ID에 대한 유사한 코드 목록을 조회
     */
    List<Similarity> getTop10SimilaritiesByBkId(String bkId) throws CustomExitException;

    /**
     * 제출물과 기존 솔루션을 비교하여 유사도를 계산
     */
    void compareWithBaseFile(String bkId, String problemId, String language) throws CustomExitException;

    /**
     * JPlag를 사용하여 코드 비교
     */
    List<JPlagComparison> compareSolutions(String solutionPath, String language) throws CustomExitException;

}
