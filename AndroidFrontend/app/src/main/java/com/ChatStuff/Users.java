package com.ChatStuff;

public class Users {
    public String name;
    public String status;

    public Users() {

    }

    public Users(String name, String status) {
        this.name = name;
        this.status = status;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}