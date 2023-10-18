import java.util.ArrayList;

public class javademo {

	public static void main(String[] args) {
		int [] arr1 = {23, 45, 34, 78,48};
		for(int i =0; i<arr1.length;i++) {
			System.out.println(arr1[i]);
			}
		ArrayList<String> a = new ArrayList<String>();
		a.add("rahul");
		a.add("naina");
		a.add("teju");
		a.add("asha");
		System.out.println(a.get(1));
		for(int i =0; i<a.size();i++) {
			System.out.println(a.get(i));
			}
		for(String val : a) {
			System.out.println(val);
		}
	}

}
