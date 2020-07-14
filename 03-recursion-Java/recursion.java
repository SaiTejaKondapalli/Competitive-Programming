class recursion {
	public int get_fib(int value) {
		if (value <= 1) {
			return value;
		}
		return get_fib(value - 1) + get_fib(value - 2);
	}
	public static void main(String[] args) {
	}
}