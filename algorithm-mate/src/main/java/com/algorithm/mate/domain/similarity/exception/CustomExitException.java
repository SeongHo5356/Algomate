package com.algorithm.mate.domain.similarity.exception;

import de.jplag.exceptions.ExitException;

public class CustomExitException extends ExitException{
    public CustomExitException(String message) {
        super(message);
    }
}
