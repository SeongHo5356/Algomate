package com.algorithm.mate.domain.similarity.entity;

public enum Language {
    JAVA("java"),
    PYTHON_3("python3"),
    C_CPP("cpp"),
    C_SHARP("csharp"),
    CHAR("char"),
    TEXT("text"),
    SCHEME("scheme");

    private final String name;

    Language(String name){
        this.name = name;
    }

    public String getName(){
        return name;
    }
}
