package com.example.meghnapai.workoutapp;

import android.app.AlarmManager;
import android.app.DatePickerDialog;
import android.app.PendingIntent;
import android.app.TimePickerDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;

import com.APICaller.base.WorkoutAPI;
import com.APICaller.schedule.Schedule;

import java.sql.Time;
import java.util.Calendar;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class CalendarActivity extends AppCompatActivity implements View.OnClickListener {



    TextView date, time;
    Button dateBtn, timeBtn, createSchedBtn;
    int _hour, _minute, _year, _month, _day , ampm;
    DatePickerDialog datePickerDialog;
    EditText WorkoutName;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendar);

         WorkoutName= (EditText) findViewById(R.id.WorkoutName);

        date = (TextView) findViewById(R.id.textEditDate);
        time = (TextView) findViewById(R.id.textEditTime);

        dateBtn = (Button) findViewById(R.id.dateBtn);
        timeBtn = (Button) findViewById(R.id.timeBtn);
        createSchedBtn = (Button) findViewById(R.id.createSchedBtn);

        dateBtn.setOnClickListener(this);
        timeBtn.setOnClickListener(this);

    }






    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.dateBtn:
                Calendar calendar = Calendar.getInstance();
                 _year = calendar.get(Calendar.YEAR);
                 _month = calendar.get(Calendar.MONTH);
                 _day = calendar.get(Calendar.DAY_OF_MONTH);

                datePickerDialog = new DatePickerDialog(CalendarActivity.this, new DatePickerDialog.OnDateSetListener() {
                    @Override
                    public void onDateSet(DatePicker datePicker, int year, int month, int dayOfMonth) {
                        date.setText((month + 1) + " : " + dayOfMonth  + " : " + year);

                        _year = year;
                        _month = month;
                        _day = dayOfMonth;
                    }
                }, _year, _month, _day);
                datePickerDialog.show();
                break;

            case R.id.timeBtn:
                  Calendar calendar1 =  Calendar.getInstance();
                 _hour = calendar1.get(Calendar.HOUR);
                 _minute = calendar1.get(Calendar.MINUTE);
                 ampm = calendar1.get(Calendar.AM_PM);

                TimePickerDialog timePickerDialog = new TimePickerDialog(CalendarActivity.this, R.style.TimePickerTheme, new TimePickerDialog.OnTimeSetListener() {
                    @Override
                    public void onTimeSet(TimePicker timePicker, int hourOfDay, int minute) {
                        String AMPM = "AM";
                        if (hourOfDay > 11) {
                            AMPM = "PM";
                        }
                        if (hourOfDay>12) {
                            hourOfDay -= 12;
                        }
                        if (hourOfDay==0){
                            hourOfDay= 12;
                        }

                        if (minute<10){

                        time.setText(hourOfDay + " : 0" + minute + AMPM);}

                        else time.setText(hourOfDay + " : " + minute + AMPM);

                        _hour = hourOfDay;
                        _minute=minute;

                    }
                }, _hour, _minute, false);
                timePickerDialog.show();

                break;


        }

    }


    public void clickSchedule(View view) {

        // Schedule schedule = new Schedule(

        //       time.getText().toString(),  // How to pass username to constructor?
        //     date.getText().toString()

        //  );

        final String WorkoutText=WorkoutName.getText().toString();

        //Toast.makeText(CalendarActivity.this, WorkoutText, Toast.LENGTH_LONG).show();

        Calendar notification = Calendar.getInstance();
        notification.set(Calendar.DAY_OF_MONTH, _day );
        notification.set(Calendar.MONTH, _month);
        notification.set(Calendar.HOUR,_hour);
        notification.set(Calendar.MINUTE, _minute);
        final String date = String.valueOf(_day) + '-' + String.valueOf(_month) + '-' + String.valueOf(_year);
        final String _time = time.getText().toString().replace(" ","");
        System.out.println(_time);
        final Session session = new Session(this);



        Schedule schedule = new Schedule(session.getUsername(), date, _time, WorkoutText);

        OkHttpClient httpClient = new OkHttpClient();
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(WorkoutAPI.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient);

        Retrofit retrofit = builder.build();
        WorkoutAPI requests = retrofit.create(WorkoutAPI.class);

        Call<ResponseBody> call = requests.newSchedulePost(schedule);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {

                if(response.code() == 201){
                    System.out.println("Success");
                    Session session = new Session(CalendarActivity.this);
                    session.setDate(date);
                    session.setTime(_time);
                    session.setWorkout(WorkoutText);
                    Intent intent = new Intent(getApplicationContext(),BodyListActivity.class);
                    startActivity(intent);

//                    PendingIntent alarmIntent = PendingIntent.getBroadcast(getApplicationContext(),111,intent,PendingIntent.FLAG_UPDATE_CURRENT);
//
//                    AlarmManager alarmManager = (AlarmManager) getSystemService(ALARM_SERVICE);
//                    alarmManager.set(AlarmManager.RTC_WAKEUP, notification.getTimeInMillis(), alarmIntent);
                    //include AlarmManager after Millis to set up intervals
                }else{
                    System.out.println("Failed");
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.println("Throws: " + t);
            }

        });






    }



}








