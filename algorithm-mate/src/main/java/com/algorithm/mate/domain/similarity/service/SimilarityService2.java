package com.algorithm.mate.domain.similarity.service;

import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import com.algorithm.mate.domain.similarity.entity.Similarity;
import de.jplag.JPlagComparison;

import java.util.List;

public interface SimilarityService2 {
    /**
     * 솔루션 폴더 내의 파일들끼리 유사도를 비교합니다.
     * @param solutionPath 비교할 폴더 경로
     * @param language 언어 정보
     * @return 비교 결과 리스트
     * @throws CustomExitException 에러 발생 시 예외
     */
    List<JPlagComparison> compareSoltions(String solutionPath, String language) throws CustomExitException;

    /**
     * 기준 파일과 정답 파일들을 비교합니다.
     * @param bkId 기준 파일의 bkId
     * @param problemId 문제 아이디
     * @param language 언어 정보
     * @throws CustomExitException 에러 발생 시 예외
     */
    void compareWithBaseFile(String bkId, String problemId, String language) throws CustomExitException;

    /**
     * 주어진 제출(bkId)에 대해 상위 10개의 유사 결과를 조회합니다.
     * @param bkId 제출의 bkId
     * @return 유사 결과 리스트
     * @throws CustomExitException 에러 발생 시 예외
     */
    List<Similarity> getTop10SimilaritiesByBkId(String bkId) throws CustomExitException;

    // 유사도 계산 메서드 정의
    String similarityCalculate(String bkId, String problemId, String language) throws CustomExitException;

    // 상위 유사 코드 파일 조회 메서드 정의
    List<String> getTopSimilarityFiles(String bkId) throws CustomExitException;


}
