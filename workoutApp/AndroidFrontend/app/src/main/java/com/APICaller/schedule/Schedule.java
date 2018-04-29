package com.APICaller.schedule;


import com.google.gson.annotations.SerializedName;

//date format day-month-year
//time format hour:min am/pm
public class Schedule {
    @SerializedName("username")
    private String userName;
    @SerializedName("date")
    private String date;
    @SerializedName("time")
    private String time;
    @SerializedName("workout")
    private String workoutName;


    public Schedule(String userName, String date, String time, String workoutName) {
        this.userName = userName;
        this.date = date;
        this.time = time;
        this.workoutName = workoutName;
    }

    public String getUserName() {
        return userName;
    }

    public String getDate() {
        return date;
    }

    public String getTime() {
        return time;
    }

    public String getWorkoutName() {
        return workoutName;
    }
}
