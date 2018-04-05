package com.example.meghnapai.workoutapp;

import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.FrameLayout;
import android.widget.Toast;

public class Homepage extends AppCompatActivity {

    private BottomNavigationView mMainNav;
    private FrameLayout mMainFrame;

    private HomeFragment homeFragment;
    private LogFragment logFragment;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_homepage);
        Session session = new Session(this);
        Toast.makeText(this,session.getUsername(),Toast.LENGTH_LONG).show();




        mMainFrame = (FrameLayout) findViewById(R.id.main_Frame);
        mMainNav = (BottomNavigationView) findViewById(R.id.bottomNav);





        mMainNav.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {

                switch (item.getItemId()) {

                    case R.id.nav_home:
                        mMainNav.setItemBackgroundResource(R.color.colorPrimaryDark);
                        homeFragment = new HomeFragment();
                        setFragment(homeFragment);
                        return true;

                    case R.id.nav_log:
                        mMainNav.setItemBackgroundResource(R.color.colorAccent);
                        logFragment = new LogFragment();
                        setFragment(logFragment);

                        return true;

                    case R.id.nav_account:
                        mMainNav.setItemBackgroundResource(R.color.pink);

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

