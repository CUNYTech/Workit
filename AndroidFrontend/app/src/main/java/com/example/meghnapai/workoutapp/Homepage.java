package com.example.meghnapai.workoutapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

public class Homepage extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_homepage);
        Session session = new Session(this);
        Toast.makeText(this,session.getUsername(),Toast.LENGTH_LONG).show();

    }
}
