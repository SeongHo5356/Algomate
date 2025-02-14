package com.algorithm.mate.domain.similarity.repository;

import com.algorithm.mate.domain.similarity.entity.Similarity;
import com.algorithm.mate.domain.submission.entity.Submission;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SimilarityRepository extends JpaRepository<Similarity, Long> {
    boolean existsByAnswerIdAndSubmission(String answerId, Submission submission);
}
