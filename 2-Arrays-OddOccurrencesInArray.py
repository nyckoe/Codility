A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.



ref: https://codesays.com/2015/solution-to-odd-occurrences-in-array-by-codility/
    
XOR truth table
Input	Output
A	B
0	0	    0
0	1	    1
1	0	    1
1	1	    0

1. XOR is commutative, which means
X ^ Y = Y ^ X.
2. XOR is assiciative, i.e.,
X ^ (Y ^ Z) = (X ^ Y) ^ Z.
3. For the truth values, as in the article,
X ^ X = 0, 0 ^ X = X.

def solution(A):
    x = 0
    for i in A:   #[1,2,3,1,2]
        x ^= i    # 0 ^ 1 ^ 2 ^ 3 ^ 1 ^ 2 = 0 ^ (1 ^ 1) ^ (2 ^ 2) ^ 3 = 0 ^ 3 =3 

    return x
