package com.algorithm.mate.domain.solution.service;

import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.when;

class SolutionServiceTest {

    @Mock
    private SolutionRepository solutionRepository;

    @InjectMocks
    private SolutionService solutionService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    // 성공 테스트
    @Test
    @DisplayName("현재 100개 이하기 때문에 false 가 출력돼야한다.")
    void givenLessThan100Solutions(){
        //given
        String problemId = "1027";
        String language = "py";

        when(solutionRepository.countByProblemIdAndLanguage(problemId, language)).thenReturn(99L);
        //when
        boolean result = solutionService.hasAtLeast100Solutions(problemId, language);

        //then
        assertFalse(result);
    }

    @Test
    @DisplayName("현재 100개 이하기 때문에 false 가 출력돼야한다.")
    void givenExactly100Solutions(){
        //given
        String problemId = "1027";
        String language = "py";
        when(solutionRepository.countByProblemIdAndLanguage(problemId, language)).thenReturn(100L);

        //when
        boolean result = solutionService.hasAtLeast100Solutions(problemId, language);

        //then
        assertTrue(result);
    }
    // 실패 테스트

    @Test
    @DisplayName("현재 100개 이하기 때문에 false 가 출력돼야한다.")
    void givenMoreThan100Solutions(){
        //given
        String problemId = "1027";
        String language = "py";
        when(solutionRepository.countByProblemIdAndLanguage(problemId, language)).thenReturn(101L);

        //when
        boolean result = solutionService.hasAtLeast100Solutions(problemId, language);

        //then
        assertTrue(result);
    }
}