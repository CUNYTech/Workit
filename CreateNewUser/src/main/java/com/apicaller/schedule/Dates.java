package com.apicaller.schedule;

import com.apicaller.urlcreater.UrlCaller;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

public class Dates {
    private String username;
    private String date;
    private String time;
    private String workoutName;

    public Dates(String username, String date, String time, String workoutName) {
        this.username = username;
        this.date = date;
        this.time = time;
        this.workoutName = workoutName;
    }

    public JSONObject callUrl() throws IOException, JSONException {
        String url = "/new/workout/" + username + '/' + date + '/' + time + '/' + workoutName;
        UrlCaller newCall = new UrlCaller(url);

        return newCall.readJsonFromUrl();
    }


}
