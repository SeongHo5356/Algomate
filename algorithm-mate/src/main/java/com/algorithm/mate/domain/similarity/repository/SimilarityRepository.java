package com.algorithm.mate.domain.similarity.repository;

import com.algorithm.mate.domain.similarity.entity.Similarity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SimilarityRepository extends JpaRepository<Similarity, Long> {
}
