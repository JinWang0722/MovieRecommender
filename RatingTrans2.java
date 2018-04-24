import java.io.*;
import java.util.*;
public class RatingTrans2 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
		ArrayList<String> user = new ArrayList<String>();
		FileReader fileReader = new FileReader("ratings.csv");
       	BufferedReader bufferedReader = new BufferedReader(fileReader);
        String line = null;  
        int c=1;
        while ((line = bufferedReader.readLine()).length()>0) { 
        	if(line.equals("END")) {
        		result.add(user);
        		break;
        	}
        	//System.out.println(line);
        	String[] temp = line.split(",");
        	if(Integer.parseInt(temp[0])==c) {
        		if(Double.parseDouble(temp[2])>=3) {
        			user.add(temp[1]);
        		}
        	}else {
        		result.add(user);
        		user= new ArrayList<String>();
        		c++;
        		if(Double.parseDouble(temp[2])>=3) {
        			user.add(temp[1]);
        		}
        	}
    		
        }
        FileWriter fileWriter = new FileWriter("result.txt");
        PrintWriter printWriter = new PrintWriter(fileWriter);
        printWriter.print("@data\n");
        System.out.println("==================");
        for(int i=0;i<result.size();i++) {
        	String out="";
			for(int j=0; j<result.get(i).size();j++) {
				 if(j==result.get(i).size()-1) out+= result.get(i).get(j);
				 else out= out+result.get(i).get(j)+",";
			}
			printWriter.print(out+"\n");
		}
        printWriter.close();

	}

}
