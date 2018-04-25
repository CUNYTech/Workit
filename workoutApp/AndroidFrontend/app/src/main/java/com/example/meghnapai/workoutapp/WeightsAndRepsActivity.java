package com.example.meghnapai.workoutapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.APICaller.base.WorkoutAPI;
import com.APICaller.exercise.Exercise;
import com.APICaller.sets.WeightLiftingSet;

import java.util.ArrayList;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class WeightsAndRepsActivity extends AppCompatActivity {

    private ArrayList<WeightsAndRepsHandler> arrayList;// for the listview dynamic adding
    //private ArrayList<int> arrayList2;
    private ArrayAdapter<WeightsAndRepsHandler> adapter;
    // "
    Button IncWeight, DecWeight, IncRep, DecRep, saveBtn, donebtn;
    EditText WeightsVal, RepsVal;
    ListView LVsets;
    String passingExercise;

    int counter = 1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_weights_and_reps);

        IncWeight = (Button) findViewById(R.id.IncWeights);
        DecWeight = (Button) findViewById(R.id.DecWeights);
        WeightsVal = (EditText) findViewById(R.id.ETWeights);
        RepsVal = (EditText) findViewById(R.id.ETReps);
        IncRep = (Button) findViewById(R.id.IncReps);
        DecRep = (Button) findViewById(R.id.DecReps);
        LVsets= (ListView) findViewById(R.id.LVSets);
        saveBtn = (Button) findViewById(R.id.SaveBtn);
        donebtn =(Button) findViewById(R.id.DoneBtn);
        arrayList=new ArrayList<WeightsAndRepsHandler>();
        adapter = new ArrayAdapter<WeightsAndRepsHandler>(this, R.layout.custom_listview_ex, R.id.textView, arrayList);
        LVsets.setAdapter(adapter);





        String [] weights= {};
        String [] reps= {};




        //for hiding the curosr and making it visible.. not working too well right now --NEED TO FIX
        WeightsVal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                WeightsVal.setCursorVisible(true);
            }
        });


        RepsVal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                RepsVal.setCursorVisible(true);
            }
        });

        IncWeight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //  Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    WeightsVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(WeightsVal.getText().toString());
                    WeightsVal.setText(String.valueOf(t + 1));
                    WeightsVal.setCursorVisible(false);
                }
            }
        });

        DecWeight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    WeightsVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(WeightsVal.getText().toString());
                    if (t > 0) {
                        WeightsVal.setText(String.valueOf(t - 1));
                        WeightsVal.setCursorVisible(false);
                    }
                }
            }
        });



        IncRep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    // Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    RepsVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(RepsVal.getText().toString());
                    RepsVal.setText(String.valueOf(t + 1));
                    RepsVal.setCursorVisible(false);
                }
            }
        });

        DecRep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    RepsVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(RepsVal.getText().toString());
                    if (t > 0) {
                        RepsVal.setText(String.valueOf(t - 1));
                        RepsVal.setCursorVisible(false);
                    }
                }
            }
        });

        saveBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String reps = RepsVal.getText().toString();
                String weights = WeightsVal.getText().toString();


                arrayList.add(new WeightsAndRepsHandler(Integer.parseInt(weights),Integer.parseInt(reps), "Weights: ", "Reps: ", counter));
                counter++;

                adapter.notifyDataSetChanged();
            }
        });

        donebtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Bundle extras = getIntent().getExtras();
                Session session = new Session(WeightsAndRepsActivity.this);
                Toast.makeText(WeightsAndRepsActivity.this, "Done", Toast.LENGTH_LONG).show();
                ArrayList<WeightLiftingSet> exercises = new ArrayList<>();

                passingExercise= extras.getString("Category");
                for(WeightsAndRepsHandler handler : arrayList){

                    WeightLiftingSet exercise = new WeightLiftingSet(session.getUsername(),session.getDate(),session.getTime(),
                            session.getWorkout(),passingExercise,handler.getSet(),handler.getWeights(),handler.getReps(),"lb" );
                    System.out.println(exercise + "\n");



                    exercises.add(exercise);
                }

                OkHttpClient httpClient = new OkHttpClient();
                Retrofit.Builder builder = new Retrofit.Builder()
                        .baseUrl(WorkoutAPI.BASE_URL)
                        .addConverterFactory(GsonConverterFactory.create())
                        .client(httpClient);

                Retrofit retrofit = builder.build();
                WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

                Call<ResponseBody> call = requests.newWeightLifingSetPost(exercises);

                call.enqueue(new Callback<ResponseBody>() {
                    @Override
                    public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                        if(response.code() == 201){
                            Intent done= new Intent(WeightsAndRepsActivity.this, RecyclerWorkouts.class);
                            startActivity(done);
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

    public boolean validate()
    {
        boolean valid = true;
        if (WeightsVal.getText().toString().isEmpty())
        {
            valid = false;
        }
        if (RepsVal.getText().toString().isEmpty())
        {
            valid = false;
        }
        return valid;
    }





}



