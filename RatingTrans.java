import java.io.*;
import java.util.*;
public class RatingTrans {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String [][] result = new String[20200][27279];
		ArrayList<String> movie = new ArrayList<String>();
		for(int i=0;i<20200;i++) {
			for(int j=0; j<27279;j++) {
				result[i][j]="?";
			}
		}
		FileReader fileReader = new FileReader("ratings.csv");
       	BufferedReader bufferedReader = new BufferedReader(fileReader);
        String line = null;  
        while ((line = bufferedReader.readLine()).length()>0) { 
        	if(line.equals("END")) break;
        	System.out.println(line);
        	String[] temp = line.split(",");
        	int index = -1;
        	for(int i=0;i<movie.size();i++) {
        		if(movie.get(i).equals(temp[1])) {
        			index=i;
        			break;
        		}
        	}
        	if(index==-1) {
        		movie.add(temp[1]);
    			index=movie.size();
        	}
    		if(Double.parseDouble(temp[2])>=3) {
    			int row = Integer.parseInt(temp[0])-1;
    			result[row][index]="y";
    		}
        }
        FileWriter fileWriter = new FileWriter("result.txt");
        PrintWriter printWriter = new PrintWriter(fileWriter);
        printWriter.print("@relation\n\n");
        for(int i=0;i<27279;i++) {
        	printWriter.print("@attribute "+i+"\n");
        }
        printWriter.print("\n");
        printWriter.print("@data\n");
        System.out.println("==================");
        for(int i=0;i<20200;i++) {
        	String out="";
			for(int j=0; j<27279;j++) {
				 if(j==27278) out+= result[i][j];
				 else out= out+result[i][j]+",";
			}
			printWriter.print(out+"\n");
		}
        printWriter.close();

	}

}
