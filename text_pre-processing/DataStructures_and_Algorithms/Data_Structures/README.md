# Data Structures


1. **Stacks**
* Real world example: “Stack of plates”
* All insertions and deletions are made at 1 end (the top)
* `LIFO` (last in —> first out)
* Common stack operations
  * Push 
  * Pop
  * Peek
  * Is_empty

* Applications of The Stack
  * **NLP most common use case: Reversing Strings!**
  * Reverse Polish notation for evaluating arithmetic expressions 
  * Syntax parsing
  * Cold stack: space for parameters and local variables is created
  * Used in recursion 
  * Undo and redo operations in word processors 
  * Low level assembly programming

* Python implementation 
  * Usually best to use a class to represent a stack 
  * When building smaller applications you can just use a LIST 
    * HOWEVER, Lists are mutable and anyone can easily insert, remove, pop methods. 
    * add item to top of stack: append()
    * retrieve item from top of stack: pop()
      * Both happen from the RIGHT 
