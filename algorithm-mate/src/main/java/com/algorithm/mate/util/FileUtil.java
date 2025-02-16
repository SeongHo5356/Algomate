package com.algorithm.mate.util;

import com.algorithm.mate.domain.similarity.exception.CustomExitException;

import java.nio.file.Path;

public interface FileUtil {
    /**
     * 임시 디렉토리를 생성합니다.
     * @return 생성된 임시 디렉토리의 Path
     * @throws CustomExitException 생성 실패 시 예외
     */
    Path createTempDirectory() throws CustomExitException;

    /**
     * 단일 파일을 복사합니다.
     * @param source 원본 파일 경로
     * @param target 대상 파일 경로
     * @throws CustomExitException 복사 실패 시 예외
     */
    void copyFile(Path source, Path target) throws CustomExitException;

    /**
     * 지정한 디렉토리의 모든 파일을 대상 디렉토리로 복사합니다.
     * @param sourceDir 원본 디렉토리 경로
     * @param targetDir 대상 디렉토리의 Path
     * @throws CustomExitException 복사 실패 시 예외
     */
    void copyFilesFromDirectory(String sourceDir, Path targetDir) throws CustomExitException;
}
