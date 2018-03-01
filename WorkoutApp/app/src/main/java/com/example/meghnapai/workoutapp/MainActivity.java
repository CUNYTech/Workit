package com.example.meghnapai.workoutapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        final TextView WelcomTextView= (TextView) findViewById(R.id.WelcomeTextView);
        final TextView IntroductionTextView= (TextView) findViewById(R.id.IntroductionTextView);
        final EditText usernameTextEdit= (EditText) findViewById(R.id.usernameTextEdit);
        final EditText passwordTextEdit= (EditText) findViewById(R.id.passwordTextEdit);

        final Button infoBtn = (Button) findViewById(R.id.infoBtn);
        final Button SignUpBtn = (Button) findViewById(R.id.SignUpBtn);
        final Button LogInBtn = (Button) findViewById(R.id.LogInBtn);

        String user = usernameTextEdit.getText().toString();    // FOR SESSION STUFF
        String pass = passwordTextEdit.getText().toString();    // FOR SESSION STUFF




        SignUpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent SignInIntent = new Intent(MainActivity.this,RegisterActivity.class);
                MainActivity.this.startActivity(SignInIntent);
            }


        }


        );


    }
}
