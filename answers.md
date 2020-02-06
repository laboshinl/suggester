1a. Briefly discuss your container, its computational complexity and its ability for its functionality to be extended. Why is sublinear performance important in this use case?
I've chosen a tree where each vertex represents a single character.
Whorst case complexity seems to be O(L) where L is lentgh of word.


1b. What alternative containers suggest themselves, and what are their relative disadvantages and advantages?

Obviously another possible implementation is hash table
- Already Optimized implementation
- More space-efficient
Cons:
- needs to calculate hash


2a. Suppose you are given somebody else’s implementation to test, but without the source code, what tests would you define?
First ones that came into my mind are:
Check basic functionality (like in example in pdf)
Try to run on empty dictionary
Try to run with an empty prefix
Try to add special characters


2b. How would you ensure an implementation that is robust in the user environment?
We should investigate more on possible errors, surround everything with try-catch, add checks and restrictions for input data

2c. How could the implementation be extended to predict the next word based on the previous words in the sentence? (Please design the interface and outline your approach, but there is no need to implement this)
I think that some kind of markov chain should be implemented to achieve it

3a. How could the implementation be altered to handle this new feature?
We can create a separate index containing all of phrase capital leters or beginnings of the words and suggest in that subtree

3b. Suggest (and optionally implement) an approach to allow the selected container to allow different rankings,
e.g. prioritising class names over local variable names. If the container structure has changed,
what implications would the approach have memory and computational efficiency?
