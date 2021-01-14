# Data Structures Essentials (zybook)

## Authors and contributors: 
Authors:
  - Roman Lysecky / Professor of Electrical and Computer Engineering / Univ. of Arizona
  - Frank Vahid / Professor of Computer Science and Engineering / Univ. of California, Riverside
  - Evan Olds / Content Developer / zyBooks
 
Senior Contributors:
  - Tony Givargis / Professor of Computer Science / Univ. of California, Irvine
  - Susan Lysecky / Senior Content Developer / zyBooks
  
Additional Contributors
  - Joe Hummel / University of Illinois at Chicago (Reviewer)
  
## Notes
### Basic data structures:
- Record: A record is the data structure that stores subitems, often called fields, with a name associated with each subitem.
- Array: An array is a data structure that stores an ordered list of items, where each item is directly accessible by a positional index.
- Linked list: A linked list is a data structure that stores an ordered list of items in nodes, where each node stores data and has a pointer to the next node.
- Binary tree: A binary tree is a data structure in which each node stores data and has up to two children, known as a left child and a right child.
- Hash table: A hash table is a data structure that stores unordered items by mapping (or hashing) each item to a location in an array.
- Heap: A max-heap is a tree that maintains the simple property that a node's key is greater than or equal to the node's childrens' keys. A min-heap is a tree that maintains the simple property that a node's key is less than or equal to the node's childrens' keys.
- Graph: A graph is a data structure for representing connections among items, and consists of vertices connected by edges. A vertex represents an item in a graph. An edge represents a connection between two vertices in a graph.

### Algorithms:
Algorithm efficiency is most commonly measured by the algorithm runtime, and an **efficient algorithm is one whose runtime increases no more than polynomially with respect to the input size**. However, some problems exist for which an efficient algorithm is unknown.
- NP-complete: problems are a set of problems for which no known efficient algorithm exists. NP-complete problems have the following characteristics:
  - No efficient algorithm has been found to solve an NP-complete problem.
  - No one has proven that an efficient algorithm to solve an NP-complete problem is impossible.
  - If an efficient algorithm exists for one NP-complete problem, then all NP-complete problem can be solved efficiently.
  
### Algorithms for data structures:
Data structures not only define how data is organized and stored, but also the operations performed on the data structure. While common operations include inserting, removing, and searching for data, the algorithms to implement those operations are typically specific to each data structure. Ex: Appending an item to a linked list requires a different algorithm than appending an item to an array.

### Abstract data types:
An abstract data type (ADT) is a data type described by predefined user operations, such as "insert data at rear," without indicating how each operation is implemented. An ADT can be implemented using different underlying data structures. However, a programmer need not have knowledge of the underlying implementation to use an ADT.\
Ex: A list is a common ADT for holding ordered data, having operations like append a data item, remove a data item, search whether a data item exists, and print the list. A list ADT is commonly implemented using arrays or linked list data structures.

- List: A list is an ADT for holding ordered data. (Array, linked list)
- Dynamic array: A dynamic array is an ADT for holding ordered data and allowing indexed access. (Array)
- Stack: A stack is an ADT in which items are only inserted on or removed from the top of a stack. (Linked list)
- Queue: A queue is an ADT in which items are inserted at the end of the queue and removed from the front of the queue. (Linked list)
- Deque: A deque (pronounced "deck" and short for double-ended queue) is an ADT in which items can be inserted and removed at both the front and back. (Linked list)
- Bag: A bag is an ADT for storing items in which the order does not matter and duplicate items are allowed. (Array, linked list)
- Set: A set is an ADT for a collection of distinct items. (Binary search tree, hash table)
- Priority queue: A priority queue is a queue where each item has a priority, and items with higher priority are closer to the front of the queue than items with lower priority. (Heap)
- Dictionary (Map): A dictionary is an ADT that associates (or maps) keys with values. (Hash table, binary search tree)

### Abstraction and optimization
Abstraction means to have a user interact with an item at a high-level, with lower-level internal details hidden from the user. ADTs support abstraction by hiding the underlying implementation details and providing a well-defined set of operations for using the ADT.

Using abstract data types enables programmers or algorithm designers to focus on higher-level operations and algorithms, thus improving programmer efficiency. However, knowledge of the underlying implementation is needed to analyze or improve the runtime efficiency.

