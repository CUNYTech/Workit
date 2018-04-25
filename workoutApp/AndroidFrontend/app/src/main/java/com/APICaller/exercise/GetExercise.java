package com.APICaller.exercise;

/**
 * Created by russ on 4/9/18.
 */

public class GetExercise {
    private String name;
    private String type;

    public GetExercise(String name, String type) {
        this.name = name;
        this.type = type;
    }



    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    @Override
    public String toString() {
        return name;
    }
}
