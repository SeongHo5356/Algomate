package com.algorithm.mate.domain.similarity.entity;

import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "similarities")
public class Similarity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "similarity_id")
    private long similarityId;

    @Column(name = "problem_id")
    private long problemId;

    public Language getLanguage() {
        return language;
    }

    public void setLanguage(Language language) {
        this.language = language;
    }

    @Enumerated(EnumType.STRING)
    @Column(name = "language")
    private Language language;

    @Column(name = "submission_id")
    private String submissionId;

    @Column(name = "answer_id")
    private String answerId;

    @Column(name = "similarity_score")
    private double similarityScore;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    // 생성자, getter, setter
    public long getProblemId() {
        return problemId;
    }

    public void setProblemId(long problemId) {
        this.problemId = problemId;
    }
    public long getSimilarityId() {
        return similarityId;
    }

    public void setSimilarityId(long similarityId) {
        this.similarityId = similarityId;
    }

    public String getAnswerId() {
        return answerId;
    }

    public void setAnswerId(String answerId) {
        this.answerId = answerId;
    }

    public String getSubmissionId() {
        return submissionId;
    }

    public void setSubmissionId(String submissionId) {
        this.submissionId = submissionId;
    }

    public double getSimilarityScore() {
        return similarityScore;
    }

    public void setSimilarityScore(double similarityScore) {
        this.similarityScore = similarityScore;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

}
