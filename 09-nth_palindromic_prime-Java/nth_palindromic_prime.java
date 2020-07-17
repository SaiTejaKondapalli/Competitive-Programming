// # Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
// # and returns the nth palindromic Prime, which is a palidrome number such that
// # it is also a prime. For example, 313 is a palindrome and it is prime
// # so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


class nth_palindromic_prime {
	private boolean isprime(int n) {
		int count = 0;
		for (int i = 1; i <= n; i++) {
			if (n % i == 0) {
				count += 1;
			}
		}
		if (count == 2) {
			return true;
		}
		return false;
	}
	private boolean ispalindrome(int n){
		int rev = 0;
		int temp = n;
		while (n > 0) {
			rev = rev * 10 + n % 10;
			n /= 10;
		}
		if(rev == temp) {
			return true;
		}
		return false;
	}
	public int fun_nth_palindromic_prime(int n){
		int count = 0;
		int i = 0;
		while (true) {
			if(isprime(n) && ispalindrome(n)){
				if(count == n){
					return i;
				}
				count += 1;
			}
			i += 1;
		}
	}
}