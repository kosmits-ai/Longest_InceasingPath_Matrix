# Longest Increasing Path in a Matrix

This project implements an efficient solution to the classic problem: **find the length of the longest increasing path in a matrix**, where movement is allowed **up, down, left, and right**, and each next value must be **strictly greater** than the previous one.

The algorithm uses **Depth-First Search (DFS)** with **memoization** to achieve optimal performance.

---

##  Features
- Efficient DFS + memoization approach  
- Clean and minimal Python implementation  
- Works for any matrix size  
- Returns the length of the longest valid path  

---

##  Algorithm Overview
1. Perform DFS from each cell  
2. Move only to neighbors with strictly greater values  
3. Cache results so each cell is computed once  
4. Track the global maximum path length 
