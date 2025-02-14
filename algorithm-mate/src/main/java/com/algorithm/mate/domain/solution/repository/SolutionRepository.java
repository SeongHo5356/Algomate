package com.algorithm.mate.domain.solution.repository;

import com.algorithm.mate.domain.solution.entity.Solution;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface SolutionRepository extends JpaRepository<Solution, Long> {
    List<Solution> findAllByUserId(String userId);
    List<Solution> findByProblemIdAndLanguage(String problemId, String language);

    Solution findByUserIdAndLanguage(String userId, String language);

    boolean existsByProblemIdAndLanguage(String problemId, String language);

    long countByProblemIdAndLanguage(String problemId, String language);
}
