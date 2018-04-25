package com.APICaller.base;

import com.APICaller.User.User;
import com.APICaller.exercise.Exercise;
import com.APICaller.exercise.GetExercise;
import com.APICaller.exercise.PostExercise;
import com.APICaller.schedule.Schedule;
import com.APICaller.sets.CalisthenicSet;
import com.APICaller.sets.CardioSet;
import com.APICaller.sets.GetSet;
import com.APICaller.sets.WeightLiftingSet;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.*;

import java.util.ArrayList;
import java.util.List;

public interface WorkoutAPI {
    String BASE_URL = "http://10.0.2.2:5000/";

    @Headers("Content-Type: application/json")
    @POST("/user/new")
    Call<ResponseBody> createNewUser(@Body User newUser);

    @GET("/user/login/{user}/{password}")
    Call<ResponseBody> login(@Path(value = "user", encoded = true) String user, @Path(value = "password", encoded = true) String password);

    @Headers("Content-Type: application/json")
    @POST("/date/new/workout")
    Call<ResponseBody> newSchedulePost(@Body Schedule newSchedule);

    @GET("/date/schedule/workout/{username}/{date}/{time}")
    Call<List<Schedule>> getSchedule(@Path(value = "username", encoded = true) String username, @Path(value = "date", encoded = true) String date, @Path(value = "time", encoded = true) String time);

    // enter exercise
    @Headers("Content-Type: application/json")
    @POST("/date/new/exercise")
    Call<ResponseBody> exercise(@Body Exercise newExercise);

    //weight lifting
    @Headers("Content-Type: application/json")
    @POST("/date/new/exercise/set")
    Call<ResponseBody> newWeightLifingSetPost(@Body ArrayList<WeightLiftingSet> newWeightLifting);

    //cardio sets
    @Headers("Content-Type: application/json")
    @POST("/date/new/exercise/cardio")
    Call<ResponseBody> newCardioSetPost(@Body ArrayList<CardioSet> newCardioSet);

    //calisthenic sets
    @Headers("Content-Type: application/json")
    @POST("/date/new/exercise/calisthenic")
    Call<ResponseBody> newCalisthenicSetPost(@Body ArrayList<CalisthenicSet> newCalisthenicSet);

    @GET("/date/progress/{username}/weight_lifting/{exercise}")
    Call<List<WeightLiftingSet>> getWeightLiftingProgress(@Path(value = "username", encoded = true) String username, @Path(value = "exercise", encoded = true) String exercise);

    @GET("/date/progress/{username}/cardio/{exercise}")
    Call<List<CardioSet>> getCardioProgress(@Path(value = "username", encoded = true) String username, @Path(value = "exercise", encoded = true) String exercise);

    @GET("/date/progress/{username}/calisthenic/{exercise}")
    Call<List<CalisthenicSet>> getCalisthenicProgress(@Path(value = "username", encoded = true) String username, @Path(value = "exercise", encoded = true) String exercise);

    @GET("/date/get/exercises/{bodyPart}")
    Call<List<GetExercise>> getExerciseByBodyPart(@Path(value = "bodyPart", encoded = true) String bodyPart);

    @POST("/date/new/exercise")
    Call<ResponseBody> newExercise(@Body PostExercise exercise);

    @GET("/date/get/exercise/list/{user}/{date}/{time}")
    Call<List<GetExercise>> getExerciseList(@Path(value = "user", encoded = true) String user ,@Path(value = "date", encoded = true) String date, @Path(value = "time", encoded = true) String time);

    @GET("/date/get/sets/{user}/{date}/{time}/{exercise}")
    Call<List<GetSet>> getSetList(@Path(value = "user", encoded = true) String user, @Path(value = "date", encoded = true) String date, @Path(value = "time", encoded = true) String time, @Path(value = "exercise", encoded = true) String exercise);

    @GET("/date/get/unique/exercise/{user}")
    Call<List<GetExercise>> getUniqueExerciseList(@Path(value = "user", encoded = true) String user);
}
