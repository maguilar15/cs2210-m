#### Define the problem/solution recursively (this is the most important step – if you don’t do this correctly, you will automatically get a 0 for the problem regardless of the code you write).

Define a pair of numbers. The number must always be smaller than the second number. If the number must always be smaller than the next one the list must be ordered.


#### Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem).

Using a matrix we can store solutions to sub-problems. Combining these results can be done by specifying the predicates in the problem. The pair *(c,d)* can follow another pair *(a,b)* if and only if b<c.
This is defined in the **if** statement inside the for loop. It is here where the sub-problems are combined. 

#### Talk about how you used IDEAL and Duke 7 to tackle the problem

