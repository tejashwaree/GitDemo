
public class LogicalOp {

	public static void main(String[] args) {
		int a = 12, b = 3, c = 4;
		if (a >= 30) {
			System.out.println("a is greater");
		} else if (b >= 12) {
			System.out.println("b is smaller");
		} else {
			System.out.println("wrong condition");
		}
		// logical op
		int t = -1;
		int s = 12;
		if ((t <= s) && (t >= 0)) {
			System.out.println("match");
		} else if ((t >= s) || (t >= 0)) {
			System.out.println("correct");
		} else {
			System.out.println("missmatch");
		}
	}

}
