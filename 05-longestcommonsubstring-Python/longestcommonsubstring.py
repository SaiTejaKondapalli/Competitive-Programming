# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    if len(s1) == 0 or len(s2) == 0:
        return ""
    if len(s1) > len(s2):
        str1 = s2
        str2 = s1
    else:
        str1 = s1
        str2 = s2
    res = str1[0]
    s = []
    for i in range(1,len(str1)):
        res += str1[i]
        if res in str2:
            s.append(res)
        else:
            res = str1[i]
    if len(s) == 0:
        return ""
    else:
        l = [x for x in s if len(x) == len(max(s, key=len))]
        print(l)
        return max(s,key = len)
