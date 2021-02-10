import java.util.ArrayList;
import java.util.List;
import java.util.Random;


class BinarySearch {

	// Returns the desired positive integer or -1 if it's not found
	public static int search(List<Integer> list, int i) {
		return searchHelper(list, i, 0, list.size()-1);
	}

	// Returns the desired positive integer or -1 if it's not found
	private static int searchHelper(List<Integer> list, int i, int first, int last) {
		int size = last - first + 1;
		int middle = first + (size / 2);

		// BASE CASE 1: empty list
		if(size == 0) {
			return -1;
		}

		// BASE CASE 2: item found
		int item = list.get(middle);
		if(i == item)
			return item;
		
		// if i is smaller, go left
		if(i < item) return searchHelper(list, i, first, middle-1);

		// if i is bigger, go right
		return searchHelper(list, i, middle+1, last);
	}
	
	public static void main(String[] args) {
			ArrayList<Integer> list = generateSortedList(100);
			int needle = list.get(20);
			
			System.out.println(list);
			System.out.println("");
			System.out.println("RESULT");
			System.out.println("needle: " + needle);
			System.out.println("result: " + search(list, needle));

			
			return;
	}

	private static ArrayList<Integer> generateSortedList(int size) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		Random r = new Random();
		
		for(int i = 0; i < size; i++) {
			if(list.size() == 0) {
				list.add(r.nextInt(10));
			} else {
				list.add(list.get(list.size()-1) + r.nextInt(10));
			}
		}
		
		return list; 
	}
	
	
}
