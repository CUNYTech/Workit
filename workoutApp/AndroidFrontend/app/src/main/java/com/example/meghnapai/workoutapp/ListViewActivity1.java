package com.example.meghnapai.workoutapp;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.ListActivity;
import android.content.Intent;
import android.os.Parcelable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.util.SparseBooleanArray;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.APICaller.base.WorkoutAPI;
import com.APICaller.exercise.GetExercise;
import com.APICaller.exercise.PostExercise;
import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.Arrays;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ListViewActivity1 extends AppCompatActivity implements ExerciseDialog.ExerciseDialogListener {

    private ArrayList<String> arrayList;
    private ArrayAdapter<String> adapter;
    //String newExercise;
    ListView listvw;
    TextView toolbarTitle;
    ArrayList<String> exercises, types;
    String bodyPart;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_view1);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // String [] default_exercise_shoulders={"Arnold Press","Dumbbell Front Raise", "Dumbbell Side Lateral Raise", "Dumbbell Rear Lateral Raise", "Barbell Rear Delt Row"};

        Bundle extras = getIntent().getExtras();

        bodyPart = extras.getString("bodyPartName");
        exercises = getIntent().getStringArrayListExtra("BodyPart");
        types = getIntent().getStringArrayListExtra("type");

        toolbarTitle=(TextView) findViewById(R.id.title);
        toolbarTitle.setText(bodyPart);


        listvw = (ListView) findViewById(R.id.listvw);

        ///arrayList = new ArrayList<>(Arrays.asList(exercises));
        adapter= new ArrayAdapter<String>(this, R.layout.custom_listview_ex,R.id.textView,exercises);

        // adapter=new ArrayAdapter<String>(this,R.layout.)

        //sendng over these values to the constructor in customAdaptorexercise
        // ListAdapter list = new CustomAdapterExercise(this, default_exercise_shoulders);
        listvw.setAdapter(adapter);
        listvw.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long id) {
                String exercise=String.valueOf(adapterView.getItemAtPosition(position));
                //Toast.makeText(ListViewActivity1.this, exercise, Toast.LENGTH_SHORT).show();
                //Toast.makeText(ListViewActivity1.this, position, Toast.LENGTH_SHORT).show();

                String type = types.get(position);
                Bundle extras = new Bundle();
//                System.out.println(position);
//                Toast.makeText(ListViewActivity1.this, type, Toast.LENGTH_SHORT).show();
                switch (type){
                    case "Weight Lifting":
                        Intent weightLift = new Intent(ListViewActivity1.this, WeightsAndRepsActivity.class);
                        ListViewActivity1.this.startActivity(weightLift);;
                        //passing these variables to the other activity page

                        extras.putString("Category",exercise);
                        weightLift.putExtras(extras);
                        startActivity(weightLift);

                        break;

                    case "Cardio":
                        Intent cardio = new Intent(ListViewActivity1.this, CardioReps.class);
                        ListViewActivity1.this.startActivity(cardio);

                        extras.putString("Category",exercise);
                        cardio.putExtras(extras);
                        startActivity(cardio);
                        break;

                    case "Calisthenics":
                        Intent calisthenic = new Intent(ListViewActivity1.this, CalisthenicReps.class);
                        ListViewActivity1.this.startActivity(calisthenic);
                        extras.putString("Category",exercise);
                        calisthenic.putExtras(extras);
                        startActivity(calisthenic);
                        break;

                }



            }
        });

    }

    // the next two methods are for the toolbar and the add button
    @Override
    public boolean onCreateOptionsMenu(Menu menu)
    {
        MenuInflater inflater=getMenuInflater();
        inflater.inflate(R.menu.toolbar_ex_menu,menu);
        return true; //super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item){

        switch (item.getItemId())
        {
            case R.id.action_add:
                openDialog();
                break;

            case R.id.action_delete:
                removeItem();
                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    // for the pop-up
    public void openDialog(){
        ExerciseDialog exerciseDialog = new ExerciseDialog();
        exerciseDialog.show(getSupportFragmentManager(), "Exercise Dialog");
    }

    //for the pop-up
    @Override
    public void applyTexts(final String nexercise, final String ncategory) {

        //Toast.makeText(ListViewActivity1.this,nexercise,Toast.LENGTH_SHORT).show();
        //this is where the new item is being added

        PostExercise newExercise;
        String[] bodyParts = {bodyPart.toLowerCase()};

        newExercise = new PostExercise(nexercise, bodyParts, ncategory);


        OkHttpClient httpClient = new OkHttpClient();
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        Retrofit retrofit = builder.build();
        WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

        Gson gson = new Gson();
        //System.out.println(gender);
        Call<ResponseBody> call = requests.newExercise(newExercise);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if(response.code() == 201) {
                    //newExercise=nexercise;
                    exercises.add(nexercise);
                    types.add(ncategory);
                    adapter.notifyDataSetChanged();
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.printf("Throws: " + t);
            }
        });

    }

    public void removeItem(){
        SparseBooleanArray positionchecker= listvw.getCheckedItemPositions();
        int count = listvw.getCount();

        for(int item=count-1; item>=0; item-- )
        {
            if(positionchecker.get(item) )
            {
                adapter.remove(arrayList.get(item));
            }
        }
        positionchecker.clear();
        adapter.notifyDataSetChanged();
    }

}
//
//        listvw.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
//@Override
//public boolean onItemLongClick(AdapterView<?> adapterView, View view, int i, long l) {
//        SparseBooleanArray positionchecker= listvw.getCheckedItemPositions();
//        int count = listvw.getCount();
//
//        for(int item=count-1; item>=0; item-- )
//        {
//        if(positionchecker.get(item) )
//        {
//        adapter.remove(arrayList.get(item));
//        }
//        }
//        positionchecker.clear();
//        adapter.notifyDataSetChanged();
//        return false;
//        }
//        });