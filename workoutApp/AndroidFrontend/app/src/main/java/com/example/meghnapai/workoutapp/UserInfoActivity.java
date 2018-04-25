package com.example.meghnapai.workoutapp;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;


import com.APICaller.User.User;
import com.APICaller.base.WorkoutAPI;
import com.google.gson.Gson;

import org.json.JSONException;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class UserInfoActivity extends AppCompatActivity {
    private EditText ageET, weightET, heightET;
    String age, weight, height, gender;
    int AGE;
    float WEIGHT, HEIGHT;
    Button SignUpBtn;
    String weightUnit= "lb";
    String heightUnit="in";
    RadioButton genderRB;
    RadioGroup GenderRG;
    String firstname, lastname, username, email, password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_info);


        ageET= (EditText) findViewById(R.id.ageET);
        weightET= (EditText) findViewById(R.id.weightET);
        heightET= (EditText) findViewById(R.id.inchesET);
        SignUpBtn = (Button) findViewById(R.id.SignUpBtn);
        GenderRG = (RadioGroup) findViewById(R.id.GenderRadioGroup);


        SignUpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                UserInfoValidation();
            }
        });

        // retiriving these values from the register activity class so we can plug it into the constructor for the UserCreater
        Bundle extras = getIntent().getExtras();
        firstname = extras.getString("FIRST_NAME");
        lastname = extras.getString("LAST_NAME");
        username = extras.getString("USERNAME");
        email = extras.getString("EMAIL");
        password = extras.getString("PASSWORD");

    }

    public void RBClick(View v)
    {
        int RBId = GenderRG.getCheckedRadioButtonId();
        genderRB= (RadioButton) findViewById(RBId);
        gender= genderRB.getText().toString();
    }


    public void UserInfoValidation()
    {
        initialize1(); // Initialize input to String variable
        if(!validate1())
        {
            Toast.makeText(this, "Please check your answers", Toast.LENGTH_SHORT).show();
        }
        else
            SuccessfulValidation();
    }

    public void SuccessfulValidation(){
        OkHttpClient httpClient = new OkHttpClient();
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        Retrofit retrofit = builder.build();
        WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

        User newUser = new User(username,password,email, firstname, lastname, gender, WEIGHT, weightUnit, HEIGHT,heightUnit);
        Gson gson = new Gson();
        //System.out.println(gender);
        Call<ResponseBody> call = requests.createNewUser(newUser);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if(response.code() == 201) {
                    Intent CalendarIntent = new Intent(UserInfoActivity.this, MainActivity.class);
                    UserInfoActivity.this.startActivity(CalendarIntent);
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.printf("Throws: " + t);
            }
        });




    }
    public boolean validate1()
    {
        boolean valid = true;


        if(age.isEmpty() || AGE<13 || AGE>100)
        {
            ageET.setError("Please Enter valid Age");
            valid= false;
        }


        if(weight.isEmpty())
        {
            weightET.setError("Please Enter valid Weight");
            valid= false;
        }

        if(height.isEmpty())
        {
            heightET.setError("Please Enter valid Height");
            valid= false;
        }

        return valid;
    }


    public void initialize1()
    {
        age=ageET.getText().toString();
        weight=weightET.getText().toString();
        height=heightET.getText().toString();

        if(!age.isEmpty())
        {
            AGE= Integer.parseInt(age);
        }

        if(!weight.isEmpty())
        {
            WEIGHT= Float.parseFloat(weight);
        }

        if(!height.isEmpty())
        {
            HEIGHT= Float.parseFloat(height);
        }


    }
}


