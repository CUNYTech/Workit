package com.example.meghnapai.workoutapp;


import android.graphics.Color;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.GridLabelRenderer;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;


/**
 * A simple {@link Fragment} subclass.
 */
public class LogFragment extends Fragment {


    public LogFragment() {

    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View v = inflater.inflate(R.layout.fragment_log2, container, false);

        GraphView myGraph = (GraphView) v.findViewById(R.id.graphView);

        myGraph.setTitle("Workout Progress");
        myGraph.setTitleTextSize(100);
        myGraph.setTitleColor(Color.WHITE);

        myGraph.getViewport().setXAxisBoundsManual(true);
        myGraph.getViewport().setMinX(0);
        myGraph.getViewport().setMaxX(11);

        myGraph.getViewport().setYAxisBoundsManual(true);
        myGraph.getViewport().setMinY(0);
        myGraph.getViewport().setMaxY(1000);

        myGraph.getViewport().setScrollable(true);




        GridLabelRenderer gridLabelRenderer =  myGraph.getGridLabelRenderer();

        gridLabelRenderer.setGridColor(Color.WHITE);
        gridLabelRenderer.setVerticalLabelsColor(Color.WHITE);
        gridLabelRenderer.setHorizontalLabelsColor(Color.WHITE);
        gridLabelRenderer.setHorizontalAxisTitle("Date");
        gridLabelRenderer.setHorizontalAxisTitleColor(Color.WHITE);
        gridLabelRenderer.setVerticalAxisTitle("Workout Volume");
        gridLabelRenderer.setVerticalAxisTitleColor(Color.WHITE);



        LineGraphSeries<DataPoint> series = new LineGraphSeries<>(getDataPoints());
        myGraph.addSeries(series);

        series.setColor(Color.BLACK);
        series.setThickness(10);
        series.setDrawBackground(true);
        series.setBackgroundColor(Color.rgb(254,16,77));


        return v;

    }



    private DataPoint[] getDataPoints() {

        DataPoint[] dp = new DataPoint[]{
                new DataPoint(0,0),
                new DataPoint(2,400),
                new DataPoint(5,500),
                new DataPoint(6,550),
                new DataPoint(7,595),
                new DataPoint(9,320),
                new DataPoint(11, 550)

        };

        return (dp);
    }
    //Read data from database
    // String[] columns = {"Dates", "workoutVolume"};  // Dates as X-Value and workoutVolume as Y-Value

    //  Cursor cursor = OURDates and workoutVolume variables.query("MyTable",columns, null, null, null, null, null)

    //  DataPoint[] dp = new DataPoint[cursor.getCount()]; // gets total amount of data points

    //  for (int i = 0; i<cursor.getCount(); i++) {
    //    cursor.moveToNext();
    //    dp [i] = new DataPoint(cursor.getInt(0), cursor.getInt(1));
    //}


    // return (dp);



}


