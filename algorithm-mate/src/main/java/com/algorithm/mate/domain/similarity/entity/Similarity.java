package com.algorithm.mate.domain.similarity.entity;

import com.algorithm.mate.domain.submission.entity.Submission;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;


@Entity
@Table(name = "similarities")
@Getter @Setter
@AllArgsConstructor
@NoArgsConstructor
public class Similarity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "similarity_id")
    private long similarityId;

    @ManyToOne
    @JoinColumn(name = "bk_id", nullable = false)
    private Submission submission;

    @Column(name = "problem_id", nullable = false)
    private long problemId;

    @Enumerated(EnumType.STRING)
    @Column(name = "language", nullable = false)
    private Language language;

    @Column(name = "submission_id", nullable = false)
    private String submissionId;

    @Column(name = "answer_id")
    private String answerId;

    @Column(name = "similarity_score")
    private double similarityScore;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt = LocalDateTime.now();
}
