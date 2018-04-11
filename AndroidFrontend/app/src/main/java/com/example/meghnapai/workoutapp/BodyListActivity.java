package com.example.meghnapai.workoutapp;

import android.content.Intent;
import android.os.Parcelable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
//import android.widget.Toolbar;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ListView;
import android.widget.Switch;
import android.widget.Toast;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListAdapter;
import android.widget.ListView;

import com.APICaller.base.WorkoutAPI;
import com.APICaller.exercise.GetExercise;
import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.List;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class BodyListActivity extends AppCompatActivity {

    ListView listView;
    String [] default_bodypart={"Shoulders", "Biceps", "Triceps","Chest","Back", "Legs","Abs","Glutes","Cardio"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_body_list);

        Toolbar toolbar = findViewById(R.id.toolbar);

        OkHttpClient httpClient = new OkHttpClient();
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        Retrofit retrofit = builder.build();
        final WorkoutAPI requests = retrofit.create(WorkoutAPI.class);


       // getActionBar().setTitle("Body Parts to Choose From");
       // getSupportActionBar().setTitle("Body Parts to Choose From");
        listView=(ListView) findViewById(R.id.bodypartlv);

        ListAdapter list = new CustomAdapterExercise(this, default_bodypart);
        listView.setAdapter(list);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long id) {
                String bodyPart=String.valueOf(adapterView.getItemAtPosition(position));
                switch (bodyPart){
                    case "Shoulders":
                        Call<List<GetExercise>> getBodyPart = requests.getExerciseByBodyPart("shoulders");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();

                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();
                                ArrayList<GetExercise> exercises= new ArrayList<GetExercise>(response.body());
                                ArrayList<String> stringExercises = new ArrayList<String>();

                                for(int i = 0; i < exercises.size(); i++){
                                    stringExercises.add(exercises.get(i).getName());
                                }

                                bodyPart.putExtra("Shoulders", stringExercises);
                                extras.putString("shoulders", "shoulders");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });


                      //  Toast.makeText(BodyListActivity.this, "Shoulders", Toast.LENGTH_SHORT).show();
                        break;
                    case "Biceps":
                        Intent biceps = new Intent(BodyListActivity.this, ListViewActivityBiceps.class);
                        BodyListActivity.this.startActivity(biceps);
                        break;
                    case "Triceps":
                        Intent triceps = new Intent(BodyListActivity.this, ListViewActivityTriceps.class);
                        BodyListActivity.this.startActivity(triceps);
                        break;
                    case "Chest":
                        Toast.makeText(BodyListActivity.this, "Chest", Toast.LENGTH_SHORT).show();
                        break;
                    case "Back":
                        Toast.makeText(BodyListActivity.this, "Back", Toast.LENGTH_SHORT).show();
                        break;
                    case "Legs":
                        Toast.makeText(BodyListActivity.this, "Legs", Toast.LENGTH_SHORT).show();
                        break;
                    case "Abs":
                        Toast.makeText(BodyListActivity.this, "Abs", Toast.LENGTH_SHORT).show();
                        break;
                    case "Glutes":
                        Toast.makeText(BodyListActivity.this, "Glutes", Toast.LENGTH_SHORT).show();
                        break;
                    case "Cardio":
                        Toast.makeText(BodyListActivity.this, "Cardio", Toast.LENGTH_SHORT).show();
                        break;

                }
            }
        });
    }



}
