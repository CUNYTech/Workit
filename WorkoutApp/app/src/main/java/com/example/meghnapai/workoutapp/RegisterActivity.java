package com.example.meghnapai.workoutapp;

import android.app.Activity;
import android.content.Intent;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class RegisterActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        TextInputLayout LayoutName= (TextInputLayout) findViewById(R.id.LayoutName);
        TextInputLayout LayoutUserame= (TextInputLayout) findViewById(R.id.LayoutUsername);
        TextInputLayout LayoutEmail= (TextInputLayout) findViewById(R.id.LayoutEmail);
        TextInputLayout LayoutPassword= (TextInputLayout) findViewById(R.id.LayoutPassword);


        EditText nameET = (EditText) findViewById(R.id.nameET);
        EditText usernameET = (EditText) findViewById(R.id.usernameET);
        EditText emailET = (EditText) findViewById(R.id.emailET);
        EditText passwordET = (EditText) findViewById(R.id.passwordET);

        Button RegisterBtn = (Button) findViewById(R.id.RegisterBtn);

        RegisterBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent SignUpIntent = new Intent(RegisterActivity.this, UserInfoActivity.class);
                RegisterActivity.this.startActivity(SignUpIntent);
            }


        });

    }
}
