This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].





def solution(A):

    a=max(A)
    b=min(A)
    if b>1 or a<1:
        return 1
        
    c=[i for i in A if i>0]       #get all positive integers
    c=list(set(c))                #remove duplicates
    c.sort()                      #ascending sort 
    d=list(range(1,len(c)+1))     #get a new list [1,2,3]

  
    if c[0]>1:                    #eg c=[2,3,4]
        return 1
    elif c==d:                    #eg c=[1,2,3]
        return max(c)+1
    else:
        for n in range(1, 100001):    #eg c=[1,2,4]
            if n^c[n-1]!=0:
                return n
                break
