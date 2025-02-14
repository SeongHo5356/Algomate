package com.algorithm.mate.domain.solution.service;

import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import com.algorithm.mate.domain.submission.entity.Submission;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service
public class SolutionService {

    private final SolutionRepository solutionRepository;

    @Autowired
    public SolutionService(SolutionRepository solutionRepository) {
        this.solutionRepository = solutionRepository;
    }

    public List<Solution> getSolutionsByProblemId(String problemId) {
        return solutionRepository.findAllByUserId(problemId);
    }

    public Solution saveOrUpdateSolution(Solution solution) {

        Solution existingSolution = solutionRepository.findByUserIdAndLanguage(solution.getUserId(),solution.getLanguage());

        // 이미 동일한 걸로 존재하면,
        if (existingSolution != null) {
            log.info("동일 정답 존재");
            // 기존 데이터 업데이트
            return saveSolution(existingSolution);
        }
        else{
            return saveSolution(solution);
        }
    }

    public Solution saveSolution(Solution solution) {
        return solutionRepository.save(solution);
    }

    // 현재 요청받은 문제번호와 언어를 기반으로 기존에 크롤링 된 답변들이 100개 이상 존재하는 지 검증
    // 1개라도 있는지 검증 solutionRepository.existsByProblemIdAndLanguage
    // 100개 이상 있는지 검증 solutionRepository.hsaAtLeast100Solutions()
    public boolean hasAtLeast100Solutions(String problemId, String language){
        long count = solutionRepository.countByProblemIdAndLanguage(problemId,language);

        return count >= 100;
    }
}
