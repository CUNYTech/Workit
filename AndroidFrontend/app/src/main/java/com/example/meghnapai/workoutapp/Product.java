package com.example.meghnapai.workoutapp;

public class Product {
    private String ExerciseName;
    private String Label1;
    private String Label2;
    private int val1;
    private int val2;

    public Product(String ExerciseName) //int val1, int val2)
    {
        this.ExerciseName = ExerciseName;

    }

    public String getExerciseName() {
        return ExerciseName;
    }


    public void setExerciseName(String exerciseName) {
        ExerciseName = exerciseName;
    }
}



