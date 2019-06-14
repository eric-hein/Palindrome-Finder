# Palindrome-Finder
Finds longest palindromic subsequence within a string. A palindromic
subsequence does not have to be contiguous (e.g. ABCDBA contains a 
maximum palindrome of ABCBA).

This implementation is a Dynamic Programming algorithm. Once a
string is passed in from a file (.txt), a 2D array is created which stores
the length of the maximum palindrome within the substrings. Columns indicate
start position and rows indicate end position of the substring.

After the array is created, the array is traced back through to find which
characters are in that palindrome. The bottom left corner of the array will
always contain the maximum value, as it has start position of 0 and end
position = to max. Thus if an adjacent value to the up or right of the current
position equals the current value, then the current character is not in the
palindrome. If neither value is equal, then the matching palindromic characters
are added to the output string from each end of the input string.

At the end of execution, the maximum palindrome is printed out to the terminal.
