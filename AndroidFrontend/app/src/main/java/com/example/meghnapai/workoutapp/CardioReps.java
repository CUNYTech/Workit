package com.example.meghnapai.workoutapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class CardioReps extends AppCompatActivity {

    private ArrayList<WeightsAndRepsHandler> arrayList;// for the listview dynamic adding
    //private ArrayList<int> arrayList2;
    private ArrayAdapter<WeightsAndRepsHandler> adapter;
    // "
    Button IncDist, DecDist, IncTime, DecTime, saveBtn;
    EditText DistanceVal, TimeVal;
    ListView LVsets;


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




                arrayList.add(new WeightsAndRepsHandler(Integer.parseInt(weights),Integer.parseInt(reps), "Distance: ", "Time: "));


                adapter.notifyDataSetChanged();
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



