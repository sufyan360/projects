//Sufyan Chaudhry
//4-29-23
//Was with provided source code
//Extends Edge class and creates a WeightedEdge to accomodate for the Weight
package application;

public class WeightedEdge extends Edge

implements Comparable<WeightedEdge> {
public double weight; // The weight on edge (u, v)

/** Create a weighted edge on (u, v) */
public WeightedEdge(int u, int v, double weight) {
super(u, v);
this.weight = weight;
}

@Override /** Compare two edges on weights */
public int compareTo(WeightedEdge edge) {
if (weight > edge.weight) {
  return 1;
}
else if (weight == edge.weight) {
  return 0;
}
else {
  return -1;
}
}
}
