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
import com.APICaller.sets.CalisthenicSet;
import com.APICaller.sets.CardioSet;

import java.util.ArrayList;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class CalisthenicReps extends AppCompatActivity {

    private ArrayList<WeightsAndRepsHandler> arrayList;// for the listview dynamic adding
    //private ArrayList<int> arrayList2;
    private ArrayAdapter<WeightsAndRepsHandler> adapter;
    // "
    Button IncCalRep, DecCalRep, saveButton, doneButton;
    EditText CalRep;
    ListView LVsets;
    int counter= 1;
    String passingExercise;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calisthenic_reps);

        IncCalRep = (Button) findViewById(R.id.IncCalRep);
        DecCalRep = (Button) findViewById(R.id.DecCalRep);
        CalRep = (EditText) findViewById(R.id.ETCalRep);

        LVsets= (ListView) findViewById(R.id.LVSets);
        saveButton = (Button) findViewById(R.id.SaveButton);
        doneButton = (Button) findViewById(R.id.DoneButton);

        arrayList=new ArrayList<WeightsAndRepsHandler>();
        adapter = new ArrayAdapter<WeightsAndRepsHandler>(this, R.layout.custom_listview_ex, R.id.textView, arrayList);
        LVsets.setAdapter(adapter);

        String [] weights= {};
        String [] reps= {};




        //for hiding the curosr and making it visible.. not working too well right now --NEED TO FIX
        CalRep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                CalRep.setCursorVisible(true);
            }
        });

        IncCalRep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //  Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    CalRep.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(CalRep.getText().toString());
                    CalRep.setText(String.valueOf(t + 1));
                    CalRep.setCursorVisible(false);
                }
            }
        });

        DecCalRep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!validate()){
                    //Toast.makeText(WeightsAndRepsActivity.this, "Please check your values", Toast.LENGTH_SHORT).show();
                    CalRep.setText(Integer.toString(0));
                }
                else {
                    int t = Integer.parseInt(CalRep.getText().toString());
                    if (t > 0) {
                        CalRep.setText(String.valueOf(t - 1));
                        CalRep.setCursorVisible(false);
                    }
                }
            }
        });

        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String weights = CalRep.getText().toString();


                arrayList.add(new WeightsAndRepsHandler(0,Integer.parseInt(weights), " ", "Reps: ", counter));
                counter++;

                adapter.notifyDataSetChanged();
            }
        });

        doneButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Bundle extras = getIntent().getExtras();
                Session session = new Session(CalisthenicReps.this);
                Toast.makeText(CalisthenicReps.this, "Done", Toast.LENGTH_LONG).show();
                ArrayList<CalisthenicSet> exercises = new ArrayList<>();

                passingExercise= extras.getString("Category");
                for(WeightsAndRepsHandler handler : arrayList){

                    CalisthenicSet exercise = new CalisthenicSet(session.getUsername(),session.getDate(),session.getTime(),
                            session.getWorkout(),passingExercise,handler.getReps(), handler.getSet());
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

                Call<ResponseBody> call = requests.newCalisthenicSetPost(exercises);

                call.enqueue(new Callback<ResponseBody>() {
                    @Override
                    public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                        if(response.code() == 201){
                            Intent done= new Intent(CalisthenicReps.this, RecyclerWorkouts.class);
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
        if (CalRep.getText().toString().isEmpty())
        {
            valid = false;
        }
        return valid;
    }





}