### Runtime complexity, best case, and worst case
An algorithm's runtime complexity is a function, T(N), that represents the number of constant time operations performed by the algorithm on an input of size N. Runtime complexity is discussed in more detail elsewhere.

Because an algorithm's runtime may vary significantly based on the input data, a common approach is to identify best and worst case scenarios. An algorithm's best case is the scenario where the algorithm does the minimum possible number of operations. An algorithm's worst case is the scenario where the algorithm does the maximum possible number of operations.

### Space complexity

An algorithm's space complexity is a function, S(N), that represents the number of fixed-size memory units used by the algorithm for an input of size N. Ex: The space complexity of an algorithm that duplicates a list of numbers is S(N) = 2N + k, where k is a constant representing memory used for things like the loop counter and list pointers.

Space complexity includes the input data and additional memory allocated by the algorithm. An algorithm's auxiliary space complexity is the space complexity not including the input data. Ex: An algorithm to find the maximum number in a list will have a space complexity of S(N) = N + k, but an auxiliary space complexity of S(N) = k, where k is a constant.

### Linear Search and Binary Search
Linear search performe search one by one. Bineary search starts with the middle of a list, sorted from 0 to N. If the middle is 4.5, take 4. Puesdo code below:
```
BinarySearch(numbers, numbersSize, key) {
   mid = 0
   low = 0
   high = numbersSize - 1
   
   while (high >= low) {
      mid = (high + low) / 2
      if (numbers[mid] < key) {
         low = mid + 1
      }
      else if (numbers[mid] > key) {
         high = mid - 1
      }
      else {
         return mid
      }
   }
   
   return -1 // not found
}
```
### Binary search efficiency
Binary search is incredibly efficient in finding an element within a sorted list. During each iteration or step of the algorithm, binary search reduces the search space (i.e., the remaining elements to search within) by half. The search terminates when the element is found or the search space is empty (element not found). For a 32 element list, if the search key is not found, the search space is halved to have 16 elements, then 8, 4, 2, 1, and finally none, requiring only 6 steps. For an N element list, the maximum number of steps required to reduce the search space to an empty sublist is log_2(N)+1. (+1 is because you need to take the last step to reduce the last element to empty.) 

Example: reduce 32 elements to an empty list - max steps to min (only 5 steps):
* step 1: reduce from [0,31] to [0,14] by checking 15
* step 2: reduce from [0,14] to [0,6] by checking 7
* step 3: reduce from [0,6] to [0,2] by checking 3
* step 4: reduce from [0,2] to [0] by checking 1
* step 5: reduce from [0] to [] by checking 0

Example: reduce 32 elements to an empty list - max steps to max (6 steps):
* step 1: reduce from [0,31] to [16,31] by checking 15
* step 2: reduce from [16,31] to [22,31] by checking 23
* step 3: reduce from [22,31] to [28,31] by checking 27
* step 4: reduce from [28,31] to [30,31] by checking 29
* step 5: reduce from [30,31] to [31] by checking 30
* step 6: reduce from [31] to [] by checking 31

Because when it is 4.5 we take 4, it takes one step less to reduce to empty list when always searching the smaller sublist.

### Constant Time Algorithm
In practice, designing an efficient algorithm aims to lower the amount of time that an algorithm runs. However, a single algorithm can always execute more quickly on a faster processor. Therefore, the theoretical analysis of an algorithm describes runtime in terms of number of constant time operations, not nanoseconds. A constant time operation is an operation that, for a given processor, always operates in the same amount of time, regardless of input values.

#### Identifying constant time operations
The programming language being used, as well as the hardware running the code, both affect what is and what is not a constant time operation. Ex: Most modern processors perform arithmetic operations on integers and floating point values at a fixed rate that is unaffected by operand values. Part of the reason for this is that the floating point and integer values have a fixed size. Below summarizes operations that are generally considered constant time operations.
* Addition, subtraction, multiplication, and division of fixed size integer or floating point values.	
* Assignment of a reference, pointer, or other fixed size data value.	
* Comparison of two fixed size data values.	
* Read or write an array element at a particular index.	

Examples:

* Copying all characters in the string would require more operations for longer strings. But assignment of a pointer/reference is a constant time operation.
* Division is often slower than multiplication on many processors. But each division operation takes the same amount of time regardless of operand values, so is still a constant time operation.
* The hardware running the code is NOT the only thing that affects what is and what is not a constant time operation. The programming language also affects what is a constant time operation. Ex: A programming language could provide variable size floating point values as the only available numerical type and implement arithmetic operations in software. Since the values are not fixed size, arithmetic operations would not be constant time.

