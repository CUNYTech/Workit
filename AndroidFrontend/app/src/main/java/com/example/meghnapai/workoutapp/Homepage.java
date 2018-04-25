package com.example.meghnapai.workoutapp;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.FrameLayout;
import android.widget.Toast;

import com.ChatStuff.ChatMainActivity;

import java.util.Calendar;

public class Homepage extends AppCompatActivity {

    private BottomNavigationView mMainNav;
    private FrameLayout mMainFrame;

    private HomeFragment homeFragment;
    private LogFragment logFragment;
    private ChatFragment chatFragment;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_homepage);
        final Session session = new Session(this);
        Toast.makeText(this,session.getUsername(),Toast.LENGTH_LONG).show();




        mMainFrame = (FrameLayout) findViewById(R.id.main_Frame);
        mMainNav = (BottomNavigationView) findViewById(R.id.bottomNav);





        mMainNav.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {

                switch (item.getItemId()) {

                    case R.id.nav_home:
                        mMainNav.setItemBackgroundResource(R.color.colorPrimaryDark);
                      //  homeFragment = new HomeFragment();
                       // setFragment(homeFragment);

                        Intent SignInIntent1 = new Intent(Homepage.this, CalendarActivity.class);
                        Homepage.this.startActivity(SignInIntent1);
                        return true;

                    case R.id.nav_log:
                        mMainNav.setItemBackgroundResource(R.color.colorAccent);
                        logFragment = new LogFragment(session);
                        setFragment(logFragment);

                        return true;

                    case R.id.nav_account:
                        mMainNav.setItemBackgroundResource(R.color.pink);
                     //   chatFragment = new ChatFragment();
                     //   setFragment(chatFragment);

                        Intent SignInIntent = new Intent(Homepage.this, ChatMainActivity.class);
                        Homepage.this.startActivity(SignInIntent);
                        return true;

                    default:
                        return false;
                }
            }
        });

    }

    private void setFragment(android.support.v4.app.Fragment fragment) {

        android.support.v4.app.FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
        fragmentTransaction.replace(R.id.main_Frame, fragment);
        fragmentTransaction.commit();

    }


}
