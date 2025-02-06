package com.algorithm.mate.domain.solution.repository;

import com.algorithm.mate.domain.similarity.entity.Language;
import com.algorithm.mate.domain.solution.entity.Solution;
import org.springframework.beans.factory.parsing.Problem;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SolutionRepository extends JpaRepository<Solution, Long> {
    List<Solution> findAllByUserId(String userId);
    List<Solution> findByProblemIdAndLanguage(String problemId, String language);

    Solution findByUserIdAndLanguage(String userId, String language);
}