### Growth of functions and complexity
#### Upper and Lower Bounds
An algorithm with runtime complexity T(N) has a lower bound and an upper bound.

* Lower bound: A function f(N) that is ≤ the best case T(N), for all values of N ≥ 1.
* Upper bound: A function f(N) that is ≥ the worst case T(N), for all values of N ≥ 1.

Ex: An algorithm with best case runtime T(N) = 7N + 36 and worst case runtime T(N) = 3N^2 + 10N + 17, has a lower bound 7N and an upper bound 30N^2. 
These lower and upper bounds provide a general picture of the runtime, while using simpler functions than the exact runtime.

#### Growth rates and asymptotic notations
An additional simplification can factor out the constant from a bounding function, leaving a function that categorizes the algorithm's growth rate. Ex: Instead of saying that an algorithm's runtime function has an upper bound of 30N^2, the algorithm could be described as having a worst case growth rate of N^2. Asymptotic notation is the classification of runtime complexity that uses functions that indicate only the growth rate of a bounding function. Three asymptotic notations are commonly used in complexity analysis:

* O notation provides a growth rate for an algorithm's upper bound.
  T(N) = O(f(N)) where a positive constant c exits such that for all N>=1, T(N)<=c*f(N) 
* Ω notation provides a growth rate for an algorithm's lower bound.
  T(N) = Ω(f(N)) where a positive constant c exits such that for all N>=1, T(N)>=c*f(N) 
* Θ notation provides a growth rate that is both an upper and lower bound.
  T(N) = Θ(f(N)) where T(N) = O(f(N)) = Ω(f(N))


### Big O notation
Big O notation is a mathematical way of describing how a function (running time of an algorithm) generally behaves in relation to the input size. In Big O notation, all functions that have the same growth rate (as determined by the highest order term of the function) are characterized using the same Big O notation. In essence, all functions that have the same growth rate are considered equivalent in Big O notation.

Some examples:
* log_2(N) = O(log(N))The logarithm base does not affect the growth rate, so the base is omitted in Big O notation. Converting from one logarithm base to another base involves a constant factor, which can be simplified in Big O notation.
* 2 * O(3N) = O(N)
* O(3N^3) + O(N^2) = O(3N^3 + N^2) = O(N^3)

### Algorithm Analysis
#### Worse Case Algorithm Analysis
To analyze how runtime of an algorithm scales as the input size increases, we first determine how many operations the algorithm executes for a specific input size, N. Then, the big-O notation for that function is determined. Algorithm runtime analysis often focuses on the worst-case runtime complexity. The worst-case runtime of an algorithm is the runtime complexity for an input that results in the longest execution. Other runtime analyses include best-case runtime and average-case runtime. Determining the average-case runtime requires knowledge of the statistical properties of the expected data inputs.

### Analyzing the time complexity of recursive algorithms
#### Recurrence relations
The runtime complexity T(N) of a recursive function will have function T on both sides of the equation. Ex: Binary search performs constant time operations, then a recursive call that operates on half of the input, making the runtime complexity T(N) = O(1) + T(N / 2). Such a function is known as a recurrence relation: A function f(N) that is defined in terms of the same function operating on a value < N.

Using O-notation to express runtime complexity of a recursive function requires solving the recurrence relation. For simpler recursive functions such as binary search, runtime complexity can be determined by expressing the number of function calls as a function of N.

#### Recursion trees
The runtime complexity of any recursive function can be split into 2 parts: operations done directly by the function and operations done by recursive calls made by the function. Ex: For binary search's T(N) = O(1) + T(N / 2), O(1) represents operations directly done by the function and T(N / 2) represents operation done by a recursive call. A useful tool for solving recurrences is a recursion tree: A visual diagram of an operation done by a recursive function, that separates operations done directly by the function and operations done by recursive calls.

### Sorting Algorithm
Sorting is the process of converting a list of elements into ascending (or descending) order. For example, given a list of numbers (17, 3, 44, 6, 9), the list after sorting is (3, 6, 9, 17, 44). You may have carried out sorting when arranging papers in alphabetical order, or arranging envelopes to have ascending zip codes (as required for bulk mailings).

