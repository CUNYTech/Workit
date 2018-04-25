package com.ChatStuff;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.meghnapai.workoutapp.R;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.text.DateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class ChatUserProfileActivity extends AppCompatActivity {

    private TextView mProfileName, mProfileStatus, mProfileFriendCount;
    private Button mProfileSendReqBtn, mProfileDenyReqBtn;

    private String mCurrent_state;

    private FirebaseUser mCurrentUser;
    private DatabaseReference mFriendRequestsDatabase;
    private DatabaseReference mFriendDatabase;
    private DatabaseReference mUsersDatabase;
    private ProgressDialog mProgressDialog;
    private DatabaseReference mRootRef;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat_user_profile);
        final String userID = getIntent().getStringExtra("user_id");

        mUsersDatabase = FirebaseDatabase.getInstance().getReference("Users").child(userID);
        mFriendRequestsDatabase = FirebaseDatabase.getInstance().getReference().child("Friend_Requests");
        mFriendDatabase = FirebaseDatabase.getInstance().getReference().child("Friends");
        mCurrentUser = FirebaseAuth.getInstance().getCurrentUser();
        mRootRef = FirebaseDatabase.getInstance().getReference();

        mProfileName = (TextView) findViewById(R.id.profile_display_name);
        mProfileStatus = (TextView) findViewById(R.id.profile_user_status);
        mProfileFriendCount = (TextView) findViewById(R.id.profile_friend_count);
        mProfileSendReqBtn = (Button) findViewById(R.id.profile_friend_request);
        mProfileDenyReqBtn = (Button) findViewById(R.id.profile_friend_request_deny);

        mCurrent_state = "not_friends";
        mProfileDenyReqBtn.setVisibility(View.INVISIBLE);
        mProfileDenyReqBtn.setEnabled(false);

        mProgressDialog = new ProgressDialog(this);
        mProgressDialog.setTitle("Loading user data...");
        mProgressDialog.setMessage("Standby");
        mProgressDialog.setCanceledOnTouchOutside(false);
        mProgressDialog.show();



        mUsersDatabase.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String display_name = dataSnapshot.child("name").getValue().toString();
                String status = dataSnapshot.child("status").getValue().toString();

                mProfileName.setText(display_name);
                mProfileStatus.setText(status);


                // FRIENDS LIST AND REQUESTS FEATURE

                mFriendRequestsDatabase.child(mCurrentUser.getUid()).addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(DataSnapshot dataSnapshot) {
                        if (dataSnapshot.hasChild(userID)) {
                            String requestType = dataSnapshot.child(userID).child("request_type").getValue().toString();
                            if (requestType.equals("request_received")) {
                                mCurrent_state = "req_received";
                                mProfileSendReqBtn.setText("Accept Friend Request");
                                mProfileDenyReqBtn.setVisibility(View.VISIBLE);
                                mProfileDenyReqBtn.setEnabled(true);
                            } else if (requestType.equals("sent")) {
                                mCurrent_state = "req_sent";
                                mProfileSendReqBtn.setText("Cancel Friend Request");
                                mProfileDenyReqBtn.setVisibility(View.INVISIBLE);
                                mProfileDenyReqBtn.setEnabled(false);
                            }
                            mProgressDialog.dismiss();
                        }
                        else {
                            mFriendDatabase.child(mCurrentUser.getUid()).addListenerForSingleValueEvent(new ValueEventListener() {
                                @Override
                                public void onDataChange(DataSnapshot dataSnapshot) {
                                    if (dataSnapshot.hasChild(userID)) {
                                        mCurrent_state = "friends";
                                        mProfileSendReqBtn.setText("Unfriend User");
                                        mProfileDenyReqBtn.setVisibility(View.INVISIBLE);
                                        mProfileDenyReqBtn.setEnabled(false);
                                    }
                                    mProgressDialog.dismiss();
                                }

                                @Override
                                public void onCancelled(DatabaseError databaseError) {
                                    mProgressDialog.dismiss();
                                }
                            });
                        }
                    }
                    @Override
                    public void onCancelled(DatabaseError databaseError) {

                    }
                });
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });


        mProfileSendReqBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mProfileSendReqBtn.setEnabled(false);  // user can't click on the send friend request twice
                // NOT FRIENDS STATE
                if (mCurrent_state.equals("not_friends")) {
                    mFriendRequestsDatabase.child(mCurrentUser.getUid()).child(userID).child("request_type").setValue("sent").addOnCompleteListener(new OnCompleteListener<Void>() {
                        @Override
                        public void onComplete(@NonNull Task<Void> task) {
                            if (task.isSuccessful()) {
                                mFriendRequestsDatabase.child(userID).child(mCurrentUser.getUid()).child("request_type").setValue("request_received").addOnSuccessListener(new OnSuccessListener<Void>() {
                                    @Override
                                    public void onSuccess(Void aVoid) {
                                        mProfileSendReqBtn.setEnabled(true);
                                        mCurrent_state = "req_sent";
                                        mProfileSendReqBtn.setText("Cancel Friend Request");
                                        mProfileDenyReqBtn.setVisibility(View.INVISIBLE);
                                        mProfileDenyReqBtn.setEnabled(false);
                                        Toast.makeText(ChatUserProfileActivity.this, "Friend request sent", Toast.LENGTH_LONG).show();
                                    }
                                });
                            } else {
                                Toast.makeText(ChatUserProfileActivity.this, "Friend request failed", Toast.LENGTH_LONG).show();
                            }
                        }
                    });
                }
                // CANCEL FRIENDS STATE
                if (mCurrent_state.equals("req_sent")) {
                    mFriendRequestsDatabase.child(mCurrentUser.getUid()).child(userID).removeValue().addOnSuccessListener(new OnSuccessListener<Void>() {
                        @Override
                        public void onSuccess(Void aVoid) {
                            mFriendRequestsDatabase.child(userID).child(mCurrentUser.getUid()).removeValue().addOnSuccessListener(new OnSuccessListener<Void>() {
                                @Override
                                public void onSuccess(Void aVoid) {
                                    mProfileSendReqBtn.setEnabled(true);
                                    mCurrent_state = "not_friends";
                                    mProfileSendReqBtn.setText("Send Friend Request");
                                }
                            });
                        }
                    });
                }

                // REQUEST RECEIVED STATE
                if (mCurrent_state.equals("req_received")) {

                    final String currentDate = DateFormat.getDateTimeInstance().format(new Date());
                    Map friendsMap = new HashMap();
                    friendsMap.put("Friends/" + mCurrentUser.getUid() + "/" + userID + "/date", currentDate);
                    friendsMap.put("Friends/" + userID + "/"  + mCurrentUser.getUid() + "/date", currentDate);

                    friendsMap.put("Friend_Requests/" + mCurrentUser.getUid() + "/" + userID, null);
                    friendsMap.put("Friend_Requests/" + userID + "/" + mCurrentUser.getUid(), null);


                    mRootRef.updateChildren(friendsMap, new DatabaseReference.CompletionListener() {
                        @Override
                        public void onComplete(DatabaseError databaseError, DatabaseReference databaseReference) {


                            if(databaseError == null){

                                mProfileSendReqBtn.setEnabled(true);
                                mCurrent_state = "friends";
                                mProfileSendReqBtn.setText("Unfriend User");

                                mProfileDenyReqBtn.setVisibility(View.INVISIBLE);
                                mProfileDenyReqBtn.setEnabled(false);

                            } else {

                                String error = databaseError.getMessage();

                                Toast.makeText(ChatUserProfileActivity.this, error, Toast.LENGTH_SHORT).show();
                            }
                        }
                    });
                }


                // UNFRIEND STUFF
                if(mCurrent_state.equals("friends")) {
                    mFriendDatabase.child(mCurrentUser.getUid()).child(userID).removeValue().addOnSuccessListener(new OnSuccessListener<Void>() {
                        @Override
                        public void onSuccess(Void aVoid) {
                            mFriendDatabase.child(userID).child(mCurrentUser.getUid()).removeValue().addOnSuccessListener(new OnSuccessListener<Void>() {
                                @Override
                                public void onSuccess(Void aVoid) {
                                    mProfileSendReqBtn.setEnabled(true);
                                    mCurrent_state = "not_friends";
                                    mProfileSendReqBtn.setText("Send Friend Request");
                                    mProfileSendReqBtn.setEnabled(true);
                                }
                            });
                        }
                    });
                }
            }
        });
    }
}
