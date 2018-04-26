# HackerRank
** Problem Statement **
At the Intergalactic Space Race, spaceships from across the galaxy compete to determine which ship is the fastest. To score the race,
the Intergalactic Space Race Association (ISRA) uses the following algorithm:

** Each spaceship S is given a score equal to the number of other spaceships that both started after and finished before S.**

Note that lower scores indicate a faster ship. The ISRA likes this system because it doesn't penalise fast ships that were slowed down 
because they were stuck behind a slow spaceship. Additionally, the algorithm doesn't reward fast spaceships who passed many slow competitors
in comparison to fast spaceships who race when there are not so many slow competitors on the track to pass.

The ISRA has hired you to implement the scoring algorithm. Given the log of spaceships with their start and end times, your task is to output
the score for each spaceship.

** Input Format **
The first line of input will contain the number of spaceships competing. After that, there will be one line per spaceship, in the following format.

spaceshipId startTime endTime

** Notes on Input **