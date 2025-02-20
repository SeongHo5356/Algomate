package com.algorithm.mate.domain.solution.service;

import com.algorithm.mate.domain.solution.entity.Solution;
import com.algorithm.mate.domain.solution.repository.SolutionRepository;
import com.algorithm.mate.domain.submission.entity.Submission;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

@Slf4j
@Service
public class SolutionService {

    //파일 저장 경로
    private static final String BASE_PATH = "src/main/resources/";

    private final SolutionRepository solutionRepository;

    @Autowired
    public SolutionService(SolutionRepository solutionRepository) {
        this.solutionRepository = solutionRepository;
    }

    public List<Solution> getSolutionsByProblemId(String problemId) {
        return solutionRepository.findAllByUserId(problemId);
    }

    public Solution saveOrUpdateSolution(Solution solution) throws IOException {

        Solution existingSolution = solutionRepository.findByUserIdAndLanguage(solution.getUserId(),solution.getLanguage());

        // 이미 동일한 걸로 존재하면,
        if (existingSolution != null) {
            log.info("동일 정답 존재");
            // 기존 데이터 업데이트
            return saveSolution(existingSolution);
        }
        else{
            return saveSolution(solution);
        }
    }

    public Solution saveSolution(Solution solution) {return solutionRepository.save(solution);}

    public void saveCodeToFile(String problemId, String filePath, String language, String code) throws IOException {

        // 확장자 결정
        String extension = getFileExtension(language);

        // 파일 경로 생성
        String fileSavePath = BASE_PATH + filePath;

        // 디렉토리 생성
        File directory = new File(BASE_PATH+ "solutions/" + problemId + "/" + extension);
        if (!directory.exists()) {
            directory.mkdirs();
            log.info("새로운 폴더 생성 : {}", directory.getAbsolutePath());
        }
        // 파일에 코드 저장
        try (FileWriter writer = new FileWriter(fileSavePath)) {
            writer.write(code);
        }
    }
    // 현재 요청받은 문제번호와 언어를 기반으로 기존에 크롤링 된 답변들이 100개 이상 존재하는 지 검증
    // 1개라도 있는지 검증 solutionRepository.existsByProblemIdAndLanguage
    // 100개 이상 있는지 검증 solutionRepository.hsaAtLeast100Solutions()
    public boolean hasAtLeast100Solutions(String problemId, String language){
        long count = solutionRepository.countByProblemIdAndLanguage(problemId,language);

        return count >= 100;
    }

    public String getFileExtension(String language) {
        switch(language.toLowerCase()){
            case "java":
                return "java";
            case "python":
                return "py";
            case "c++":
                return "cpp";
            case "c":
                return "c";
            default:
                throw new IllegalArgumentException("Unsupported language: " + language);
        }
    }
}
