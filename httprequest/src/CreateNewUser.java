import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import com.google.gson.*;

import java.io.DataOutputStream;
import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.lang.Object;

import org.apache.hc.client5.http.classic.HttpClient;
import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClientBuilder;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.HttpResponse;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.io.entity.StringEntity;
import org.apache.hc.core5.http.message.BasicClassicHttpRequest;
import org.json.JSONException;
import 	org.json.JSONObject;
public class CreateNewUser{

	public void connection() {
	HttpClient httpClient = HttpClientBuilder.create().build(); //Use this instead 

	try {

	    HttpPost request = new HttpPost("http://127.0.0.1:5000/user/new");
	    StringEntity params =new StringEntity("{\"username\":\"myname\",\"email\":\"20@qmail.com\",\"password\":\"123456\",\"fname\":\"seoi\",\"lname\":\"dioe\",\"gender\":\"female\",\"height\":\"123\",\"heightUnit\":\"cm\",\"weight\":\"123\",\"weightUnits\":\"lb\",\"bmi\":\"12.4\"} ");
	    request.addHeader("content-type", "application/x-www-form-urlencoded");
	    request.setEntity(params);
	    HttpResponse response = httpClient.execute(request);
	    String json = EntityUtils.toString(((BasicClassicHttpRequest) response).getEntity());
	    //handle response here...
	   System.out.println(json);

	}catch (Exception ex) {

	    //handle exception here

	} finally {
	    //Deprecated
	    //httpClient.getConnectionManager().shutdown(); 
	}

	}
}