package com.example.meghnapai.workoutapp;

import android.content.SharedPreferences;
import android.content.Context;

public class Session {
    private static final String Username = "username";
    private static final String Password = "password";
    private static final String PREFERENCES_NAME = "WorkoutApp";
    SharedPreferences prefs;
    SharedPreferences.Editor editor;

    public Session(Context context) {
        // TODO Auto-generated constructor stub
        prefs = context.getSharedPreferences(PREFERENCES_NAME,
                Context.MODE_PRIVATE);
        editor = prefs.edit();
    }

    public void setUsername(String username) {
        editor.putString(Username, username);
        editor.commit();
    }

    public String getUsername() {
        String username = prefs.getString(Username, "");
        return username;
    }

    public void setPassword(String password) {
        editor.putString(Password, password);
        editor.commit();
    }

    public String getPassword() {
        String password = prefs.getString(Password, "");
        return password;
    }
}