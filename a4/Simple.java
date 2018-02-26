import java.util.Scanner;

public class Simple
{
    public static void main(String[] args) {
		Scanner S= new Scanner(System.in);
		int N = Integer.parseInt(S.nextLine());
		long[] vals = new long[N];
		int match = 0;
		for(int i = 0; i < N; i+= 1) vals[i] = Long.parseLong(S.nextLine());

		for (int i = 0; i < N; i++) {// i goes through {0, ..., N-1}
			for (int j = i+1; j < N; j++) {
				for (int k = j+1; k < N; k++) {
					for (int l = k+1; l < N; l++) {
						if (vals[i] + vals[j] + vals[k] + vals[l] == 0) {
                                match++;
	                        }
					}
				}
			}
		}
		if (match == 0) {
			System.out.print("False \n");
		} else {
			System.out.print("True \n");
		}
    }
}
