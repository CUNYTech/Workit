package com.APICaller.sets;

import com.APICaller.exercise.Exercise;
import com.google.gson.annotations.SerializedName;

/**
 * Created by russ on 4/1/18.
 */

public class WeightLiftingSet {
    private String username;
    private String date;
    private String time;
    private String workout;
//    private String tag;
    private String exerciseName;
    private int setNum;
    private int weight;
    private int reps;
    @SerializedName("weightUnit")
    private String weightUnits;


    public WeightLiftingSet(String username, String date, String time, String workout, String exerciseName, int setNum, int weight, int reps, String weightUnits) {
        this.username = username;
        this.date = date;
        this.time = time;
        this.workout = workout;
//        this.tag = tag;
        this.exerciseName = exerciseName;
        this.setNum = setNum;
        this.weight = weight;
        this.reps = reps;
        this.weightUnits = weightUnits;
    }

    public WeightLiftingSet(Exercise exercise, int setNum, int weight, int reps, String weightUnits) {
        this.username = exercise.getUsername();
        this.date = exercise.getDate();
        this.time = exercise.getTime();
        this.workout = exercise.getWorkout();
        //this.tag = exercise.getTag();
        this.exerciseName = exercise.getExerciseName();
        this.setNum = setNum;
        this.weight = weight;
        this.reps = reps;
        this.weightUnits = weightUnits;
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

    //public String getTag() {
       // return tag;
    //}

    public String getExerciseName() {
        return exerciseName;
    }

    public int getSetNum() {
        return setNum;
    }

    public int getWeight() {
        return weight;
    }

    public int getReps() {
        return reps;
    }

    public String getWeightUnits() {
        return weightUnits;
    }

    @Override
    public String toString() {
        return "WeightLiftingSet{" +
                "username='" + username + '\'' +
                ", date='" + date + '\'' +
                ", time='" + time + '\'' +
                ", workout='" + workout + '\'' +
                ", exerciseName='" + exerciseName + '\'' +
                ", setNum=" + setNum +
                ", weight=" + weight +
                ", reps=" + reps +
                ", weightUnits='" + weightUnits + '\'' +
                '}';
    }
}
