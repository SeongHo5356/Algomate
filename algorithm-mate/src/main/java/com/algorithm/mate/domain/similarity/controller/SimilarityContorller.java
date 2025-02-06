package com.algorithm.mate.domain.similarity.controller;

import com.algorithm.mate.domain.similarity.service.SimilarityService;
import de.jplag.JPlagComparison;
import de.jplag.exceptions.ExitException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/similarity")
public class SimilarityContorller {

    @Autowired
    private SimilarityService similarityService;

    @PostMapping("/compare2")
    public String compareSolutions2(String problemId, String language){

        String baseFilePath = System.getProperty("user.dir") + "/src/main/resources/solutions/" +problemId+ "/base";
        String solutionsPath = System.getProperty("user.dir") + "/src/main/resources/solutions/" + problemId + "/" + language;

        try{
            similarityService.compareWithBaseFile(baseFilePath, solutionsPath);
            return "Comparison completed and results saved to database.";
        } catch (ExitException e){
            return "Error during comparison: " + e.getMessage();
        }
    }

}
