package com.APICaller.sets;

import com.google.gson.annotations.SerializedName;

/**
 * Created by russ on 4/23/18.
 */

public class GetSet {
    @SerializedName("setNumber")
    private int setNumber;

    @SerializedName("reps")
    private int reps;

    @SerializedName("weight")
    private int weight;

    @SerializedName("weightUnit")
    private String weightUnit;

    @SerializedName("length")
    private int length;

    @SerializedName("lengthUnit")
    private String lengthUnit;

    // weight lifting
    public GetSet(int setNumber, int reps, int weight, String weightUnit) {
        this.setNumber = setNumber;
        this.reps = reps;
        this.weight = weight;
        this.weightUnit = weightUnit;
    }

    // calisthentic
    public GetSet(int setNumber, int reps) {
        this.setNumber = setNumber;
        this.reps = reps;
    }

    //cardio
    public GetSet(int length, String lengthUnit) {
        this.length = length;
        this.lengthUnit = lengthUnit;
    }

    public int getSetNumber() {
        return setNumber;
    }

    public int getReps() {
        return reps;
    }

    public int getWeight() {
        return weight;
    }

    public String getWeightUnit() {
        return weightUnit;
    }

    public int getLength() {
        return length;
    }

    public String getLengthUnit() {
        return lengthUnit;
    }

    @Override
    public String toString() {
        if(weightUnit != null){
            return setNumber + "." + "       " + "reps: " +   reps + "       " + "weight: " + weight;
        }

        if(weightUnit == null && lengthUnit == null){
            return setNumber + "." + "       " + "reps: " +   reps;
        }

        if(lengthUnit != null){
            return length + " " +lengthUnit;

        }

        return null;
    }
}
