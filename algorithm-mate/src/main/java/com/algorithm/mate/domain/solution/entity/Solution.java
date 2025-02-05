package com.algorithm.mate.domain.solution.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter @Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "solutions")
public class Solution {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "problem_id", nullable = false)
    private String problemId;

    @Column(name = "file_path", nullable = false)
    private String filePath;

    @Column(name = "language", nullable = false)
    private String language;

    @Column(name = "user_id")
    private String userId;

    // id 제외 생성자
    public Solution(String problemId, String filePath, String language, String userId) {
        this.problemId = problemId;
        this.filePath = filePath;
        this.language = language;
        this.userId = userId;
    }
}
