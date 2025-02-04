package com.algorithm.mate.domain.submission.dto;

public class SubmissionRequestDto {
    private String code;
    private String problemId;
    private String userId;
    private String language;
    private String bkId;

    public SubmissionRequestDto() {
    }

    public SubmissionRequestDto(String code, String problemId, String userId, String language, String bkId) {
        this.code = code;
        this.problemId = problemId;
        this.userId = userId;
        this.language = language;
        this.bkId = bkId;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getProblemId() {
        return problemId;
    }

    public void setProblemId(String problemId) {
        this.problemId = problemId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public String getBkId() {
        return bkId;
    }

    public void setBkId(String bkId) {
        this.bkId = bkId;
    }
}
