package com.example.meghnapai.workoutapp;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.APICaller.exercise.Exercise;

import java.util.List;


    public class ProductAdapter extends RecyclerView.Adapter<ProductAdapter.ProductViewHolder> {


        //this context we will use to inflate the layout
        private Context mCtx;

        //we are storing all the products in a list
        private List<Product> productList;

        //getting the context and product list with constructor
        public ProductAdapter(Context mCtx, List<Product> productList) {
            this.mCtx = mCtx;
            this.productList = productList;
        }

        @Override
        public ProductViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
            //inflating and returning our view holder
            LayoutInflater inflater = LayoutInflater.from(mCtx);
            View view = inflater.inflate(R.layout.recycler_workouts_cardview, null);
            return new ProductViewHolder(view);
        }

        @Override
        public void onBindViewHolder(final ProductViewHolder holder, int position) {
            //getting the product of the specified position
            Product product = productList.get(position);

            //binding the data with the viewholder views
            holder.ExerciseTitle.setText(product.getExerciseName());

//            holder.textViewPrice.setText(String.valueOf(product.getPrice()));
//
//            holder.imageView.setImageDrawable(mCtx.getResources().getDrawable(product.getImage()));

        }


        @Override
        public int getItemCount() {
            return productList.size();
        }


        class ProductViewHolder extends RecyclerView.ViewHolder {

            TextView ExerciseTitle;

            public ProductViewHolder(View itemView) {
                super(itemView);

                ExerciseTitle = itemView.findViewById(R.id.Exercise);
                itemView.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Intent SignInIntent = new Intent(mCtx, Listview_reps.class);
                        Bundle extras = new Bundle();
                        extras.putString("ExerciseName", ExerciseTitle.getText().toString());
                        SignInIntent.putExtras(extras);
                        mCtx.startActivity(SignInIntent);

                    }
                });
            }
        }
    }

