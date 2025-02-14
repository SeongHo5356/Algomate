package com.algorithm.mate.domain.similarity.repository;

import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.submission.entity.Submission;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SimilarityRepository extends JpaRepository<Similarity, Long> {
    boolean existsByAnswerIdAndSubmission(String answerId, Submission submission);

    List<Similarity> findBySubmission_BkIdOrderBySimilarityScoreDesc(String bkId, Pageable pageable);
}

