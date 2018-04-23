package com.example.meghnapai.workoutapp;

import android.content.Intent;
import android.speech.RecognitionService;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class RecyclerWorkouts extends AppCompatActivity {

    RecyclerView recyclerView;
    RecyclerView.LayoutManager layoutManager;
    RecyclerView.Adapter adapter;
    String passingExercise;

//
    List<Product> productList;
//
//    //the recyclerview
  //  RecyclerView recyclerView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recycler_workouts);
        Bundle extras = getIntent().getExtras();
        passingExercise= extras.getString("PassedEx");

        System.out.println(passingExercise);
        //getting the recyclerview from xml
        recyclerView = (RecyclerView) findViewById(R.id.RecyclerView);
       recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        //initializing the productlist
        productList = new ArrayList<>();


        //adding some items to our list
        productList.add(
                new Product(passingExercise
                ));
        //adapter.notifyDataSetChanged();

        //creating recyclerview adapter
        ProductAdapter adapter = new ProductAdapter(this, productList);

        //setting adapter to recyclerview
        recyclerView.setAdapter(adapter);

        recyclerView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               // Toast.makeText(itemView.getContext(), "Position:" + Integer.toString(getPosition()), Toast.LENGTH_SHORT).show();
            }
        });
    }



}
