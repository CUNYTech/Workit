package com.ChatStuff;

public class Messages {

    private String message;
    private boolean seen;

    public Messages() {

    }

    public Messages(String message, boolean seen) {
        this.message = message;
        this.seen = true;
    }

    public boolean isSeen() {
        return seen;
    }

    public void setSeen(boolean seen) {
        this.seen = seen;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
