package com.example.meghnapai.workoutapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class WeightsAndRepsActivity extends AppCompatActivity {

    private ArrayList<WeightsAndRepsHandler> arrayList;// for the listview dynamic adding
    //private ArrayList<int> arrayList2;
    private ArrayAdapter<WeightsAndRepsHandler> adapter;
    // "
    Button IncWeight, DecWeight, IncRep, DecRep, saveBtn;
    EditText WeightsVal, RepsVal;
    ListView LVsets;


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


                arrayList.add(new WeightsAndRepsHandler(Integer.parseInt(weights),Integer.parseInt(reps), "Weights: ", "Reps: "));


                adapter.notifyDataSetChanged();
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



