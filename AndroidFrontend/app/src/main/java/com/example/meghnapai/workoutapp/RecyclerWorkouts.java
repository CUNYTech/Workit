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

import com.APICaller.base.WorkoutAPI;
import com.APICaller.exercise.GetExercise;
import com.APICaller.sets.GetSet;

import java.util.ArrayList;
import java.util.List;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RecyclerWorkouts extends AppCompatActivity {

    RecyclerView recyclerView;
    RecyclerView.LayoutManager layoutManager;
    RecyclerView.Adapter adapter;

    ArrayList<GetExercise> exercises;
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



        //getting the recyclerview from xml
        recyclerView = (RecyclerView) findViewById(R.id.RecyclerView);
       recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        //initializing the productlist



        //adding some items to our list

        //adapter.notifyDataSetChanged();

        //creating recyclerview adapter


        Session session = new Session(RecyclerWorkouts.this);
        OkHttpClient httpClient = new OkHttpClient();
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        Retrofit retrofit = builder.build();
        final WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

        Call<List<GetExercise>> call = requests.getExerciseList(session.getUsername(),session.getDate(),session.getTime());

        call.enqueue(new Callback<List<GetExercise>>() {
            @Override
            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                System.out.println("Response: " + response.body());
                exercises = new ArrayList<>(response.body());
                productList = new ArrayList<>();
                for(GetExercise exercise: exercises){
                    System.out.println("exercise: " + exercise.getName());
                    productList.add(new Product(exercise.getName()));

                }

                final ProductAdapter adapter = new ProductAdapter(RecyclerWorkouts.this, productList);
                recyclerView.setAdapter(adapter);
            }

            @Override
            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                System.out.println("Throws: " + t);
            }
        });

        //setting adapter to recyclerview
//recyclerView.setOnClickListener(new View.OnClickListener() {
//    @Override
//    public void onClick(View v)
//
//
//    }
//});


//        recyclerView.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//              //  Toast.makeText(itemView.getContext(), "Position:" + Integer.toString(getPosition()), Toast.LENGTH_SHORT).show();
//            }
//        });
    }



}
