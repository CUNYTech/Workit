package com.APICaller.endPointCom;

import com.APICaller.User.User;
import com.APICaller.base.WorkoutAPI;
import com.APICaller.schedule.Schedule;
import com.APICaller.schedule.ScheduleList;
import com.google.gson.Gson;
import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import java.util.ArrayList;
import java.util.List;

public class Caller {
    OkHttpClient httpClient;
    Retrofit.Builder builder;
    Retrofit retrofit;
    WorkoutAPI requests;
    private ArrayList<Response<ResponseBody>> returnValue = new ArrayList<>();

    public ArrayList<Response<ResponseBody>> getReturnValue() {
        return returnValue;
    }

    public Caller() {
        this.httpClient = new OkHttpClient();
        this.builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        this.retrofit = builder.build();
        this.requests = retrofit.create(WorkoutAPI.class);
    }

    public ArrayList<Response<ResponseBody>> CreateUser(User user){
        final ArrayList<Response<ResponseBody>> returnValue = new ArrayList<>();
        Call<ResponseBody> call = requests.createNewUser(user);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                returnValue.add(response);
                System.out.printf(response.toString());
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.printf("Throws: " + t);
            }
        });

        return returnValue;
    }

    public ArrayList<Response<ResponseBody>> login(String username, String password){
        final ArrayList<Response<ResponseBody>> returnValue = new ArrayList<>();
        Call<ResponseBody> call = requests.login(username,password);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                returnValue.add(response);
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.printf("Throws: " + t);
            }
        });

        return returnValue;
    }

    public void newWorkout(Schedule schedule){

        Call<ResponseBody> call = requests.newSchedulePost(schedule);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                returnValue.add(response);
//                System.out.printf(String.valueOf(response.toString()));



            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.printf("Throws: " + t);
            }
        });



    }

    public void getSchedule(String username, String date, String time){
        Call <List<Schedule>> call = requests.getSchedule(username, date, time);
        call.enqueue(new Callback<List<Schedule>>() {
            @Override
            public void onResponse(Call<List<Schedule>> call, Response<List<Schedule>> response) {
                Gson gson = new Gson();
                System.out.printf(gson.toJson(response.body()));
            }

            @Override
            public void onFailure(Call<List<Schedule>> call, Throwable t) {
                System.out.printf(t.toString());
            }
        });
    }

}
