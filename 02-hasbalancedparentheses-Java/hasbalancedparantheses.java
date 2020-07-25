// # Write the function hasBalancedParentheses, which takes a string and returns True
// # if that code has balanced parentheses and False otherwise (ignoring all
// # 	non-parentheses in the string). We say that parentheses are balanced if each
// # right parenthesis closes (matches) an open (unmatched) left parenthesis,
// # and no left parentheses are left unclosed (unmatched) at the end of the text.
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) ("
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as
// # you iterate over the string.


class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){
		if(s.length() == 0){
			return true;
		}
		int l = 0;
		int r = 0;
		for(int i = 0;i < s.length();i++){
			if(s.charAt(i)=='('){
				l += 1;
			}
			else{
				if(s.charAt(i) == ')'){
					r += 1;
				}
			}
		}
		if(l == r){
			return true;
		}
		return false;
	}
}
