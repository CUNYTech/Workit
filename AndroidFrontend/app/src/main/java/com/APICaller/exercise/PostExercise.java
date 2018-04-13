package com.APICaller.exercise;

/**
 * Created by russ on 4/11/18.
 */

public class PostExercise {
    private String exerciseName;
    private String tag;
    private String[] bodyPart;

    public PostExercise(String name, String[] bodyPart, String tag) {
        this.tag =tag;
        this.exerciseName = name;
        this.bodyPart = bodyPart;
    }

    public String getExerciseName() {
        return exerciseName;
    }

    public void setexerciseName(String name) {
        this.exerciseName = name;
    }

    public String[] getBodyPart() {
        return bodyPart;
    }

    public void setBodyPart(String[] bodyPart) {
        this.bodyPart = bodyPart;
    }
}
