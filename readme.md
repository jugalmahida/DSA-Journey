# Hello, I am Jugal Mahida

Today is 29/11/2025 11:29AM, i started my dsa journey with Udemy Course & MasterJI App (Indian Version of Leetcode with very specific Challenges & Problems)

# Steps to construct an algorithm

1. Understand the problem definition
2. Choose the technique (Two Pointers, DP, Greedy, Divider & Conquer and many more !)
3. Dry Run (Draw Flow Chat)
4. Testing the algorithm
5. Implementation (Coding Time!)
6. Analysis of your solution (Best Time & Space complexity)

## Additional note of me

- Start the timer when program is start with technique name for better understanding
- It will showing the start time & end time for the choosing the best technique for the problem

# Big O Notation

- O(1) = Code will runs only onces, this is also called as Constant Time complexity.
- O(log n) = In every iteration problem array size will divide by 2, means 1000 -> 500 -> 250 -> 125 ..., Eg Binary Search in shorted order, Reach array's half index then check the result would be left or right, if result would be in left then go in left side then check result would left or right repeat this process util the result not found.
- O(n) = Code will runs n times means if n = 5 then code will runs 5 times. Eg Linear Search.
- O(n ^ 2) = Code will runs n ^ 2 times if n = 5 then code will runs 5 ^ 2 -> 25 times. Name of this - Quadratic complexity
- O(n ^ 3) = Code will runs n ^ 3 times if n = 5 then code will runs 5 ^ 3 -> 125 times. Name of this - Cubic complexity
- O(n ^ c) = Where c (Constant & c > 0) is 2 & n is 20 then Code will runs 20 ^ 2 -> 400 times . Name of this - Polynomial complexity
- O(c ^ n) = opposite of above complexity. Name of this - Exponential complexity
- n! < n ^ n & 2 ^ n < n! < n ^ n

# Array - DS

- Array is stored in a continuous in memory
- When array reaches its size then new array comes in picture with size previous_array \* 2 with all old elements are copy into new array.
- This concept follows in this programming languages Python (lists), JavaScript (arrays), Java (ArrayList) Java has both support Static & Dynamic, C++ (vector)
  C# (List), Ruby (arrays)
- Array operation like `insert`, `remove`, `get`, `count` , `pop` with take O(n) time complexity.
- Find memory address formula :- \
  arr(i) = Base Address + (i - LowerBound of an index) \* size of an element in bytes
- Base Address is first array element's memory address
- i - Given index
- LowerBound - means where array current position by default it will be 0 but if where at 2th index and find 6th index memory address then Lower Bound will be 2

## Multidimensional Array

- This type of array will be stored in memory in 2 types.
- Consider this array to understand.\
  [\
   &nbsp; [96,32,4], \
   &nbsp; [4,8,2], \
   &nbsp; [9,7,3] \
  ]

1. Row Major - Where all element will be stored in memory in row wise [96,32,4,4,8,2,9,7,3]
2. Column Major - Where all element will be stored in memory in column wise [96,4,9,32,8,7,4,2,3]

- Find memory address of given index in row major array ( arr[i][j] ) :- \
  Base Address + [ ( i - LBR) * Number_of_Columns + ( j - LBC ) ] \* size of an element in bytes
- Find memory address of given index in column major array ( arr[i][j] ) :- \
  Base Address + [ ( j - LBC) * Number_of_Rows + ( i - LBR ) ] \* size of an element in bytes
- i - given row index
- LBR - Lower Bound of Row position
- Number Of columns present in array
- j - given column index
- LBC - Lower Bound of Column position