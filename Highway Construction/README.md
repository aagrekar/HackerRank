**Problem Statement**

You are planning the next FIFA World Cup and you are counting the number of highways that need to be built to connect the cities 
with the venue. Your country has 'n' cities and all cities lie on a single straight road called “Highway Road”. If you want to go 
from City 'x' to City 'y' (where x<= y), you need to go through cities 'x', 'x+1', 'x+2', ..., 'y-1', y.

The requirements for the highways are as follows:
* All games will be held in the nth city.
* New bidirectional roads, called "Super Highways", need to be built such that it is possible to visit the nth city from any other 
  city directly.

You also have the cost to fulfil the second condition. The engineering team knows that if the length of a Super Highway is 'l', then 
it will cost 'l^k', where 'k' is an integer constant.The length of Super Highway between city 'x' and 'y' is |x-y|

For this problem, you need to find only a rough estimation of the cost, hence, find Total Cost Modulo 1000000009.

**Input Format**

First line will contain a single positive integer  denoting the number of queries. Then for each case there will be two positive 
integers, n and k.

**Output Format**

For each case find the cost to build Super Highways such that it is possible to visit nth city from any other city directly. You have 
to print this value Modulo 1000000009.

**Sample Input 0**

1

4 2

**Sample Output 0**

13

**Explanation 0**

There are four cities. We need to build Super Highways that connect city 1 to city 4 and city 2 to city 4. No need to connect city 3 
with city 4 since they are adjacent on “Highway Road”. So cost is 

(4-1)^2 + (4-2)^2 = 3^2 + 2^2 = 13.
