package com.algorithm.mate.domain.submission.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "submissions")
public class Submission {

    @Id
    @Column(name = "bk_id")
    private String bkId;

    @Column(name = "problem_id")
    private String problemId;

    @Column(name = "language")
    private String language;

    @Column(name = "user_id")
    private String userId;

    @Column(name = "code", columnDefinition = "TEXT")
    private String code;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

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

    public String getBkId() {
        return bkId;
    }

    public void setBkId(String bkId) {
        this.bkId = bkId;
    }

    public String getProblemId() {
        return problemId;
    }

    public void setProblemId(String problemId) {
        this.problemId = problemId;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }
}