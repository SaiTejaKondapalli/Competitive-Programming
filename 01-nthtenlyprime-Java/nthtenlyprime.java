// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n
// # and returns the nth Additive Prime, which is a prime number such that
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class nthtenlyprime {
	public boolean isprime(int n){
		int count = 0;
		for(int i = 1;i <= n;i++){
			if(n % i == 0){
				count += 1;
			}
		}
		if(count == 2){
			return true;
		}
		return false;
	}

	public int sumofdigits(int n){
		int summ = 0;
		int rem = 0;
		while(n > 0){
			rem = n % 10;
			summ += rem;
			n = n / 10;
		}
		return summ;
	}
	public int fun_nthtenlyprime(int n){
		int i = 1;
		int count = 0;
		while(true){
			if(isprime(n) && sumofdigits(n) == 10){
				if(count == n){
					return i;
				}
				count += 1;
			}
			i += 1;
		}
	}
}