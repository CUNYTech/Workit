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
import com.APICaller.sets.CardioSet;
import com.APICaller.sets.WeightLiftingSet;

import java.util.ArrayList;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class CardioReps extends AppCompatActivity {

    private ArrayList<WeightsAndRepsHandler> arrayList;// for the listview dynamic adding
    //private ArrayList<int> arrayList2;
    private ArrayAdapter<WeightsAndRepsHandler> adapter;
    // "
    Button IncDist, DecDist, IncTime, DecTime, saveBtn, doneBtn;
    EditText DistanceVal, TimeVal;
    ListView LVsets;
    int counter = 1;
    String passingExercise;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cardio_reps);

        IncDist = (Button) findViewById(R.id.IncDist);
        DecDist = (Button) findViewById(R.id.DecDist);
        DistanceVal = (EditText) findViewById(R.id.ETDistance);
        TimeVal = (EditText) findViewById(R.id.ETTime);
        IncTime = (Button) findViewById(R.id.IncTime);
        DecTime = (Button) findViewById(R.id.DecTime);
        LVsets= (ListView) findViewById(R.id.LVSets);
        saveBtn = (Button) findViewById(R.id.SaveButtn);
        doneBtn= (Button) findViewById(R.id.DoneButtn);

        arrayList=new ArrayList<WeightsAndRepsHandler>();
        adapter = new ArrayAdapter<WeightsAndRepsHandler>(this, R.layout.custom_listview_ex, R.id.textView, arrayList);
        LVsets.setAdapter(adapter);

        String [] weights= {};
        String [] reps= {};




        //for hiding the curosr and making it visible.. not working too well right now --NEED TO FIX
        DistanceVal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                DistanceVal.setCursorVisible(true);
            }
        });


        TimeVal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TimeVal.setCursorVisible(true);
            }
        });

        IncDist.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //  Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    DistanceVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(DistanceVal.getText().toString());
                    DistanceVal.setText(String.valueOf(t + 1));
                    DistanceVal.setCursorVisible(false);
                }
            }
        });

        DecDist.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    DistanceVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(DistanceVal.getText().toString());
                    if (t > 0) {
                        DistanceVal.setText(String.valueOf(t - 1));
                        DistanceVal.setCursorVisible(false);
                    }
                }
            }
        });



        IncTime.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    // Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    TimeVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(TimeVal.getText().toString());
                    TimeVal.setText(String.valueOf(t + 1));
                    TimeVal.setCursorVisible(false);
                }
            }
        });

        DecTime.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    TimeVal.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(TimeVal.getText().toString());
                    if (t > 0) {
                        TimeVal.setText(String.valueOf(t - 1));
                        TimeVal.setCursorVisible(false);
                    }
                }
            }
        });

        saveBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String reps = TimeVal.getText().toString();
                String weights = DistanceVal.getText().toString();




                arrayList.add(new WeightsAndRepsHandler(Integer.parseInt(weights),Integer.parseInt(reps), "Distance: ", "Time: ",counter));
                counter++;


                adapter.notifyDataSetChanged();
            }
        });

        doneBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Bundle extras = getIntent().getExtras();
                Session session = new Session(CardioReps.this);
                Toast.makeText(CardioReps.this, "Done", Toast.LENGTH_LONG).show();
                ArrayList<CardioSet> exercises = new ArrayList<>();

                passingExercise= extras.getString("Category");
                for(WeightsAndRepsHandler handler : arrayList){

                    CardioSet exercise = new CardioSet(session.getUsername(),session.getDate(),session.getTime(),
                            session.getWorkout(),passingExercise,handler.getWeights(),"miles" );
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

                Call<ResponseBody> call = requests.newCardioSetPost(exercises);

                call.enqueue(new Callback<ResponseBody>() {
                    @Override
                    public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                        if(response.code() == 201){
                            Intent done= new Intent(CardioReps.this, RecyclerWorkouts.class);
                            Bundle bundle = new Bundle();
                            bundle.putString("PassedEx", passingExercise);
                            done.putExtras(bundle);
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
        if (DistanceVal.getText().toString().isEmpty())
        {
            valid = false;
        }
        if (TimeVal.getText().toString().isEmpty())
        {
            valid = false;
        }
        return valid;
    }





}



