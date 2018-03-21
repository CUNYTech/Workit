package com.APICaller.User;

import com.google.gson.annotations.SerializedName;

public class User {
    @SerializedName("username")
    private String username;
    @SerializedName("password")
    private String password;
    @SerializedName("email")
    private String email;
    @SerializedName("fname")
    private String firstName;
    @SerializedName("lname")
    private String lastName;
    @SerializedName("gender")
    private String gender;
    @SerializedName("weight")
    private float weight;
    @SerializedName("weightUnit")
    private String weightUnit;
    @SerializedName("height")
    private float height;
    @SerializedName("heightUnit")
    private String heightUnit;
    @SerializedName("bmi")
    private int bmi;


    private int bmiCalc(float weight, String weightUnit, float height, String heightUnit){
        if (weightUnit == "kg" && heightUnit == "cm"){
            return (int)Math.floor(weight/((height*100)*(height*100)));
        }else if (weightUnit == "lb" && heightUnit == "ft"){
            return (int)Math.floor(weight/(((height*12)*(height*12))*703));
        }

        return -1;

    }

    public User(String username, String password, String email, String firstName, String lastName, String gender, float weight, String weightUnit, float height, String heightUnit) {
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
        this.bmi = bmiCalc(weight,weightUnit,height,heightUnit);
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public String getEmail() {
        return email;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getGender() {
        return gender;
    }

    public float getWeight() {
        return weight;
    }

    public String getWeightUnit() {
        return weightUnit;
    }

    public float getHeight() {
        return height;
    }

    public String getHeightUnit() {
        return heightUnit;
    }

    public int getBmi() {
        return bmi;
    }

//    public JsonObject createJson(){
//        Gson gson = new Gson();
//        String stringJson = gson.toJson(this);
//        JsonObject json = new JsonObject();
//        json.
//    }
}
