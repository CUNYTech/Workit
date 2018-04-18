package com.example.meghnapai.workoutapp;

public class WeightsAndRepsHandler {

    private int weights;
    private int reps;

    public WeightsAndRepsHandler(int weights, int reps) {
        this.weights = weights;
        this.reps = reps;
    }

    public int getWeights() {
        return weights;
    }

    public int getReps() {
        return reps;
    }

    @Override
    public String toString() {
        return "Weights: " + weights +
                "              reps: " + reps;
    }
}

