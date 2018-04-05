package com.example.meghnapai.workoutapp;

import android.app.LauncherActivity;
import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

/**
 * Created by meghnapai on 3/25/18.
 */

// for the Body Part Recycler View
    /*
    For Recycler view we need 2 things:
    RecyclerView.Adapter-->combines data to the view
    RecyclerView.iewHolder -->holds the view

     */
public class ProductAdapter extends RecyclerView.Adapter<ProductAdapter.ProductViewHolder>{

    private Context mctx;
    private List<Product> ProductList;


    public ProductAdapter(Context mctnx, List<Product> productList) {
        this.mctx = mctnx;
        ProductList = productList;
    }

    //Returns the view_holder, i.e. UI Elements
    @Override
    public ProductViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(mctx);
        View view= inflater.inflate(R.layout.bodypart_list_layout, null);
        ProductViewHolder holder= new ProductViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(ProductViewHolder holder, final int position) {
        final Product product= ProductList.get(position);
        holder.textViewTitle.setText(product.getTitle());
        holder.imageview.setImageDrawable(mctx.getResources().getDrawable(product.getImage()));
        holder.parentLayout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(mctx, String.valueOf(product.getId()),Toast.LENGTH_SHORT).show();
            }}
        );
    }

    @Override
    public int getItemCount() {
        return ProductList.size();
    }

    class ProductViewHolder extends RecyclerView.ViewHolder{

        ImageView imageview;
        TextView textViewTitle;
        RelativeLayout parentLayout;
        public ProductViewHolder(View itemView) {
            super(itemView);

            imageview= itemView.findViewById(R.id.imageView);
            textViewTitle= itemView.findViewById(R.id.textViewTitle);
            parentLayout= itemView.findViewById(R.id.parent_layout);
        }
    }
}
