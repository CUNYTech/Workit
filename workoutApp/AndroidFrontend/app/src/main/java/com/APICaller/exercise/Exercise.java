package com.APICaller.exercise;

import com.APICaller.schedule.Schedule;
import com.google.gson.annotations.SerializedName;

/**
 * Created by russ on 4/1/18.
 */

public class Exercise {
    @SerializedName("username")
    private String username;
    @SerializedName("date")
    private String date;
    @SerializedName("bodyPart")
    private String[] bodyPart = new String[5];
    @SerializedName("time")
    private String time;
    @SerializedName("workout")
    private String workout;
    @SerializedName("exerciseName")
    private String exerciseName;
    @SerializedName("tag")
    private String tag;

    public Exercise(String username, String date, String[] bodyPart, String time, String workout, String exerciseName, String tag) {
        this.username = username;
        this.date = date;
        for(int i = 0; i < bodyPart.length; i++){
            this.bodyPart[i] = bodyPart[i];
        }

        this.time = time;
        this.workout = workout;
        this.exerciseName = exerciseName;
        this.tag = tag;
    }

    public Exercise(Schedule schedule, String exerciseName, String tag, String[] bodyPart) {
        this.username = schedule.getUserName();
        this.date = schedule.getDate();
        for(int i = 0; i < bodyPart.length; i++){
            this.bodyPart[i] = bodyPart[i];
        }
        this.time = schedule.getTime();
        this.workout =schedule.getWorkoutName();
        this.exerciseName = exerciseName;
        this.tag = tag;

    }

    public Exercise(String username, String date, String time, String workout, String exerciseName, String tag) {
        this.username = username;
        this.date = date;
        this.time = time;
        this.workout = workout;
        this.exerciseName = exerciseName;
        this.tag = tag;
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
}
