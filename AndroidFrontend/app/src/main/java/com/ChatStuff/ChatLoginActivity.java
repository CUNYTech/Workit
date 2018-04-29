package com.ChatStuff;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.meghnapai.workoutapp.R;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class ChatLoginActivity extends AppCompatActivity {

    private Toolbar mToolbar;

    private EditText mLoginEmail;
    private EditText mLoginPassword;

    private Button mLogin_btn;

    private ProgressDialog mLogInProgress;

    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat_login);

        mAuth = FirebaseAuth.getInstance();

        mToolbar = (Toolbar) findViewById(R.id.login_toolbar);
        setSupportActionBar(mToolbar);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        getSupportActionBar().setTitle("Login");

        mLogInProgress = new ProgressDialog(this );


        mLoginEmail = (EditText) findViewById(R.id.login_email);
        mLoginPassword = (EditText) findViewById(R.id.login_password);
        mLogin_btn = (Button) findViewById(R.id.login_login_btn);

        mLogin_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email = mLoginEmail.getText().toString();
                String password = mLoginPassword.getText().toString();

                if (!TextUtils.isEmpty(email) || !TextUtils.isEmpty(password)) {
                    mLogInProgress.setTitle("Logging in...");
                    mLogInProgress.setMessage("Please wait.");
                    mLogInProgress.setCanceledOnTouchOutside(false);
                    mLogInProgress.show();
                    loginUser(email, password);
                }
            }
        });
    }

    private void loginUser(String email, final String password) {
        mAuth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            // Sign in success, update UI with the signed-in user's information
                            mLogInProgress.dismiss();
                            Intent mainIntent = new Intent(ChatLoginActivity.this, ChatMainActivity.class);
                            mainIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                            startActivity(mainIntent);
                            FirebaseUser user = mAuth.getCurrentUser();
                        } else {
                            // If sign in fails, display a message to the user.
                            mLogInProgress.hide();
                            //String test = task.getException().getMessage();
                            Toast.makeText(ChatLoginActivity.this, "Login Failed.", Toast.LENGTH_SHORT).show();
                        }
                    }
                });
    }
}
