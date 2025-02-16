package com.algorithm.mate.util;

import com.algorithm.mate.domain.similarity.exception.CustomExitException;
import lombok.extern.slf4j.Slf4j;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

@Slf4j
public class FileUtilImpl implements FileUtil {

    @Override
    public Path createTempDirectory() throws CustomExitException {
        try {
            return Files.createTempDirectory("jplag");
        } catch (Exception e) {
            throw new CustomExitException("Failed to create temp directory: " + e.getMessage());
        }
    }

    @Override
    public void copyFile(Path source, Path target) throws CustomExitException {
        try {
            Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
        } catch (Exception e) {
            throw new CustomExitException("Failed to copy file: " + e.getMessage());
        }
    }

    @Override
    public void copyFilesFromDirectory(String sourceDir, Path targetDir) throws CustomExitException {
        try {
            File[] files = new File(sourceDir).listFiles();
            if (files != null) {
                for (File file : files) {
                    copyFile(file.toPath(), targetDir.resolve(file.getName()));
                }
            }
        } catch (Exception e) {
            throw new CustomExitException("Failed to copy files: " + e.getMessage());
        }
    }
}
