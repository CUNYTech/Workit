
public class User {
public String userName;
public String pw;
public String email;
public User(String u, String p, String em) {
	userName = u;
	pw = p;
	email = em;
}
public String getUserEmail() {
	return this.email;
}
}
