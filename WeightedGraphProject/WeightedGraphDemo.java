//Sufyan Chaudhry
//4-29-23
//Will be a JavaFX GUI application
//Reading data from a file and then displaying the weighted graph, edges, a MST, and the shortest path between two vertices
//Let the user select which file and which two vertices to get the shortest path of
package application;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import application.WeightedGraph.MST;
import application.WeightedGraph.ShortestPathTree;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class WeightedGraphDemo extends Application {
	
	public static void main(String args[]) {
		launch(args);
	}
	
	//Make weightedGraph and weightedEdge objects
	private static WeightedGraph<Integer> WGraph;
	private static List<WeightedEdge> edges;
	
	//This is the variable that will store the file name
	private String filePicked;
	
	//Seperate buttons for each file
	private Button file1, file2, file3;
	
	//Label to display the weighted graph
	private Label displayGraph;
	
	//Labels to display the minimum spanning tree information
	private Label displayMST;
	private Label displayMSTweight;
	
	//To display the shortest path between methods
	private Label displayShortest;
	private TextField vert1;
	private TextField vert2;
	private Button getPath;
	
	public void start(Stage primaryStage) {
		
		//Setting to 0
		vert1 = new TextField("00");
		vert2 = new TextField("00");
		
		//Showing the user the file names as buttons and setting the file name variable to null
		file1 = new Button("WeightedGraphSample.txt");
		file2 = new Button("WeightedGraphSample1.txt");
		file3 = new Button("WeightedGraphSample2.txt");
		filePicked = null;
		
		//If file1 button is clicked then resetting the vertices for the shortest path, making the file picked the first file, reading the file and storing everything and calling the set data method
		file1.setOnAction(e -> {
			
			vert1.setText("0");
			vert2.setText("0");
			
			filePicked = "WeightedGraphSample.txt";
			loadData(filePicked);
			setData();
		});
		
		//If file2 button is clicked then resetting the vertices for the shortest path, making the file picked the second file, reading the file and storing everything and calling the set data method
		file2.setOnAction(e -> {
			
			vert1.setText("0");
			vert2.setText("0");
			
			filePicked = "WeightedGraphSample1.txt";
			loadData(filePicked);
			setData();
		});
		
		//If file3 button is clicked then resetting the vertices for the shortest path, making the file picked the third file, reading the file and storing everything and calling the set data method
		file3.setOnAction(e -> {
			
			vert1.setText("0");
			vert2.setText("0");
			
			filePicked = "WeightedGraphSample2.txt";
			loadData(filePicked);
			setData();
		});
		
		
		//Setting text for the getPath button
		getPath = new Button("Get shortest path between these verticies");

		//Hiding the shortest path stuff so the user has to pick a file first and then they can access these fields
		getPath.setVisible(false);
		vert1.setVisible(false);
		vert2.setVisible(false);
		
		//If getPath is clicked then setting the data again but this time not setting the verticies to 0
		getPath.setOnAction(e -> {
			setData();
				
		});	
		
		//Initializing all the lables but leaving them blank until a file is clicked
		displayGraph = new Label ();
		
		displayMST = new Label ();
	
		displayMSTweight = new Label();
		
		displayShortest = new Label();
		
		//Adding the file buttons into an hbox
		HBox files = new HBox(10, file1, file2, file3);
		files.setAlignment(Pos.CENTER);
		
		//Adding the shortest path attributes into an hbox
		HBox shortest = new HBox(10, vert1, vert2, getPath);
		shortest.setAlignment(Pos.CENTER);
		
		//Making a vbox to display
		VBox displayBox = new VBox(10, files, displayGraph, shortest, displayShortest, displayMST, displayMSTweight);
        displayBox.setAlignment(Pos.CENTER);
        
        //Setting the scene and adding it to the stage
        Scene scene = new Scene(displayBox, 800, 800);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Weighted Graph GUI");
        primaryStage.show();
		
	}
	
	
	public static void loadData(String fileName) {
		
		try(Scanner input = new Scanner(new File(fileName))) {;
			
		//initializing the weighted edge array list
			edges = new ArrayList<>();
			
			//Splitting the lines
			String[] data = input.nextLine().split(" ");
			//Getting the number of vertices
			int numberOfVertices = Integer.parseInt(data[0]);
			
			//while loop to go through the whole file
			while (input.hasNextLine()) {
				
				//Following your advice on how to split the edges from each other
				data = input.nextLine().split("[\\\\|]");
				
				//For loop to assign each part of the edge to a variable and then add it to the weighted edge array list
				for (String edge : data) {
					String[] addEdge = edge.trim().split(",");
                    int u = Integer.parseInt(addEdge[0].trim());
                    int v = Integer.parseInt(addEdge[1].trim());
                    double weight = Double.parseDouble(addEdge[2].trim());
                    edges.add(new WeightedEdge(u, v, weight)); 
				}
			}
			
			//Initialize weighted graph and use edges and num of verts constructor
			WGraph = new WeightedGraph(edges, numberOfVertices);
			
			//close the scanner
			input.close();
		}
		
		//error handling 
		catch(FileNotFoundException e) {
			System.out.println("File not found: " + e.getMessage());
		}
		
	};
	
	//method to set all the data that is called after file is selected
	public void setData() {
		
		//make the shortest path atributes visible
		getPath.setVisible(true);
		vert1.setVisible(true);
		vert2.setVisible(true);
		
		//setting the display graph label 
		displayGraph.setText("Weighted Graph\n" + "Number of Edges: " +WGraph.getSize()+ "\nEdges and Verticies:\n" +WGraph.printEdgesString());
		
		//creating a mst
		MST mst = WGraph.getMinimumSpanningTree(0);
		
		//displaying the mst
		displayMST.setText("\t\t\t\t\t\t\tMinimum Spanning Tree\n" + mst.printTree());
		
		//displaying the total weight
		displayMSTweight.setText("Total Weight: " + String.valueOf(mst.getTotalWeight()));
		
		//making two variable and assigning them the vert1 and vert2 values (shortest path vertices)
		int source = Integer.parseInt(vert1.getText());
		int destination = Integer.parseInt(vert2.getText());
		
		//Create a shortest path tree object
	    ShortestPathTree shortestPath = WGraph.getShortestPath(source);
	    List<WeightedEdge> pathEdges = shortestPath.getPath(destination);
	    
	    //Get the shortest path between the two vertices and store in a stringbuilder
	    if (pathEdges == null) {
	        displayShortest.setText("No path found from vertex " + source + " to vertex " + destination);
	    } 
	    else {
	    	StringBuilder sb = new StringBuilder();
	        sb.append("Shortest path from vertex " + source + " to " + destination + " is: ");
	        for (Object edge : pathEdges) {
	            sb.append("\t" + edge);
	        }
	        //set the text to the stringbuilder
	        displayShortest.setText(sb.toString());
	    }
		
	}

}
