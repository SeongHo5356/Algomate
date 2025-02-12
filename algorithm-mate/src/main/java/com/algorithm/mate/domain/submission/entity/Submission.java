package com.algorithm.mate.domain.submission.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity
@Table(name = "submissions")
@Getter @Setter
public class Submission {

    @Id
    @Column(name = "bk_id")
    private String bkId;

    @Column(name = "problem_id", nullable = false)
    private String problemId;

    @Column(name = "language", nullable = false)
    private String language;

    @Column(name = "user_id", nullable = false)
    private String userId;

    @Column(name = "code", columnDefinition = "TEXT")
    private String code;

    @Column(name = "created_at")
    private LocalDateTime createdAt = LocalDateTime.now();

    // 생성자, getter, setter
    public Submission() {}

    public Submission(String bkId, String problemId, String language, String userId, String code) {
        this.bkId = bkId;
        this.problemId = problemId;
        this.language = language;
        this.userId = userId;
        this.code = code;
        this.createdAt = LocalDateTime.now();
    }
}