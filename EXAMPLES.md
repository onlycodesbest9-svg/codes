# RecursiveLearn - Example Problems

This document contains example problems you can try in RecursiveLearn.

## 📝 Beginner Problems

### 1. Simple Arithmetic Sequence

**Recurrence Relation:** `a_n = a_(n-1) + 3`  
**Initial Condition:** `0:1`

**Expected Result:**
- Closed form: `a_n = 1 + 3n`
- Sequence: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, ...

**Try it:**
1. Go to Solver tab
2. Enter the relation and initial condition
3. Click "Solve"

---

### 2. Simple Geometric Sequence

**Recurrence Relation:** `a_n = 2*a_(n-1)`  
**Initial Condition:** `0:1`

**Expected Result:**
- Closed form: `a_n = 2^n`
- Sequence: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, ...

**Application:** Powers of 2, binary trees, computer memory

---

### 3. Constant Sequence

**Recurrence Relation:** `a_n = a_(n-1)`  
**Initial Condition:** `0:5`

**Expected Result:**
- Closed form: `a_n = 5`
- Sequence: 5, 5, 5, 5, 5, 5, ...

**Application:** Steady-state systems

---

## 🎯 Intermediate Problems

### 4. Fibonacci Sequence

**Recurrence Relation:** `a_n = a_(n-1) + a_(n-2)`  
**Initial Conditions:** `0:0, 1:1`

**Expected Result:**
- Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
- Closed form: `a_n = (φⁿ - ψⁿ)/√5` where φ = (1+√5)/2

**Application:** Nature patterns, golden ratio, algorithm analysis

---

### 5. Lucas Numbers

**Recurrence Relation:** `a_n = a_(n-1) + a_(n-2)`  
**Initial Conditions:** `0:2, 1:1`

**Expected Result:**
- Sequence: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, ...

**Application:** Related to Fibonacci, appears in combinatorics

---

### 6. Tribonacci Sequence

**Recurrence Relation:** `a_n = a_(n-1) + a_(n-2) + a_(n-3)`  
**Initial Conditions:** `0:0, 1:0, 2:1`

**Expected Result:**
- Sequence: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...

**Application:** Extension of Fibonacci to three terms

---

## 🔥 Advanced Problems

### 7. Second-Order Homogeneous

**Recurrence Relation:** `a_n = 3*a_(n-1) - 2*a_(n-2)`  
**Initial Conditions:** `0:1, 1:4`

**Expected Result:**
- Characteristic equation: r² - 3r + 2 = 0
- Roots: r₁ = 1, r₂ = 2
- Closed form: `a_n = -2 + 3·2ⁿ`
- Sequence: 1, 4, 10, 22, 46, 94, 190, 382, ...

---

### 8. Second-Order with Different Coefficients

**Recurrence Relation:** `a_n = 5*a_(n-1) - 6*a_(n-2)`  
**Initial Conditions:** `0:1, 1:2`

**Expected Result:**
- Characteristic equation: r² - 5r + 6 = 0
- Roots: r₁ = 2, r₂ = 3
- Sequence: 1, 2, 4, 8, 16, 32, ...

---

### 9. Third-Order Recurrence

**Recurrence Relation:** `a_n = a_(n-1) + a_(n-2) + a_(n-3)`  
**Initial Conditions:** `0:1, 1:1, 2:1`

**Expected Result:**
- Sequence: 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, ...

---

## 🌍 Real-World Applications

### 10. Compound Interest (7% annually)

**Problem:** You invest $10,000 at 7% annual interest, compounded yearly. How much will you have after n years?

**Recurrence Relation:** `a_n = 1.07*a_(n-1)`  
**Initial Condition:** `0:10000`

**Expected Result:**
- Year 0: $10,000
- Year 1: $10,700
- Year 2: $11,449
- Year 3: $12,250
- Year 4: $13,108
- Year 5: $14,026

**Closed form:** `a_n = 10000 × 1.07ⁿ`

---

### 11. Population Growth (5% per year)

**Problem:** A city has 100,000 people and grows by 5% annually.

**Recurrence Relation:** `a_n = 1.05*a_(n-1)`  
**Initial Condition:** `0:100000`

**Expected Result:**
- Year 0: 100,000
- Year 5: 127,628
- Year 10: 162,889
- Year 20: 265,330

---

### 12. Tower of Hanoi

**Problem:** Minimum moves to solve Tower of Hanoi with n disks.

**Recurrence Relation:** `a_n = 2*a_(n-1) + 1`  
**Initial Condition:** `1:1`