The challenge of sorting is that a program can't "see" the entire list to know where to move an element. Instead, a program is limited to simpler steps, typically observing or swapping just two elements at a time. So sorting just by swapping values is an important part of sorting algorithms.

#### Selection sort - runtime O(N^2)
Selection sort is a sorting algorithm that treats the input as two parts, a sorted part and an unsorted part, and repeatedly selects the proper next value to move from the unsorted part to the end of the sorted part.
```
for (i = 0; i < numbersSize - 1; ++i) {

   // Find index of smallest remaining element
   indexSmallest = i
   for (j = i + 1; j < numbersSize; ++j) {

      if (numbers[j] < numbers[indexSmallest]) {
         indexSmallest = j
      }
   }

   // Swap numbers[i] and numbers[indexSmallest]
   temp = numbers[i]
   numbers[i] = numbers[indexSmallest]
   numbers[indexSmallest] = temp
}
```

#### Insertion sort - runtime O(N^2)
Insertion sort is a sorting algorithm that treats the input as two parts, a sorted part and an unsorted part, and repeatedly inserts the next value from the unsorted part into the correct location in the sorted part.

The index variable i denotes the starting position of the current element in the unsorted part. Initially, the first element (i.e., element at index 0) is assumed to be sorted, so the outer for loop initializes i to 1. The inner while loop inserts the current element into the sorted part by repeatedly swapping the current element with the elements in the sorted part that are larger. Once a smaller or equal element is found in the sorted part, the current element has been inserted in the correct location and the while loop terminates.


```
for (i = 1; i < numbersSize; ++i) {
   j = i
   // Insert numbers[i] into sorted part
   // stopping once numbers[i] in correct position
   while (j > 0 && numbers[j] < numbers[j - 1]) {
       
      // Swap numbers[j] and numbers[j - 1]
      temp = numbers[j]
      numbers[j] = numbers[j - 1]
      numbers[j - 1] = temp
      --j
   }
}
```

Insertion sort's nearly sorted run time is O(N). For each outer loop execution, if the element is already in sorted position, only a single comparison is made. Each element not in sorted position requires at most N comparisons. If there are a constant number, C, of unsorted elements, sorting the N - C sorted elements requires one comparison each, and sorting the C unsorted elements requires at most N comparisons each. The runtime for nearly sorted inputs is O((N - C) * 1 + C * N) = O(N).


#### Shell sort's interleaved lists
Shell sort is a sorting algorithm that treats the input as a collection of interleaved lists, and sorts each list individually with a variant of the insertion sort algorithm. Shell sort uses gap values to determine the number of interleaved lists. A gap value is a positive integer representing the distance between elements in an interleaved list. For each interleaved list, if an element is at index i, the next element is at index i + gap value.

Shell sort begins by choosing a gap value K and sorting K interleaved lists in place. Shell sort finishes by performing a standard insertion sort on the entire array. Because the interleaved parts have already been sorted, smaller elements will be close to the array's beginning and larger elements towards the end. Insertion sort can then quickly sort the nearly-sorted array.

Any positive integer gap value can be chosen. In the case that the array size is not evenly divisible by the gap value, some interleaved lists will have fewer items than others.

##### Insertion sort for interleaved lists
If a gap value of K is chosen, creating K entirely new lists would be computationally expensive. Instead of creating new lists, shell sort sorts interleaved lists in-place with a variation of the insertion sort algorithm. The insertion sort algorithm variant redefines the concept of "next" and "previous" items. For an item at index X, the next item is at X + K, instead of X + 1, and the previous item is at X - K instead of X - 1.
```
InsertionSortInterleaved(numbers, numbersSize, startIndex, gap) {
   i = 0
   j = 0
   temp = 0  // Temporary variable for swap

   for (i = startIndex + gap; i < numbersSize; i = i + gap) {
      j = i
      while (j - gap >= startIndex && numbers[j] < numbers[j - gap]) {
         temp = numbers[j]
         numbers[j] = numbers[j - gap]
         numbers[j - gap] = temp
         j = j - gap
      }
   }
}
```
For list = [88, 67, 91, 45, 14, 68, 71, 26, 64], we need to call (list, 9, 0, 3), (list, 9, 1, 3), (list, 9, 2, 3) to sort interleaved lists, and then finally (list, 9, 0, 1) to sort the overall nearly sorted list.

