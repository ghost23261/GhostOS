package com.ghost23261.os;
import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;
import android.graphics.Color;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        tv.setText("GHOST OS | RAZR+ 2025\n\nTerminal Engine Operational.\nRouting to Python Shell...");
        tv.setTextColor(Color.parseColor("#FF00FF"));
        tv.setBackgroundColor(Color.BLACK);
        tv.setTextSize(18f);
        tv.setPadding(40, 40, 40, 40);
        setContentView(tv);
    }
}
