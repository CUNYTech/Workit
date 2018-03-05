package com.apicaller.schedule;

import com.apicaller.urlcreater.UrlCaller;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

public class Schedule {
    private String username;
    private String date;
    private String time;

    public Schedule(String username, String date, String time) {
        this.username = username;
        this.date = date;
        this.time = time;
    }

    public JSONObject getUsersSchedule() throws IOException, JSONException {
        String url = "/schedule/workout/" + username + '/' + date + '/' + time;
        UrlCaller newCall = new UrlCaller(url);

        return newCall.readJsonFromUrl();
    }
}
