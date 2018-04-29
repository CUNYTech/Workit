package com.example.meghnapai.workoutapp;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;
import java.util.regex.Pattern;

public class RegisterActivity extends AppCompatActivity {
    private EditText et_firstname, et_lastname, et_username, et_email, et_password;
    private String firstname, lastname, username, email, password;
    Button RegisterBtn;
    // brandons stuff
    private FirebaseAuth mAuth;
    private DatabaseReference mDatabase;
    private ProgressDialog mRegProgress;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        // everything below is brandons
        mAuth = FirebaseAuth.getInstance();
        mRegProgress = new ProgressDialog(this);

        TextInputLayout LayoutFirstName = (TextInputLayout) findViewById(R.id.LayoutFirstName);
        TextInputLayout LayoutLASTName = (TextInputLayout) findViewById(R.id.LayoutLastName);
        TextInputLayout LayoutUserame = (TextInputLayout) findViewById(R.id.LayoutUsername);
        TextInputLayout LayoutEmail = (TextInputLayout) findViewById(R.id.LayoutEmail);
        TextInputLayout LayoutPassword = (TextInputLayout) findViewById(R.id.LayoutPassword);
        
        
        et_firstname = (EditText) findViewById(R.id.firstnameET);
        et_lastname = (EditText) findViewById(R.id.lastnameET);
        et_username = (EditText) findViewById(R.id.usernameET);
        et_email = (EditText) findViewById(R.id.emailET);
        et_password = (EditText) findViewById(R.id.passwordET);
        
        RegisterBtn = (Button) findViewById(R.id.RegisterBtn);
        
        RegisterBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String username = et_username.getText().toString();
                String email = et_email.getText().toString();
                String password = et_password.getText().toString();
                registerUser(username, email, password);
                register();
            }
        });
        
    }
    
    
    public void register() {
        initialize(); // Initialize input to String variable
        if(!validate())
        {
            Toast.makeText(this, "SignUp has failed", Toast.LENGTH_SHORT).show();
        }
        else
            OnSignUPSuccess();
    }
    
    
    public void OnSignUPSuccess()
    {
        // What will happen after valid sign up
        Intent SignUpIntent = new Intent(RegisterActivity.this, UserInfoActivity.class);
        RegisterActivity.this.startActivity(SignUpIntent);
        //passing these variables to the other activity page
        Bundle extras = new Bundle();
        extras.putString("FIRST_NAME",firstname);
        extras.putString("LAST_NAME",lastname);
        extras.putString("USERNAME",username);
        extras.putString("EMAIL",email);
        extras.putString("PASSWORD",password);
        SignUpIntent.putExtras(extras);
        startActivity(SignUpIntent);



    }
    
    public boolean validate()
    {
        boolean valid = true;
        if(firstname.isEmpty() || firstname.length()>32)
        {
            et_firstname.setError("Please Enter valid First Name");
            valid= false;
        }

        if(lastname.isEmpty() || lastname.length()>32)
        {
            et_lastname.setError("Please Enter valid Last Name");
            valid= false;
        }
        if(email.isEmpty() || !Patterns.EMAIL_ADDRESS.matcher(email).matches())
        {
            et_email.setError("Please Enter valid Email Address");
            valid= false;
        }
        
        if(username.isEmpty() || username.length()>32)
        {
            et_username.setError("Please Enter valid Username");
            valid= false;
        }
        
        if(username.length()<4)
        {
            et_username.setError("Username Length must be at least 4 characters");
            valid= false;
        }
        
        if(password.isEmpty())
        {
            et_password.setError("Please Enter valid Password");
            valid= false;
        }
        
        if(password.length()<4)
        {
            et_password.setError("Password Length must be at least 4 characters");
            valid= false;
        }
        
        return valid;
    }
    
    public void initialize()
    {
        firstname=et_firstname.getText().toString().trim();
        lastname=et_lastname.getText().toString().trim();
        username=et_username.getText().toString().trim();
        email=et_email.getText().toString().trim();
        password=et_password.getText().toString().trim();
    }

    private void registerUser(final String displayName, String email, String password) {
        mAuth.createUserWithEmailAndPassword(email, password).addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if(task.isSuccessful()) {
                    FirebaseUser currentUser = FirebaseAuth.getInstance().getCurrentUser();
                    String uid = currentUser.getUid();

                    mDatabase = FirebaseDatabase.getInstance().getReference().child("Users").child(uid);
                    HashMap<String, String> userMap = new HashMap<>();
                    userMap.put("name", displayName);
                    userMap.put("status", "Default Status");

                    mDatabase.setValue(userMap).addOnCompleteListener(new OnCompleteListener<Void>() {
                        @Override
                        public void onComplete(@NonNull Task<Void> task) {
                            if (task.isSuccessful()) {
                                mRegProgress.dismiss();
                                //Intent mainIntent = new Intent(ChatRegisterActivity.this, ChatMainActivity.class);
                                //mainIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                                //startActivity(mainIntent);
                                finish();
                            }
                        }
                    });

                } else {
                    mRegProgress.hide();
                    String test = task.getException().getMessage();
                    Toast.makeText(RegisterActivity.this, test, Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}

