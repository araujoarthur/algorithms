# binarysearch_int

A binary search is a top performant algorithm to find an element in an ordered list. It takes place by comparing the target with the one in the middle position and, if it's lower than the target, increases the floor, if it's higher, decreases the ceil.

The calculation used in binarysearch_int to find the middle element is a bit tricky to understand, but it starts (and is mathematically equivalent) to the one just in sight: $c = (up + bottom)/2$. As they are loosely related, we are able to rewrite $up$ in terms of &bottom& as: $bottom - bottom + up$. Then, if we rewrite $c$ to $c = up/2 + bottom/2$ and use our new $up$ definiton, we get to: $(up + bottom - bottom)/2 + bottom/2$, the only logical term to use in order to remove the external $bottom/2$ is $+bottom/2$, otherwise we would end with the same expression we started. So we reach to $(up-bottom)/2 + bottom = c$.

The divisions aren't explicilty truncated because it's a property of integer division.

# To-Do
## C
- [X] Binary Search for integer.
- [ ] Binary Search for ``char*`` type.