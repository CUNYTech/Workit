package com.example.meghnapai.workoutapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class CalisthenicReps extends AppCompatActivity {

    private ArrayList<WeightsAndRepsHandler> arrayList;// for the listview dynamic adding
    //private ArrayList<int> arrayList2;
    private ArrayAdapter<WeightsAndRepsHandler> adapter;
    // "
    Button IncCalRep, DecCalRep, saveButton;
    EditText CalRep;
    ListView LVsets;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calisthenic_reps);

        IncCalRep = (Button) findViewById(R.id.IncCalRep);
        DecCalRep = (Button) findViewById(R.id.DecCalRep);
        CalRep = (EditText) findViewById(R.id.ETCalRep);

        LVsets= (ListView) findViewById(R.id.LVSets);
        saveButton = (Button) findViewById(R.id.SaveButton);

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


                arrayList.add(new WeightsAndRepsHandler(Integer.parseInt(weights),0, "Reps: ", " "));


                adapter.notifyDataSetChanged();
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



