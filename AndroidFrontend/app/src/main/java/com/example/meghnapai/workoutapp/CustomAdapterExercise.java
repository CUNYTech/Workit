package com.example.meghnapai.workoutapp;

import android.content.Context;
import android.support.annotation.NonNull;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

/**
 * Created by meghnapai on 3/28/18.
 */

//this is just for the way I want the list view to look
class CustomAdapterExercise extends ArrayAdapter<String> {
    public CustomAdapterExercise(@NonNull Context context, String [] exercises) {
        super(context, R.layout.custom_listview_ex, exercises);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        LayoutInflater exInflator = LayoutInflater.from(getContext());
        View customView= exInflator.inflate(R.layout.custom_listview_ex, parent, false);
        //Reference to string array list
        String singleEx = getItem(position);
        TextView text = (TextView) customView.findViewById(R.id.textView);

        text.setText(singleEx);
        return customView;

    }
}
