import java.util.Scanner;

public class PrimeNum {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter any no. : ");
		int n = sc.nextInt();
		int count= 0, i=2;
		boolean isPrime = true;
		while(i<n){
			if(n%i==0) {
		
		isPrime= false;
		break;
		}
		i=i+1;
	   }
		if (isPrime==true) {
		System.out.println(n+ " is a prime no.");
		}
		else {
		System.out.println(n+ " is not a prime no.");
		}
		
	}

}
