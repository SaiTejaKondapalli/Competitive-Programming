// median(a) (10 pts)
// Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value,
// which is the value of the middle element, or the average of the two middle elements if there is no single middle
// element. If the list is empty, return None.

public class Median {
	public int median(double[] list) {
		// Your code goes here
		int l = list.length;
		if (l == 0)
			return 0;
		else {
			if (l % 2 != 0) {
				return (int) list[l / 2];
			}
			return (int) (list[l / 2 - 1] + list[l / 2]) / 2;
		}
	}
	public static void main(String[] args) {

	}
}