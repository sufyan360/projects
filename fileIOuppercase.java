//Name: Sufyan Chaudhry
//Date: 11/9/22
//Purpose: To write a class that makes two files one that writes and another that reads that file and makes it uppercase


//import file IO and scanner
import java.io.*;
import java.util.Scanner;


public class fileIOuppercase 
{

	public static void main(String[] args)  
	{
		//Make a scanner and get the file name
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the writing file name: ");
		String write = input.nextLine();
		
		//Have error exception so the file runs
		try 
		{
			
		//Create the object for the file and then use scanner to get its contents
		PrintWriter outputFile = new PrintWriter(write);
		System.out.println("Enter file contents: ");
		String content = input.nextLine();
		
		//Write the contents in the file and close the file
		outputFile.write(content);
		outputFile.close();
		
		
		
		//Make a new file object for the reading file
		
		File file = new File (write);
		
		//Have scanner read the file
		Scanner inputFile = new Scanner (file);
		
		//Get the second file name and make object
		System.out.println("What do you want to call the second file: ");
		String read = input.nextLine();
		PrintWriter caps = new PrintWriter(read);
		
		//While loop to read the content and change to uppercase
		while (inputFile.hasNext())
		{
			String line = inputFile.nextLine();
			caps.println(line.toUpperCase());
		}
		
		System.out.println("Check the files.");
		
		//Close the files
		caps.close();
		inputFile.close();
		}
		
		//Exception for error handling
		catch(Exception e)
		{
			System.err.println("File not found");
		}

	}

}
