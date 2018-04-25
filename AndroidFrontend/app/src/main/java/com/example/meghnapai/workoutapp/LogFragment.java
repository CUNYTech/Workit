package com.example.meghnapai.workoutapp;


import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.APICaller.base.WorkoutAPI;
import com.APICaller.sets.GetSet;
import com.APICaller.sets.WeightLiftingSet;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.GridLabelRenderer;
import com.jjoe64.graphview.helper.DateAsXAxisLabelFormatter;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.TimeZone;

import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


/**
 * A simple {@link Fragment} subclass.
 */
@SuppressLint("ValidFragment")
public class LogFragment extends Fragment {
    private Session session;
    private ArrayList<WeightLiftingSet> sets;
    private  DataPoint [] data;


    @SuppressLint("ValidFragment")
    public LogFragment(Session session) {
        this.session = session;
    }



    @Override
    public View onCreateView(final LayoutInflater inflater, final ViewGroup container,
                             final Bundle savedInstanceState) {

        Thread  thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    callGetRequest();

                } catch (IOException e) {
                    e.printStackTrace();
                }

            }
        });

        thread.start();

        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }


        return createGraph(inflater,container,savedInstanceState);
   }

    @SuppressLint("SimpleDateFormat")
    private View createGraph(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState){

        data = getDataPoints(sets);
        View v = inflater.inflate(R.layout.fragment_log2, container, false);
        GraphView myGraph = (GraphView) v.findViewById(R.id.graphView);

        myGraph.setTitle("Workout Progress");
        myGraph.setTitleTextSize(100);
        myGraph.setTitleColor(Color.WHITE);

        myGraph.getViewport().setXAxisBoundsManual(false);
        myGraph.getViewport().setYAxisBoundsManual(false);
        myGraph.getViewport().setScrollable(true);

        GridLabelRenderer gridLabelRenderer =  myGraph.getGridLabelRenderer();

        gridLabelRenderer.setLabelFormatter(new DateAsXAxisLabelFormatter(getContext(),new SimpleDateFormat("Y-M-dd")));
        gridLabelRenderer.setGridColor(Color.WHITE);
        gridLabelRenderer.setVerticalLabelsColor(Color.WHITE);
        gridLabelRenderer.setHorizontalLabelsColor(Color.WHITE);
        gridLabelRenderer.setHorizontalAxisTitle("Date");
        gridLabelRenderer.setHorizontalAxisTitleColor(Color.WHITE);
        gridLabelRenderer.setVerticalAxisTitle("Weight");
        gridLabelRenderer.setVerticalAxisTitleColor(Color.WHITE);

        LineGraphSeries<DataPoint> series = new LineGraphSeries<>(data);
        myGraph.addSeries(series);

        series.setColor(Color.BLACK);
        series.setThickness(10);
        series.setDrawBackground(true);
        series.setBackgroundColor(Color.rgb(254,16,77));

        return v;
    }

    private void callGetRequest() throws IOException {
        OkHttpClient httpClient = new OkHttpClient();
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        Retrofit retrofit = builder.build();
        final WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

        Call<List<WeightLiftingSet>> call = requests.getWeightLiftingProgress(session.getUsername(),"barbell chest press");
        sets = new ArrayList<>(call.execute().body());
    }



    private DataPoint[] getDataPoints(ArrayList<WeightLiftingSet> sets) {
        DataPoint[] dp = new DataPoint[sets.size()];

        for(int i = 0; i < sets.size(); i++){
            Date date = new Date(sets.get(i).getDate());
            dp[i] = new DataPoint(date,sets.get(i).getWeight());
        }


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

