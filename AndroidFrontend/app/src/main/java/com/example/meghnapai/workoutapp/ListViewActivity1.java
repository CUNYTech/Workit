package com.example.meghnapai.workoutapp;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.ListActivity;
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

import java.util.ArrayList;
import java.util.Arrays;

public class ListViewActivity1 extends AppCompatActivity implements ExerciseDialog.ExerciseDialogListener {

    private ArrayList<String> arrayList;
    private ArrayAdapter<String> adapter;
    String newExercise;
    ListView listvw;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_view1);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        String [] default_exercise_shoulders={"Arnold Press","Dumbbell Front Raise", "Dumbbell Side Lateral Raise", "Dumbbell Rear Lateral Raise", "Barbell Rear Delt Row"};

        listvw = (ListView) findViewById(R.id.listvw);

        arrayList = new ArrayList<>(Arrays.asList(default_exercise_shoulders));
        adapter= new ArrayAdapter<String>(this, R.layout.custom_listview_ex,R.id.textView,arrayList);
       // adapter=new ArrayAdapter<String>(this,R.layout.)

        //sendng over these values to the constructor in customAdaptorexercise
       // ListAdapter list = new CustomAdapterExercise(this, default_exercise_shoulders);
        listvw.setAdapter(adapter);
        listvw.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long id) {
                String exercise=String.valueOf(adapterView.getItemAtPosition(position));
                Toast.makeText(ListViewActivity1.this, exercise, Toast.LENGTH_SHORT).show();
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
    public void applyTexts(String nexercise) {
         newExercise=nexercise;
         //Toast.makeText(ListViewActivity1.this,nexercise,Toast.LENGTH_SHORT).show();
         //this is where the new item is being added
         arrayList.add(newExercise);
        adapter.notifyDataSetChanged();

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
