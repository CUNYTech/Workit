package APICaller.base;


import APICaller.User.User;
import APICaller.schedule.Schedule;
import APICaller.schedule.ScheduleList;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.*;

import java.util.List;

public interface WorkoutAPI {
    String BASE_URL = "http://localhost:5000/";

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
}
