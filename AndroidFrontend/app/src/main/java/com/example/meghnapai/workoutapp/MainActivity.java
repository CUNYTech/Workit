package com.example.meghnapai.workoutapp;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


import com.APICaller.base.WorkoutAPI;
import com.ChatStuff.ChatMainActivity;

import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;



public class MainActivity extends AppCompatActivity {

    // brandons stuff
    private ProgressDialog mLogInProgress;
    private FirebaseAuth mAuth;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Session session = new Session(this);

        // brandons stuff
        mAuth = FirebaseAuth.getInstance();
        mLogInProgress = new ProgressDialog(this );

        final TextView WelcomTextView= (TextView) findViewById(R.id.WelcomeTextView);
        final TextView IntroductionTextView= (TextView) findViewById(R.id.IntroductionTextView);
        final  EditText usernameTextEdit= (EditText) findViewById(R.id.usernameTextEdit);
        final EditText passwordTextEdit= (EditText) findViewById(R.id.passwordTextEdit);

        final Button infoBtn = (Button) findViewById(R.id.infoBtn);
        final Button SignUpBtn = (Button) findViewById(R.id.SignUpBtn);
        final Button LogInBtn = (Button) findViewById(R.id.LogInBtn);

        if(session.getUsername() != null){
            Intent homePage = new Intent(MainActivity.this, Homepage.class);
            MainActivity.this.startActivity(homePage);
        }


        SignUpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent SignInIntent = new Intent(MainActivity.this, RegisterActivity.class);
                MainActivity.this.startActivity(SignInIntent);
            }}
        );

        infoBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Intent SignInIntent = new Intent(MainActivity.this, ListViewActivity1.class);
                Intent SignInIntent = new Intent(MainActivity.this, ChatMainActivity.class);
                MainActivity.this.startActivity(SignInIntent);
            }}
        );

        LogInBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               final Session loginInfo=new Session(MainActivity.this);
                final  EditText usernameTextEdit= (EditText) findViewById(R.id.usernameTextEdit);
                final EditText passwordTextEdit= (EditText) findViewById(R.id.passwordTextEdit);

                final String user= usernameTextEdit.getText().toString();
                final String pass=passwordTextEdit.getText().toString();

                // loginUser(user, pass);
                // AN EMAIL EDIT TEXT NEEDS TO BE ADDED. FIREBASE NEEDS EMAIL + PASSWORD TO LOGIN ONLY.

                OkHttpClient httpClient = new OkHttpClient();
                Retrofit.Builder builder = new Retrofit.Builder()
                        .baseUrl(WorkoutAPI.BASE_URL)
                        .addConverterFactory(GsonConverterFactory.create())
                        .client(httpClient);

                Retrofit retrofit = builder.build();
                WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

                Call<ResponseBody> call = requests.login(user,pass);
                call.enqueue(new Callback<ResponseBody>() {
                                 @Override
                                 public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {

                                     if(response.code() == 202){
                                         loginInfo.setPassword(pass);
                                         loginInfo.setUsername(user);
                                         Intent homepage = new Intent(MainActivity.this, Homepage.class);
                                         MainActivity.this.startActivity(homepage);
                                     }else{
                                         throwInavlidLogin();
                                     }
                                 }

                                 @Override
                                 public void onFailure(Call<ResponseBody> call, Throwable t) {
                                     System.out.println("Throws: " + t);
                                 }

            });




            }

        });
    }
    public void throwInavlidLogin(){
        Toast.makeText(this, "Invalid Login", Toast.LENGTH_SHORT).show();
    }

    private void loginUser(String email, final String password) {
        mAuth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            // Sign in success, update UI with the signed-in user's information
                            mLogInProgress.dismiss();
                            //Intent mainIntent = new Intent(ChatLoginActivity.this, ChatMainActivity.class);
                            //mainIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                            //startActivity(mainIntent);
                            FirebaseUser user = mAuth.getCurrentUser();
                        } else {
                            // If sign in fails, display a message to the user.
                            mLogInProgress.hide();
                            //String test = task.getException().getMessage();
                            Toast.makeText(MainActivity.this, "Login Failed.", Toast.LENGTH_SHORT).show();
                        }
                    }
                });
    }
}






