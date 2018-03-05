package com.apicaller.user;

import com.apicaller.urlcreater.UrlCaller;
import com.google.gson.JsonObject;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

public class Login {
    private String username;
    private String password;

    public Login(String username, String password){
        this.username = username;
        this.password = password;
    }

    public JSONObject login() throws IOException, JSONException {
        String url = "user/login/" + username + '/' + password;
        UrlCaller login = new UrlCaller(url);
        return login.readJsonFromUrl();
    }

    public String getUsername() {
        return username;
    }
}
