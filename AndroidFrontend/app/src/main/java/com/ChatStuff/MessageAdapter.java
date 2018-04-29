package com.ChatStuff;

import android.graphics.Color;
import android.support.v4.content.ContextCompat;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.example.meghnapai.workoutapp.R;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.auth.FirebaseAuth;

import java.util.List;

public class MessageAdapter extends RecyclerView.Adapter<MessageAdapter.MessageViewHolder>{


    private List<Messages> mMessageList;
    private DatabaseReference mUserDatabase;
    private FirebaseAuth mAuth;

    public MessageAdapter(List<Messages> mMessageList) {
        this.mMessageList = mMessageList;
    }

    @Override
    public MessageViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

        View v = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.message_single_layout ,parent, false);

        return new MessageViewHolder(v);
    }

    public class MessageViewHolder extends RecyclerView.ViewHolder {

        public TextView messageText;
        public TextView displayName;

        public MessageViewHolder(View view) {
            super(view);

            messageText = (TextView) view.findViewById(R.id.message_text);
        }
    }

    @Override
    public void onBindViewHolder(final MessageViewHolder viewHolder, int i) {
        mAuth = FirebaseAuth.getInstance();
        String currentUserID = mAuth.getCurrentUser().getUid();
        Messages c = mMessageList.get(i);
        String from_user = c.getFrom();
        if (from_user.equals(currentUserID)) {
            viewHolder.messageText.setBackgroundColor(Color.parseColor("#551f31"));
            viewHolder.messageText.setTextColor(Color.WHITE);
        }
        else {
            viewHolder.messageText.setBackgroundColor(Color.parseColor("#23283a"));
            viewHolder.messageText.setTextColor(Color.WHITE);
        }
        viewHolder.messageText.setText(c.getMessage());

    }

    @Override
    public int getItemCount() {
        return mMessageList.size();
    }
}