##### Shell sort
Shell sort begins by picking an arbitrary collection of gap values. For each gap value K, K calls are made to the insertion sort variant function to sort K interleaved lists. Shell sort ends with a final gap value of 1, to finish with the regular insertion sort.

Shell sort tends to perform well when choosing gap values in descending order. A common option is to choose powers of 2 minus 1, in descending order. Ex: For an array of size 100, gap values would be 63, 31, 15, 7, 3, and 1. This gap selection technique results in shell sort's time complexity being no worse than O(N^(3/2)).

Using gap values that are powers of 2 or in descending order is not required. Shell sort will correctly sort arrays using any positive integer gap values in any order, provided a gap value of 1 is included.


#### Quick sort
Quicksort is a sorting algorithm that repeatedly partitions the input into low and high parts (each part unsorted), and then recursively sorts each of those parts. To partition the input, quicksort chooses a pivot to divide the data into low and high parts. The pivot can be any value within the array being sorted, commonly the value of the middle array element. Ex: For the list (4, 34, 10, 25, 1), the middle element is located at index 2 (the middle of indices [0, 4]) and has a value of 10.

Once the pivot is chosen, the quicksort algorithm divides the array into two parts, referred to as the low partition and the high partition. All values in the low partition are less than or equal to the pivot value. All values in the high partition are greater than or equal to the pivot value. The values in each partition are not necessarily sorted. Ex: Partitioning (4, 34, 10, 25, 1) with a pivot value of 10 results in a low partition of (4, 1, 10) and a high partition of (25, 34). Values equal to the pivot may appear in either or both of the partitions.

```

Partition(numbers, lowIndex, highIndex) {
   // Pick middle element as pivot
   midpoint = lowIndex + (highIndex - lowIndex) / 2
   pivot = numbers[midpoint]
 
   done = false
   while (!done) {
      // Increment lowIndex while numbers[lowIndex] < pivot
      while (numbers[lowIndex] < pivot) {
         lowIndex += 1
      }
    
      // Decrement highIndex while pivot < numbers[highIndex]
      while (pivot < numbers[highIndex]) {
         highIndex -= 1
      }
    
      // If zero or one elements remain, then all numbers are
      // partitioned. Return highIndex.
      if (lowIndex >= highIndex) {
         done = true
      }
      else {
         // Swap numbers[lowIndex] and numbers[highIndex]
         temp = numbers[lowIndex]
         numbers[lowIndex] = numbers[highIndex]
         numbers[highIndex] = temp
       
         // Update lowIndex and highIndex
         lowIndex += 1
         highIndex -= 1
      }
   }
 
   return highIndex
}
```

This partition algorithm above attempts to partition the data into two groups: a group greater than the middle element, and a group smaller or equal to the middle element. It does this checking for each elements from both sides. If a number is positioned to the left of the middle element and is smaller than the middle element, the number is at its correct location. If a number is positioned to the right of the middle element and is greater than the middle element, the number is also at its correct location. If they are not at their correct location, the while loops will stop and if lowIndex and HighIndex are still going on (which indicates the partition process did not end), the algorithm will swap these two numbers so they are at the right positions. 

The partitioning algorithm uses two index variables lowIndex and highIndex, initialized to the left and right sides of the current elements being sorted. As long as the value at index lowIndex is less than the pivot value, the algorithm increments lowIndex, because the element should remain in the low partition. Likewise, as long as the value at index highIndex is greater than the pivot value, the algorithm decrements highIndex, because the element should remain in the high partition. Then, if lowIndex >= highIndex, all elements have been partitioned, and the partitioning algorithm returns highIndex, which is the index of the last element in the low partition. Otherwise, the elements at indices lowIndex and highIndex are swapped to move those elements to the correct partitions. The algorithm then increments lowIndex, decrements highIndex, and repeats.

* The pivot value is the value of the middle element.
* lowIndex is incremented until a value greater than the pivot is found.
* highIndex is decremented until a value less than the pivot is found.
* Elements at indices lowIndex and highIndex are swapped, moving those elements to the correct partitions.
* The partition process repeats until indices lowIndex and highIndex reach or pass each other, indicating all elements have been partitioned.
* Once partitioned, the algorithm returns highIndex, which is the highest index of the low partition. The partitions are not yet sorted.


