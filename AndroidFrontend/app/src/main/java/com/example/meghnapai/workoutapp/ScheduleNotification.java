package com.example.meghnapai.workoutapp;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.support.v4.app.NotificationCompat;

import com.example.meghnapai.workoutapp.R;
import com.example.meghnapai.workoutapp.WorkoutLog;

/**
 * Created by dajco on 3/16/2018.
 */

public class ScheduleNotification extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {

        NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);

       Intent workout_log = new Intent(context, WorkoutLog.class);
        workout_log.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP); // ENSURES NEW ACTIVITY CALLED REPLACES CURRENT ACTIVITY IF RUNNING

       PendingIntent pendingIntent = PendingIntent.getActivity(context,100, workout_log,PendingIntent.FLAG_UPDATE_CURRENT);

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context)
                .setContentIntent(pendingIntent)
                .setSmallIcon(R.mipmap.ic_launcher)
                .setContentTitle("YOUR WORKOUT")
                .setContentText("YOUR SHOULD BE WORKING OUT RIGHT NOW!")
                .setSound(RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
                .setAutoCancel(true);

       notificationManager.notify(100,builder.build());

    }
}