**Expected Result:**
- 1 disk: 1 move
- 2 disks: 3 moves
- 3 disks: 7 moves
- 4 disks: 15 moves
- 5 disks: 31 moves
- n disks: 2ⁿ - 1 moves

---

### 13. Number of Subsets

**Problem:** How many subsets does a set with n elements have?

**Recurrence Relation:** `a_n = 2*a_(n-1)`  
**Initial Condition:** `0:1`

**Expected Result:**
- 0 elements: 1 subset (empty set)
- 1 element: 2 subsets
- 2 elements: 4 subsets
- 3 elements: 8 subsets
- n elements: 2ⁿ subsets

**Closed form:** `a_n = 2ⁿ`

---

### 14. Binary Tree Nodes

**Problem:** How many nodes in a perfect binary tree of depth n?

**Recurrence Relation:** `a_n = 2*a_(n-1) + 1`  
**Initial Condition:** `0:1`

**Expected Result:**
- Depth 0: 1 node
- Depth 1: 3 nodes
- Depth 2: 7 nodes
- Depth 3: 15 nodes
- Depth n: 2ⁿ⁺¹ - 1 nodes

---

### 15. Savings Account

**Problem:** You save $100 monthly with 0.5% monthly interest.

**Recurrence Relation:** `a_n = 1.005*a_(n-1) + 100`  
**Initial Condition:** `0:0`

**Expected Result:**
- Month 1: $100
- Month 2: $200.50
- Month 3: $301.50
- Month 12: $1,233.56 (approximately)

---

## 🎮 Practice Exercises

### Exercise Set A: Basic Arithmetic

1. `a_n = a_(n-1) + 2`, `0:0` → 0, 2, 4, 6, 8, ...
2. `a_n = a_(n-1) + 10`, `0:5` → 5, 15, 25, 35, ...
3. `a_n = a_(n-1) - 3`, `0:20` → 20, 17, 14, 11, ...

### Exercise Set B: Basic Geometric

4. `a_n = 3*a_(n-1)`, `0:1` → 1, 3, 9, 27, 81, ...
5. `a_n = 0.5*a_(n-1)`, `0:100` → 100, 50, 25, 12.5, ...
6. `a_n = -2*a_(n-1)`, `0:1` → 1, -2, 4, -8, 16, ...

### Exercise Set C: Fibonacci Variations

7. Even Fibonacci: Start with `0:0, 1:2`
8. Odd Fibonacci: Start with `0:1, 1:1`
9. Modified: `a_n = 2*a_(n-1) + a_(n-2)`, `0:0, 1:1`

---

## 💡 Tips for Solving

1. **Identify the Type**
   - First-order: Only uses `a_(n-1)`
   - Second-order: Uses `a_(n-1)` and `a_(n-2)`
   - Homogeneous: No constant term
   - Non-homogeneous: Has a constant term

2. **Check Your Syntax**
   - Use parentheses: `a_(n-1)` not `a_n-1`
   - Use asterisks: `3*a_(n-1)` not `3a_(n-1)`
   - Use colons: `0:5` not `a_0=5` (unless using long format)

3. **Verify Results**
   - Compute first few terms manually
   - Check if pattern makes sense
   - Use visualizer to see growth

4. **Real-World Context**
   - Arithmetic → Linear growth (adding constant)
   - Geometric → Exponential growth (multiplying constant)
   - Fibonacci-like → Complex patterns

---

## 🚀 Challenge Problems

Try these in RecursiveLearn:

1. **Double Previous Plus Index**
   - `a_n = 2*a_(n-1) + n`, `0:1`

2. **Alternating Signs**
   - `a_n = -a_(n-1) + 1`, `0:0`

3. **Pell Numbers**
   - `a_n = 2*a_(n-1) + a_(n-2)`, `0:0, 1:1`
   - Result: 0, 1, 2, 5, 12, 29, 70, ...

4. **Custom Challenge**
   - Create your own relation and predict the pattern!

---

## 📊 Visualization Ideas

Try plotting these to see interesting patterns:

1. **Linear vs Exponential**
   - Plot `a_n = a_(n-1) + 5` vs `a_n = 1.5*a_(n-1)`
   - Compare growth rates

2. **Fibonacci Growth**
   - Plot Fibonacci sequence
   - See exponential growth (golden ratio)

3. **Oscillating Sequence**
   - Plot `a_n = -a_(n-1)`, `0:1`
   - See alternating pattern

4. **Compound Interest Over Time**
   - Plot `a_n = 1.05*a_(n-1)`, `0:10000`
   - Visualize investment growth

---

**Ready to try these?**

Open RecursiveLearn and start exploring! 🎓✨
