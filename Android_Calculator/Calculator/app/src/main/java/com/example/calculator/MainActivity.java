package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.view.View;
import android.widget.TextView;

// xml----layout of the app (front end)
// java----function of the  (back end)

// in here, get two inputs from XML widgets(窗体), do the calculation, then push the output back
// to XML

public class MainActivity extends AppCompatActivity {

    EditText et1,et2; // two inputs (EditText) in XML
    Button add, sub, mul, div; // four buttons in XML
    TextView output;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        et1 = findViewById(R.id.op1);
        // search the Views in layout and get a value from the TextView
        // the XML code is 'android:id="@+id/op2"', so R.id.op1
        et2 = findViewById(R.id.op2); // similar for op2

        add = findViewById(R.id.add);
        sub = findViewById(R.id.sub);
        mul = findViewById(R.id.multiply);
        div = findViewById(R.id.divide);

        output = findViewById(R.id.Output);
    }

    // creat four functions for output
    public void addFunc(View v) {
        try {
            String op1 = et1.getText().toString(); // get an input (from onCreate by default it is a text)
            String op2 = et2.getText().toString();

            Float op1num = Float.parseFloat(op1);
            Float op2num = Float.parseFloat(op2);
            // Get 2 strings as 2 inputs, make them floating number, add, subtract, multiply,or divide them

            Float out = op1num + op2num;
            output.setText(String.valueOf(out));
        } catch (Exception e) {
            output.setText("Enter all values to continue");
        }
    }

    public void subFunc(View v) {
        try {
            String op1 = et1.getText().toString();
            String op2 = et2.getText().toString();

            Float op1num = Float.parseFloat(op1);
            Float op2num = Float.parseFloat(op2);

            Float out = op1num - op2num;
            output.setText(String.valueOf(out));
        } catch (Exception e) {
            output.setText("Enter all values to continue");
        }
    }

    public void mulFunc(View v) {
        try {
            String op1 = et1.getText().toString();
            String op2 = et2.getText().toString();

            Float op1num = Float.parseFloat(op1);
            Float op2num = Float.parseFloat(op2);

            Float out = op1num * op2num;
            output.setText(String.valueOf(out));
        } catch (Exception e) {
            output.setText("Enter all values to continue");
        }
    }

    public void divFunc(View v) {
        try {
            String op1 = et1.getText().toString();
            String op2 = et2.getText().toString();

            Float op1num = Float.parseFloat(op1);
            Float op2num = Float.parseFloat(op2);

            Float out = op1num / op2num;
            output.setText(String.valueOf(out));
        } catch (Exception e) {
            output.setText("Enter all values to continue");
        }
    }
}