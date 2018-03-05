package com.apicaller.user;

import com.apicaller.urlcreater.UrlCaller;
import com.google.gson.JsonObject;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

public class UserCreater {
    private String username;
    private String password;
    private String email;
    private String firstName;
    private String lastName;
    private String gender;
    private float weight;
    private String weightUnit;
    private float height;
    private String heightUnit;
    private int bmi;

    private int bmiCalc(float weight, String weightUnit, float height, String heightUnit){
        if (weightUnit == "kg" && heightUnit == "cm"){
            return (int)Math.floor(weight/((height*100)*(height*100)));
        }else if (weightUnit == "lb" && heightUnit == "ft"){
            return (int)Math.floor(weight/(((height*12)*(height*12))*703));
        }

        return -1;

    }

    public UserCreater(String username, String password, String email, String firstName, String lastName, String gender, float weight, String weightUnit, float height, String heightUnit, int bmi) {
        this.username = username;
        this.password = password;
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
        this.weight = weight;
        this.weightUnit = weightUnit;
        this.height = height;
        this.heightUnit = heightUnit;
        this.bmi = bmiCalc(weight, weightUnit, height, heightUnit);
    }

    public JSONObject callUrl() throws IOException, JSONException {
        String url = "user/new/" + username + '/' + email + '/' + password + '/' + firstName + '/' + lastName + '/' + gender + '/' +  String.valueOf(height) + '/' + heightUnit + '/' + String.valueOf(weight) + '/' + weightUnit + '/' + String.valueOf(bmi);

        UrlCaller newUser = new UrlCaller(url);
        return newUser.readJsonFromUrl();
    }

    public String getUsername() {
        return username;
    }
}
