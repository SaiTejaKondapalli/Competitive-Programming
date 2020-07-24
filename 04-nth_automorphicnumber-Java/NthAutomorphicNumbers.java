// nthAutomorphicNumbers(n) [20 pts]
// In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
// number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
// 76 and 890625 are all automorphic numbers.
public class NthAutomorphicNumbers {
	public boolean isautomorphic(int n){
		String s1 = Integer.toString(n);
		int l1 = s1.length();
		int sq = n * n;
		String s2 = Integer.toString(sq);
		int l2 = s2.length();
		String s3 = s2.substring(l2-l1);
		if(s1.equals(s3)){
			return true;
		}
		return false;
	}
	public long nthAutomorphicNumbers(int n) {
		// Your code goes here
		int i = 0;
		int count = 0;
		while(true){
			if(isautomorphic(i)){
				count += 1;
				if(count == n){
					return i;
				}
			}
			i += 1;
		}
	}
}