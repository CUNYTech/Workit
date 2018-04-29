package com.example.meghnapai.workoutapp;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;


public class HomeFragment extends Fragment {


    public HomeFragment() {
        // Required empty public constructor
    }






    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment


        View v= inflater.inflate(R.layout.fragment_home, container, false);

        Button chat = (Button) v.findViewById(R.id.IncDist);
        Button workoutChoice = (Button) v.findViewById(R.id.workoutChoice);

        chat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent schedule = new Intent(getActivity(), CalendarActivity.class);
                startActivity(schedule);
            }

        });

       // workoutChoice.setOnClickListener(new View.OnClickListener() {
        //    @Override
         //   public void onClick(View view) {
          //      Intent WorkoutChoice = new Intent(getActivity(), .class);
            //    startActivity(WorkoutChoice);
          //  }
        //});
        return v;
    }


}

