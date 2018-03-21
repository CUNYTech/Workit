package com.examAPICaller;


import com.APICaller.User.User;
import com.APICaller.endPointCom.Caller;
import com.APICaller.schedule.Schedule;
import okhttp3.ResponseBody;
import retrofit2.Response;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        User user  = new User("bob123", "1234567", "bob123@email.com", "Bob", "TheBuilder", "Male", 156.0f
                ,"lb", 5.6f, "ft");

        Schedule schedule1 = new Schedule("bob123", "2-3-2018", "2:00pm", "chest");
        Schedule schedule2 = new Schedule("bob123", "3-3-2018", "2:00pm", "chest");
        Schedule schedule3 = new Schedule("bob123", "4-3-2018", "2:00pm", "chest");
        Schedule schedule4 = new Schedule("bob123", "8-4-2018", "2:00pm", "chest");


        Caller newCall = new Caller();

//        executeCall1(newCall, user, schedule1);


//        ArrayList<Response<ResponseBody>> createUser = newCall.CreateUser(user);
//        System.out.println(createUser.toString());
//
//        ArrayList<Response<ResponseBody>> scheduleCall2 = newCall.newWorkout(schedule2);
//        System.out.printf(scheduleCall2.get(1).toString());
//        ArrayList<Response<ResponseBody>> scheduleCall3 = newCall.newWorkout(schedule3);
//        newCall.newWorkout(schedule4);
//        ArrayList<Response<ResponseBody>> scheduleCall4 = newCall.getReturnValue();
//        System.out.printf(scheduleCall4.get(0).toString());
        newCall.getSchedule("bob123", "2-2-2018", "2:00pm");

    }



}
