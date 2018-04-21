package com.example.meghnapai.workoutapp;

import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatDialogFragment;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;

/**
 * Created by meghnapai on 4/2/18.
 */

// this is the pop-up for the new exercise
public class ExerciseDialog extends AppCompatDialogFragment {
    private EditText newEx;
    private ExerciseDialogListener listener;
    RadioButton CategoryRB;
    RadioGroup CategoryRG;
    String Category;
    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        LayoutInflater inflater= getActivity().getLayoutInflater();
        final View view= inflater.inflate(R.layout.dialog_new_ex,null);

        CategoryRG = (RadioGroup) view.findViewById(R.id.CategoryRadioGroup);

        CategoryRG.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup radioGroup, int i) {
                int RBId=CategoryRG.getCheckedRadioButtonId();
                CategoryRB= (RadioButton) view.findViewById(RBId);
                Category= CategoryRB.getText().toString();
            }
        });

        builder.setView(view)
                .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        dismiss();

                    }
                })
                // when user clicks ok, the value in the edit text is passed over to the ListViewActivity1 page
                .setPositiveButton("ok", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        String exercise= newEx.getText().toString();
                        listener.applyTexts(exercise,Category);

                    }
                });
        newEx= view.findViewById(R.id.ExNameET);
       // addNewEx= view.findViewById(R.id.button_addEx);
        return builder.create();
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        try {
            listener = (ExerciseDialogListener) context;
        } catch (ClassCastException e) {
            throw new ClassCastException(context.toString()+ "must implement ExerciseDialogListenr");
        }
    }

    public interface ExerciseDialogListener
    {
        void applyTexts(String exercise,String Category);

    }

}
