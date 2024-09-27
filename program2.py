def decode_message(s: str, p: str) -> bool:
    # Initialize a DP table with dimensions (len(s)+1) x (len(p)+1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Fill in the first row (when s is empty)
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the rest of the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # '?' matches any single character, or characters must match exactly
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[len(s)][len(p)]
