package com.example.calculator;

import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

// it is also a launcher activity (first activity if you want to open your app)
public class SplashScreen extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_screen);

        // On java, main code will work on the main thread, also supports the UI
        // It cannot be stopped, or UI is crashed
        // In java, we should do: main tread still runs
        // but, create a new thread, and after xxx seconds, move to there
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent i = new Intent(SplashScreen.this, MainActivity.class); // switch from here to MainActivity
                startActivity(i); // run this intent
                // this means: after 3s, go to MainActivity.java
                finish(); // if we go to the MainActivity.java, it will not go back to SplashScreen
                // finish() simplt means: end the Activity here
            }
        }, 3000); // move to this thread with a delay of 3 seconds





    }
}