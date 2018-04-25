package com.APICaller.sets;

import com.APICaller.exercise.Exercise;
import com.google.gson.annotations.SerializedName;

/**
 * Created by russ on 4/1/18.
 */

public class CardioSet {
    @SerializedName("username")
    private String username;
    @SerializedName("date")
    private String date;
    @SerializedName("time")
    private String time;
    @SerializedName("workout")
    private String workout;
    @SerializedName("exerciseName")
    private String exerciseName;
    @SerializedName("length")
    private int length;
    @SerializedName("lengthUnit")
    private String lengthUnit;

    public CardioSet(String username, String date, String time, String workout, String exerciseName, int length, String lengthUnit) {
        this.username = username;
        this.date = date;
        this.time = time;
        this.workout = workout;
        this.exerciseName = exerciseName;
        this.length = length;
        this.lengthUnit = lengthUnit;
    }

    public CardioSet(Exercise exercise, int length, String lengthUnit) {
        this.username = exercise.getUsername();
        this.date = exercise.getDate();
        this.time = exercise.getTime();
        this.workout = exercise.getWorkout();

        this.exerciseName = exercise.getExerciseName();
        this.length = length;
        this.lengthUnit = lengthUnit;
    }

    public String getUsername() {
        return username;
    }

    public String getDate() {
        return date;
    }

    public String getTime() {
        return time;
    }

    public String getWorkout() {
        return workout;
    }

    public String getExerciseName() {
        return exerciseName;
    }

    public int getLength() {
        return length;
    }

    public String getLengthUnit() {
        return lengthUnit;
    }
}
