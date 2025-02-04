package com.algorithm.mate.domain.dbTEST.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/test")
public class DbTest {
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @GetMapping
    public String testConnection() {
        String result = jdbcTemplate.queryForObject("SELECT version()", String.class);
        return "Connected to: " + result;
    }
}
