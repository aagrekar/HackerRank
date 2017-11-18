**Problem Statement**

You are filling a matrix by following a set of rules. Given a square matrix of size nxn, where (0,0) is its upper-left cell and 
(n-1,n-1) is its bottom-right cell, fill all the cells according to the following rules:

Value of  is defined recursively as follows:

if i=0 and j=0 then a[i][j] = m
else if i=j then a[i][j] = a[i-1][j-1] + k
else if i>j then a[i][j] = a[i-1][j] - 1
else, if i<j, then a[i][j] = a[i][j-1] - 1
In other words, given integers m and k, the matrix is filled by putting m in the upper-left cell, and then every other cell (i,i) 
on the main diagonal of the matrix is filled with the value a[i-1][j-1] + k. Remaining cells of the matrix are filled according 
to the two other recursive rules defined above.

For example, for n=4, m=3, k=1, the matrix will be:-

3 2 1 0

2 4 3 2

1 3 5 4

0 2 4 6

The task is to print the matrix after all its cells are filled with values.

**Input Format:**

In the first and only line of the input, there are 3 space-separated integers n, m, and k, where n is the size of the matrix and 
both m and k denote values used in the recursive definition in the statement.

**Output Format:**

Output the matrix with exactly n lines. 

In the ith line, print n space-separated integers denoting the ith row of the matrix with all cells filled with appropriate values.

**Sample Input 0**

5 10 7

**Sample Output 0**

10 9 8 7 6

9 17 16 15 14

8 16 24 23 22

7 15 23 31 30

6 14 22 30 38

**Explanation 0**

See the color-coded illustration below for the right answer:

![alt text](https://s3.amazonaws.com/hr-assets/0/1497406658-98851a5913-Capture.PNG)

**Sample Input 1**

6 5 2

**Sample Output 1**

5 4 3 2 1 0

4 7 6 5 4 3

3 6 9 8 7 6

2 5 8 11 10 9

1 4 7 10 13 12

0 3 6 9 12 15

**Explanation 1**

See the color-coded illustration below for the right answer for the  matrix: 

![alt text](https://s3.amazonaws.com/hr-assets/0/1497406680-f599c1d0b2-Capture2.PNG)
