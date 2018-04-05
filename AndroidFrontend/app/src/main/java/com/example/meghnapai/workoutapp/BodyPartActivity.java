package com.example.meghnapai.workoutapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

public class BodyPartActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    ProductAdapter adapter;

    List<Product> productList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_body_part);

        productList=new ArrayList<>();
        recyclerView= (RecyclerView) findViewById(R.id.recyclerView);
        recyclerView.setHasFixedSize(true);

        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        productList.add(
                new Product(
                        1,
                        "BACK",
                        R.drawable.image1));

        productList.add(
                new Product(
                        2,
                        "CHEST",
                        R.drawable.chest));

        productList.add(
                new Product(
                        3,
                        "LEGS",
                        R.drawable.legs));
        productList.add(
                new Product(
                        4,
                        "ARMS",
                        R.drawable.arms));
        productList.add(
                new Product(
                        5,
                        "CORE",
                        R.drawable.core));

        adapter = new ProductAdapter(this,productList);
        recyclerView.setAdapter(adapter );



    }
}