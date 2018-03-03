package com.example.meghnapai.workoutapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class UserInfoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_info);

        final Button SignUpBtn = (Button) findViewById(R.id.SignUpBtn);


        SignUpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent CalendarIntent = new Intent(UserInfoActivity.this, CalendarActivity.class);
                UserInfoActivity.this.startActivity(CalendarIntent);
            }
        }
        );

    }
}

