package com.APICaller.sets;

import com.APICaller.exercise.Exercise;
import com.google.gson.annotations.SerializedName;

/**
 * Created by russ on 4/1/18.
 */

public class CalisthenicSet {
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
    @SerializedName("tag")
    private String tag;
    @SerializedName("setNum")
    private int setNum;
    @SerializedName("reps")
    private int reps;

    public CalisthenicSet(String username, String date, String time, String workout, String tag, int setNum, int reps) {
        this.username = username;
        this.date = date;
        this.time = time;
        this.workout = workout;
        this.tag = tag;
        this.setNum = setNum;
        this.reps = reps;
    }

    public CalisthenicSet(Exercise exercise, int setNum, int reps) {
        this.username = exercise.getUsername();
        this.date = exercise.getDate();
        this.time = exercise.getTime();
        this.workout = exercise.getWorkout();
        this.tag = exercise.getTag();
        this.setNum = setNum;
        this.reps = reps;
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

    public String getTag() {
        return tag;
    }

    public int getSetNum() {
        return setNum;
    }

    public int getReps() {
        return reps;
    }
}
