package com.APICaller.schedule;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

public class ScheduleList {
    @SerializedName("schedules")
    @Expose
    private ArrayList<Schedule> scheduleList = new ArrayList<>();

    public ArrayList<Schedule> getScheduleList() {
        return scheduleList;
    }

    public void setScheduleList(ArrayList<Schedule> scheduleList) {
        this.scheduleList = scheduleList;
    }
}
