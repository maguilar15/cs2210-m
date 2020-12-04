#### Define the problem/solution recursively (this is the most important step – if you don’t do this correctly, you will automatically get a 0 for the problem regardless of the code you write).

The problem states to find an arithmetic slice that consists of a minimum of three elements.
These three elements will share a difference between any two consecutive elements in the same.
The problem specifies a domain for how an arithmetic slice should behave.
Therefore, the recursive step will be a variable called **res** that will be updated.  

#### Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem).

I am going to store the result in a variable **p**. This variable will store the solutions to the sub-problems. 
Ultimately combining them inside the nested while loop. 

#### Talk about how you used IDEAL and Duke 7 to tackle the problem.                                      
