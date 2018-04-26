# HackerRank
**Problem Statement**

At the Intergalactic Space Race, spaceships from across the galaxy compete to determine which ship is the fastest. To score the race,
the Intergalactic Space Race Association (ISRA) uses the following algorithm:

**Each spaceship S is given a score equal to the number of other spaceships that both started after and finished before S.**

Note that lower scores indicate a faster ship. The ISRA likes this system because it doesn't penalise fast ships that were slowed down 
because they were stuck behind a slow spaceship. Additionally, the algorithm doesn't reward fast spaceships who passed many slow competitors
in comparison to fast spaceships who race when there are not so many slow competitors on the track to pass.

The ISRA has hired you to implement the scoring algorithm. Given the log of spaceships with their start and end times, your task is to output
the score for each spaceship.

**Input Format**

The first line of input will contain the number of spaceships competing. After that, there will be one line per spaceship, in the following format.

spaceshipId startTime endTime

**Notes on Input**

-  The number of spaceships will be an integer from 0 to 70000.
- spaceshipId will be an integer in the range [0,10^9].
- startTime and endTime are both integers that satisfy 0 <= startTime < endTime <= 10^18.
- spaceshipId is distinct.
- start and end times (taken as whole) will not contain any duplicate elements. If a racer has a start time of x then no other start or end time will also equal x.
- The fields are space delimited.

**Output Format**

Given the input, your task is to output the score for each spaceshipId in the following format:

spaceshipId score

with score as defined above. The output lines should be sorted in ascending order of score with ties broken by sorting by spaceshipId, also in ascending order. The sorting can be accomplished with a simple sort at the end.

**Directions:**
Please design a solution that is o(n^2) (that is "little-o", i.e. strictly less than O(n^2)). Brute force solutions that are not o(n^2)
will not be fast enough and fail some of the harder test cases.

One way you may achieve o(n^2) time is to utilize a data structure with X buckets, where X is some number (perhaps some function of input size). Each of the buckets is initially empty and defined by a start and end time. Eventually, each bucket will contain spaceships whose start times fall between the bucket's start and end time. The bucket boundaries should be chosen such that the buckets will ultimately contain the same number of spaceships. With this framework, you can iterate over the spaceships in end time order and as you iterate over each spaceship, fill in the bucketed data structure such that you can use it to quickly count the number of competitors that finished before and started after that spaceship.

You may ignore the above hint and use a different algorithm if you prefer.

**Sample Input and Output**

Input:

5

2 100 200

3 110 190

4 105 145

1 90 150

5 102 198


Output:

3 0

4 0

1 1

5 2

2 3

Note that in the above example spaceship 3 has a score of 0 because no one starts after spaceship 3 (a drawback to this scoring system is the last spaceship always has a score of 0). Spaceship 4 also has a score of 0 because the only racer who starts after spaceship 4's start time (spaceship 3) has a later finish time. Spaceship 3 is listed ahead of spaceship 4 despite having a slower time because spaceship 3's id is lower. At the other end, spaceship 2 has a score of 3 because spaceships 3, 4 and 5 start after spaceship 2 and finish before spaceship 2 finished. 
