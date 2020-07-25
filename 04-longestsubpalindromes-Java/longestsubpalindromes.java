// # Write the function longestSubpalindrome(s), that takes a string s and returns
// the longest palindrome that occurs as consecutive characters (not just letters, but
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!")
// # returns "b-4-b". If there is a tie, return the lexicographically larger value --
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce")
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions,
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also,
// from the explanation above, we see that longestSubpalindrome("aba") is "aba",
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public String helper(String s,int begin,int end,int n){
		while(begin >= 0 && end <= n -1 && s.charAt(begin) == s.charAt(end)){
			begin--;
			end++;
		}
		return s.substring(begin+1,end);
	}
	public String fun_longestsubpalindromes(String s){
		if(s.length() == 1){
			return s;
		}
		int n = s.length();
		String res = s.substring(0,1);
		for(int i = 0;i < n;i++){
			String temp = helper(s,i,i,n);
			if(temp.length() > res.length()){
				res = new String(temp);
			}
			if(temp.length() == res.length()){
				if(temp.compareTo(res) > 0){
					res = new String(temp);
				}
			}
			temp = helper(s,i,i+1,n);
			if(temp.length() > res.length()){
				res = new String(temp);
			}
		}
		return res;
	}
}
