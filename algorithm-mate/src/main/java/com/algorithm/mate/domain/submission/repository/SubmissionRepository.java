package com.algorithm.mate.domain.submission.repository;

import com.algorithm.mate.domain.submission.entity.Submission;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SubmissionRepository extends JpaRepository<Submission, String> {
    // 복합 기본키로 데이터 조회
    Submission findByBkId(String bkId);
}
