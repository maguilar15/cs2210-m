#### Define the problem/solution recursively (this is the most important step – if you don’t do this correctly, you will automatically get a 0 for the problem regardless of the code you write).

First let's define what a falling path is. A falling path is an element in the first row and is combined with one element from each row. 
The next row that is chosen has to be a column that is different from the previous one. 
Therefore, the problem must be solved with a matrix. 

#### Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem).

I initialized a matrix with a row, column length equal to the passed parameter in the function call. 
I then had to determine what is preceding column that will be accumulated in the sum that will be stored n the matrix.

#### Talk about how you used IDEAL and Duke 7 to tackle the problem

Started by reading the problem and comprehending what it is asking. I then knew I had to do an addition depending on a different column. This column has to be pre-determined before it can be computed. 

