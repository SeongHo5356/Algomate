package com.algorithm.mate.domain.solution.repository;

import com.algorithm.mate.domain.solution.entity.Solution;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SolutionRepository extends JpaRepository<Solution, Long> {
    List<Solution> findAllByUserId(String userId);

    Solution findByUserIdAndLanguage(String userId, String language);
}
