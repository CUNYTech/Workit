import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

import org.omg.CORBA.portable.InputStream;
import com.google.gson.*;
public class Practice {
	public static void DB_NewProjectREST(User usr) {
        // public static String excutePost(String targetURL, String urlParameters)
        //URL url;
        HttpURLConnection connection = null;  
        String name = "abs";
        ///First, all the GSON/JSon stuff up front
        Gson gson = new Gson();
        //convert java object to JSON format
        String json = gson.toJson(name);
      //Then credentials and send string
        String send_string = "bob123/bob123@email.com/1234567/Bob/Thebuilder/male/5.6/ft/156.0/lb/20.0";

        try {
          //Create connection
          URL url = new URL("http://127.0.0.1:5000/user/new/"+send_string);
          String urlParameters = "username=" + URLEncoder.encode(json, "UTF-8");

          connection = (HttpURLConnection)url.openConnection();
//          connection.setRequestMethod("POST");
          connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

//          connection.setRequestProperty("Content-Length", "" + Integer.toString(urlParameters.getBytes().length));
          connection.setRequestProperty("Content-Language", "en-US");  

          connection.setUseCaches(false);
          connection.setDoInput(true);
          connection.setDoOutput(true);

          //Send request
          DataOutputStream wr = new DataOutputStream (connection.getOutputStream ());
          wr.writeBytes (urlParameters);
          wr.flush ();
          wr.close ();

          URL backUrl = new URL("http://127.0.0.1:5000/user/login/bob123/1234567");
          HttpURLConnection newconnection = (HttpURLConnection)backUrl.openConnection();

//          connection.setRequestMethod("POST");
          newconnection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

//        connection.setRequestProperty("Content-Length", "" + Integer.toString(urlParameters.getBytes().length));
          newconnection.setRequestProperty("Content-Language", "en-US");  

          newconnection.setUseCaches(false);
          newconnection.setDoInput(true);
          newconnection.setDoOutput(true);
//          //Get Response    
         InputStream out = (InputStream) newconnection.getInputStream();
         BufferedReader rd = new BufferedReader(new InputStreamReader(out));
          String line;
          StringBuffer response = new StringBuffer(); 
          while((line = rd.readLine()) != null) {
            response.append(line);
            response.append('\r');
          }
          rd.close();
        } catch (Exception e) {
            e.printStackTrace();
            //return null;
        }finally {
            if(connection != null) {
                connection.disconnect(); 
            }
        }
    }
	public static void main(String[] args) {
		User m = new User("soei","soei","eoiwe@gamil.com");
		DB_NewProjectREST(m);
		}
	}
