package com.ChatStuff;

public class Messages {

    private String message;
    private boolean seen;
    private String from;

    public Messages() {

    }

    public Messages(String from) {
        this.from = from;
    }

    public Messages(String message, boolean seen, String from) {
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

    public String getFrom() { return from; }

    public void setFrom(String from) { this.from = from; }
}
