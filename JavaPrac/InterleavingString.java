/*
Given strings s1, s2, and s3, find whether s3 is formed
by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration
where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is
s1 + t1 + s2 + t2 + s3 + t3 + ... or
t1 + s1 + t2 + s2 + t3 + s3 + ...
Note:
a + b is the concatenation of strings a and b.
s1 or t1 could be any lenth.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: s1 = aa + bc + c; s2 = dbbc + a
 */


class InterleavingString {
    //Memoization
    public boolean memoization(String s1, String s2, String s3) {
        if(s1.length() + s2.length() != s3.length())
            return false;
        return solution(s1, s2, s3, 0, 0, new Boolean[s1.length() + 1][s2.length() + 1]);
    }

    private boolean solution(String s1, String s2, String s3, int i, int j, Boolean[][] dp) {
	  if(i == s1.length() && j == s2.length())
		  return true;

	  if(dp[i][j] != null)
		  return dp[i][j];

	  if(i < s1.length() && s1.charAt(i) == s3.charAt(i + j)) {
		  boolean poss = solution(s1, s2, s3, i + 1, j, dp);
		  if(poss) {
			  dp[i][j] = true;
			  return true;
		  }
	  }

	  if(j < s2.length() && s2.charAt(j) == s3.charAt(i + j)) {
		  boolean poss = solution(s1, s2, s3, i, j + 1, dp);
		  if(poss) {
			  dp[i][j] = true;
			  return true;
		  }
	  }

	  dp[i][j] = false;
	  return false;
   }

    //Tabulation
     public boolean tabulation(String s1, String s2, String s3) {
          if(s1.length() + s2.length() != s3.length())
              return false;
          boolean[][] dp = new boolean[s1.length() + 1][s2.length() + 1];
          for(int i = 0; i < dp.length; i++) {
              for(int j = 0; j < dp[0].length; j++) {
                  if(i == 0 && j == 0)
                      dp[i][j] = true;
                  else if(i == 0) {
                      if(s2.charAt(j - 1) == s3.charAt(j - 1))
                          dp[i][j] = dp[i][j - 1];
                      else
                          dp[i][j] = false;
                  }else if(j == 0) {
                      if(s1.charAt(i - 1) == s3.charAt(i - 1))
                          dp[i][j] = dp[i - 1][j];
                      else
                          dp[i][j] = false;
                  }else {
                      if(s1.charAt(i - 1) == s3.charAt(i + j - 1))
                          dp[i][j] = dp[i-1][j];
                      if(s2.charAt(j - 1) == s3.charAt(i + j - 1))
                          dp[i][j] = (dp[i][j] || dp[i][j-1]);
                  }
              }
          }
          return dp[s1.length()][s2.length()];
    }

    public static void main(String[] args) {
        InterleavingString ils = new InterleavingString();
        System.out.println(ils.memoization("ab", "ab", "aabb"));
        System.out.println(ils.tabulation("ab", "ab", "ababc"));
    }
}
