package com.algorithm.mate.domain.solution.controller;

import com.algorithm.mate.domain.solution.dto.SolutionRequestDto;
import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.service.SolutionService;
import org.springframework.core.io.Resource;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.FileSystemResource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/v1/solution")
public class SolutionController {

    private final SolutionService solutionService;

    @Autowired
    public SolutionController(SolutionService solutionService){
        this.solutionService = solutionService;
    }

    @GetMapping("/solutions")
    public List<Solution> getSolution(@RequestParam String problemId){
        return solutionService.getSolutionsByProblemId(problemId);
    }

    @PostMapping("/save")
    public ResponseEntity<String> saveSolution(@RequestBody SolutionRequestDto request) throws IOException {

        log.info("📌 문제 ID: {}", request.getProblemId());
        log.info("📌 파일 경로: {}", request.getFilePath());
        log.info("📌 언어: {}", request.getLanguage());
        log.info("📌 유저 ID: {}", request.getUserId());
//        log.info("📌 코드 내용: \n{}", request.getCode());  // ✅ 코드 출력

        // DTO를 entity로 변환
        Solution solution = new Solution(
                request.getProblemId(),
                request.getFilePath(),
                request.getLanguage(),
                request.getUserId()
        );

        // 파일로 저장
        solutionService.saveCodeToFile(request.getProblemId(), request.getFilePath(), request.getLanguage(), request.getCode());

        // 데이터베이스에 저장
        solutionService.saveOrUpdateSolution(solution);

        return ResponseEntity.ok("✅ Code submitted successfully!");
    }


    private final String basePath = "/app/resources/solutions/";

    @GetMapping("/{dir}/{subdir}/{filename:.+}")
    public ResponseEntity<Resource> getFile(
            @PathVariable String dir,
            @PathVariable String subdir,
            @PathVariable String filename) {

        // 실제 파일 경로 생성 (예: /Users/.../solutions/2623/py/87165878.py)
        Path filePath = Paths.get(basePath, dir, subdir, filename);
        File file = filePath.toFile();

        // 파일 리소스 생성
        Resource resource = new FileSystemResource(file);

        // 파일 타입에 따라 ContentType 설정 (여기서는 단순히 text/plain으로 처리)
        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_DISPOSITION, "inline; filename=\"" + StringUtils.cleanPath(file.getName()) + "\"");

        return ResponseEntity.ok()
                .headers(headers)
                .contentLength(file.length())
                .contentType(MediaType.TEXT_PLAIN)
                .body(resource);
    }
}
