package com.example.meghnapai.workoutapp;

public class WeightsAndRepsHandler {

    private int weights;
    private int reps;
    String label1;
    String label2;
    public WeightsAndRepsHandler(int weights, int reps, String label1, String label2) {
        this.weights = weights;
        this.reps = reps;
        this.label1 = label1;
        this.label2 = label2;
    }

    public int getWeights() {
        return weights;
    }

    public int getReps() {
        return reps;
    }

    @Override
    public String toString() {
        return label1 + weights + "         " +
                label2 + reps;
    }
}

