package com.example.meghnapai.workoutapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

import com.squareup.timessquare.CalendarPickerView;

import java.text.DateFormat;
import java.util.Calendar;
import java.util.Date;

public class CalendarActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendar);

        Date today = new Date();  // calendar set to today
        Calendar nextYear = Calendar.getInstance();
        nextYear.add(Calendar.YEAR, 1);  //adds one year to calendar

        CalendarPickerView datePicker = findViewById(R.id.calendar);
        datePicker.init(today, nextYear.getTime())
                .inMode(CalendarPickerView.SelectionMode.RANGE)
                .withSelectedDate(today);

        datePicker.getSelectedDates();



        datePicker.setOnDateSelectedListener(new CalendarPickerView.OnDateSelectedListener() {  //get out date back when selected
            @Override
            public void onDateSelected(Date date) {
               // String selectedDate = DateFormat.getDateInstance(DateFormat.FULL).format(date);

                Calendar calSelect = Calendar.getInstance();
                calSelect.setTime(date);

                String selectedDate = "" + calSelect.get(Calendar.MONTH)
                        + "/" + (calSelect.get(Calendar.DAY_OF_MONTH) ) //ADD ONE SO MONTH DOESNT START AT ZERO
                        + "/" + calSelect.get(Calendar.YEAR);

                Toast.makeText(CalendarActivity.this, selectedDate, Toast.LENGTH_SHORT).show();


            }

            @Override
            public void onDateUnselected(Date date) {

            }
        });
    }
}
