# Dungeon Numbers
[Dungeon numbers](https://www.youtube.com/watch?v=xNx3JxRhnZE) are numbers that arise when we interpret a subscript $a_b$ as meaning $a$ in base $b$ and then make a long chain of sub-subscripts. This repository contains a basic implementation of dungeon numbers. 

The function `dungeonNumber()` may either be called with a sequence of numbers, as in `dungeonNumber(10, 11, 12, 13, 14, 15)` (meaning $10_{11_{12_{13_{14_{15}}}}}$), or it may be called by first defining `set = [10, 11, 12, 13, 14, 15]` and then calling `dungeonNumber(set)`. 

The sequences computed in the Numberphile and as the output of this script are as follows: 
![various dungeon number sequences](output_sequences.png)