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

    @GetMapping("/compare")
    public List<JPlagComparison> compareSolution(@RequestParam String solutionsPath) throws ExitException {
        return similarityService.compareSoltions(solutionsPath);
    }

    @PostMapping("/compare")
    public String compareSolutions(
            @RequestParam String baseFilePath,
            @RequestParam String solutionsPath) throws ExitException {
        try{
            similarityService.compareWithBaseFile(baseFilePath, solutionsPath);
            return "Comparison completed and results saved to database.";
        } catch (ExitException e){
            return "Error during comparison: " + e.getMessage();
        }
    }
}
