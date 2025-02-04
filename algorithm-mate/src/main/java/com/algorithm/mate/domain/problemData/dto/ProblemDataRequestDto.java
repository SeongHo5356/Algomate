package com.algorithm.mate.domain.problemData.dto;

public class ProblemDataRequestDto {
    private String title;
    private String content;
    private String userId;

    public ProblemDataRequestDto(){}

    public ProblemDataRequestDto(String title, String content, String userId) {
        this.title = title;
        this.content = content;
        this.userId = userId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }
}
