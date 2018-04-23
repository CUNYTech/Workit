package com.example.meghnapai.workoutapp;

public class WeightsAndRepsHandler {
    private int set;
    private int weights;
    private int reps;
    String label1;
    String label2;

    public WeightsAndRepsHandler(int weights, int reps, String label1, String label2, int set) {
        this.weights = weights;
        this.reps = reps;
        this.label1 = label1;
        this.label2 = label2;
        this.set = set;
    }

    public int getWeights() {
        return weights;
    }

    public int getReps() {
        return reps;
    }

    public int getSet() {
        return set;
    }

    @Override
    public String toString() {
        if(weights > 0)
            return set +"."+ "       "+ label1 + weights + "         " +
                    label2 + reps;

        return set +"."+ "       "+
                label2 + reps;
    }
}

