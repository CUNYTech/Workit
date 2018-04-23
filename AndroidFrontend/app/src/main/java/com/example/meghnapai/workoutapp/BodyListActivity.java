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
import android.widget.TextView;
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
    TextView toolbarTitle;
    Call<List<GetExercise>> getBodyPart;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_body_list);

        Toolbar toolbar = findViewById(R.id.toolbar);
        toolbarTitle=(TextView) findViewById(R.id.title);
        toolbarTitle.setText("Muscle Groups");


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
                        getBodyPart = requests.getExerciseByBodyPart("shoulders");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                        System.out.println(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "shoulders");
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
                        getBodyPart = requests.getExerciseByBodyPart("biceps");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Biceps");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Triceps":
                        getBodyPart = requests.getExerciseByBodyPart("triceps");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Triceps");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Chest":
                        getBodyPart = requests.getExerciseByBodyPart("chest");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Chest");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Back":
                        getBodyPart = requests.getExerciseByBodyPart("back");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Back");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Legs":
                        getBodyPart = requests.getExerciseByBodyPart("legs");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Legs");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Abs":
                        getBodyPart = requests.getExerciseByBodyPart("abs");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Abs");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Glutes":
                        getBodyPart = requests.getExerciseByBodyPart("glutes");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Glutes");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;
                    case "Cardio":
                        getBodyPart = requests.getExerciseByBodyPart("cardio");
                        getBodyPart.enqueue(new Callback<List<GetExercise>>() {

                            @Override
                            public void onResponse(Call<List<GetExercise>> call, Response<List<GetExercise>> response) {
                                Gson gson = new Gson();
                                ArrayList<GetExercise> exercises = null;
                                ArrayList<String> stringExercises = new ArrayList<String>();
                                ArrayList<String> stringTypes = new ArrayList<String>();
                                Intent bodyPart = new Intent(BodyListActivity.this, ListViewActivity1.class);
                                Bundle extras = new Bundle();

                                if(response.body() != null) {
                                    exercises = new ArrayList<GetExercise>(response.body());


                                    for (int i = 0; i < exercises.size(); i++) {
                                        stringExercises.add(exercises.get(i).getName());
                                        stringTypes.add(exercises.get(i).getType());
                                    }
                                }else
                                    stringExercises.add("nothing is here");
                                bodyPart.putExtra("type", stringTypes);
                                bodyPart.putExtra("BodyPart", stringExercises);
                                extras.putString("bodyPartName", "Cardio");
                                bodyPart.putExtras(extras);
                                BodyListActivity.this.startActivity(bodyPart);

                            }

                            @Override
                            public void onFailure(Call<List<GetExercise>> call, Throwable t) {
                                System.out.println(t);
                            }
                        });
                        break;

                }
            }
        });
    }



}
