"""
Palindrome.py: Finds the longest palindromic subsequence within a string of
characters. This implementation is a Dynamic Programming algorithm. Once a
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
"""


def parse_file(file_name):
    """Reads the input file string and returns it as a list of characters."""
    input_file = open(file_name, 'r')
    line = input_file.readline()
    input_string = list(line)
    return input_string


def make_array(input_string):
    """Creates a 2-D array which shows which characters are in the palindrome.

    The array's columns represent the starting position in the substring and
    the rows represent the ending position in the string. The value stored in
    each cell is the length of the longest palindromic subsequence in that
    substring. Left and right cursors track from either end of the input string
    to identify matching characters.

    @Params: input_string - a char list containing the string to be searched
    @Returns: array - The created 2-D array
    """

    array = [[None] * len(input_string) for i in range(len(input_string))]
    for i in range(len(input_string)):
        array[i][i] = 1

    for i in range(len(input_string)):
        # String will never go backwards, so we don't need anything past [i][i]
        j = i - 1
        while j >= 0:
            p_length = 0
            right = i
            left = j
            last_added = j

            while right > last_added:
                while right > left:
                    if input_string[right] == input_string[left]:
                        p_length += 2
                        last_added = left
                        left += 1
                        right -= 1
                    # If they don't match, compare character closer to the
                    # end of the substring
                    else:
                        left += 1

                # This can only be true at end of calculation and means that the
                # palindrome is of odd length, so it includes the element right
                # and left both point to. Need to break here before left and
                # right values are updated, so following comparison remains true
                if right == left == last_added + 1:
                    break

                left = last_added + 1
                right -= 1

            # Palindrome of odd length
            if right == left:
                p_length += 1

            # If adding this element gave us a longer palindrome, then
            # store this palindrome's length
            if p_length > array[i-1][j]:
                array[i][j] = p_length
            else:
                array[i][j] = array[i-1][j]
            j -= 1

    return array


def backtrace(array, input_string):
    """Finds what characters compose the maximal palindromic subsequence.

    Traces backwards through the 2D Array, beginning at the bottom left corner.
    Identified palindromic characters are added to the middle of the output
    string. When current position = None, we have added all palindromic
    characters.

    @Params: array - the 2D array to be traced through, created by make_array
             input_string - the character list with the original input string
    @Returns: output - a list of characters containing the maximum palindrome
    """

    output = []
    i = len(array) - 1  # i iterates through rows, so we start at bottom row
    j = 0               # j iterates through columns, so we start at furthest left
    if array[i][j] == 1:
        output.insert(0, input_string[0])
        return output

    while True:
        # If curr value (palindrome length at this cell) == right value
        if array[i][j] == array[i][j+1]:
            j += 1
        # If curr value == up value
        elif array[i][j] == array[i-1][j]:
            i -= 1
        else:
            mid = len(output) // 2
            if array[i-1][j+1] is None:
                # If they're equal, then palindrome is odd length so we
                # insert the 1 middle element
                if i == j:
                    output.insert(mid, input_string[i])
                else:
                    output.insert(mid, input_string[i])
                    output.insert(mid + 1, input_string[j])
                break
            else:
                output.insert(mid, input_string[i])
                output.insert(mid + 1, input_string[j])
                i -= 1
                j += 1

    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()
    input_file = args.input_file

    input_string = parse_file(input_file)
    array = make_array(input_string)
    # For Debugging: Can easily print array's contents here
    for i in array:
       print(i)
    palindrome = backtrace(array, input_string)
    print("Longest palindrome is of length %d:" % len(palindrome))
    print(palindrome)


if __name__ == "__main__":
    import argparse
    main()
