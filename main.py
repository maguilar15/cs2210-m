from minimum_falling_path_sum.P1 import fallingPathSum
from palindromic_substrings.P2 import palindromicSubstring
from arithmetic_slices.P3 import arithmeticSlices
from maximum_length_of_pair_chair.P5 import longestChain
from integer_break.P6 import integerBreak
from perfect_squares.P8 import perfectSquares

if __name__ == "__main__":
    p1 = [[1,2,3],[4,5,6],[7,8,9]]
    a1 = fallingPathSum(p1)
    s1 = [[1, 2, 3], [5, 6, 8], [12, 13, 15]] == a1 
    print(f"Problem 1 : {a1}, passing: {s1}")

    p2 = "aaa"
    a2 = palindromicSubstring(p2)
    s2 = 6 == a2 
    print(f"Problem 2 : {a2}, passing: {s2}")

    p3 = [1,2,3,4]
    a3 = arithmeticSlices(p3)
    s3 = 3 == a3 
    print(f"Problem 3 : {a3}, passing: {s3}")

    p4 = ""
    a4 = ""
    s4 = False
    print(f"Problem 4 : {a3}, passing: {s4}")

    p5 = [[1,2],[2,3],[3,4]]
    a5 = longestChain(p5)
    s5 = 2 == a5 
    print(f"Problem 5 : {a5}, passing: {s5}")
    
    p6 = 10 
    a6 = integerBreak(p6)
    s6 = 36 == a6
    print(f"Problem 6 : {a6}, passing: {s6}")

    a7 = None
    s7 = False
    print(f"Problem 7 : {a7}, passing: {s7}")

    p8 = 12
    a8 = perfectSquares(p8)
    s8 = 3 == a8
    print(f"Problem 8 : {a8}, passing: {s8}")