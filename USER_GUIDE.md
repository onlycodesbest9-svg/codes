# RecursiveLearn User Guide

## Welcome to RecursiveLearn! 🎓

This comprehensive guide will help you master recursive sequences and recurrence relations.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Main Features](#main-features)
3. [Lessons Module](#lessons-module)
4. [Solver Module](#solver-module)
5. [Visualizer Module](#visualizer-module)
6. [Practice Exercises](#practice-exercises)
7. [Settings & Customization](#settings--customization)
8. [Tips & Tricks](#tips--tricks)

---

## Getting Started

### Installation

**Windows:**
1. Double-click `install.bat`
2. Wait for installation to complete
3. Double-click `run.bat` to launch

**Linux/Mac:**
```bash
pip install -r requirements.txt
./run.sh
```

### First Launch

When you first open RecursiveLearn, you'll see:
- **Sidebar Navigation** - Switch between different modules
- **Lessons Tab** - Start here to learn the basics
- **Progress Tracker** - View your score and badges

---

## Main Features

### 📘 Lessons

Interactive learning modules covering:
1. **Lesson 1**: Sequences and Recurrence Relations
   - What is a sequence?
   - Understanding recurrence relations
   - Real-world examples (compound interest, Tower of Hanoi)

2. **Lesson 2**: Solving Linear Homogeneous Recurrence Relations
   - Characteristic equation method
   - Finding closed-form solutions
   - Worked examples including Fibonacci

3. **Lesson 3**: Applications
   - Computer Science applications
   - Population growth models

### 🧮 Solver

Solve recurrence relations step-by-step:

**Supported Formats:**
- Simple: `a_n = a_(n-1) + 5`
- Second-order: `a_n = 3*a_(n-1) - 2*a_(n-2)`
- Fibonacci: `a_n = a_(n-1) + a_(n-2)`

**Initial Conditions:**
- Format 1: `a_0 = 5, a_1 = 10`
- Format 2: `0:5, 1:10`

**Features:**
- ✓ Step-by-step solutions
- ✓ Closed-form expressions
- ✓ First 20 sequence terms
- ✓ Export to PDF/DOCX

### 📊 Visualizer

Create beautiful graphs of sequences:

1. Enter recurrence relation
2. Set initial conditions
3. Choose number of terms (5-100)
4. Click "Plot Sequence"

**Customization:**
- Toggle markers on/off
- Show/hide grid
- Save plots as PNG or PDF

### 🧠 Practice

Test your knowledge:

- **Beginner** 🟢 - Basic concepts
- **Intermediate** 🟡 - More complex relations
- **Advanced** 🔴 - Challenging problems

**Features:**
- Instant feedback
- Hints available
- Progress tracking
- Score system (+50 points per exercise)

---

## Lessons Module

### How to Use

1. Click **📘 Lessons** in the sidebar
2. Select a lesson from the list
3. Read through each section
4. Click **Next** to progress
5. Mark complete when finished (+100 points)

### Tips

- 📝 Take notes as you read
- 🔍 Pay attention to worked examples
- ✅ Complete exercises after each lesson
- 🏆 Earn badges for completion

---

## Solver Module

### Step-by-Step Guide

#### Example 1: Simple Linear Relation

**Problem:** Find the sequence for `a_n = a_(n-1) + 5` with `a_0 = 5`

1. Enter relation: `a_n = a_(n-1) + 5`
2. Enter initial: `0:5`
3. Check "Show step-by-step solution"
4. Click **🔍 Solve**

**Result:**
```
Closed-form: a_n = 5n + 5
Sequence: 5, 10, 15, 20, 25, ...
```

#### Example 2: Fibonacci Sequence

**Problem:** Solve `a_n = a_(n-1) + a_(n-2)` with `a_0 = 0, a_1 = 1`

1. Enter relation: `a_n = a_(n-1) + a_(n-2)`
2. Enter initial: `0:0, 1:1`
3. Click **🔍 Solve**

**Result:**
```
Characteristic roots: (1+√5)/2, (1-√5)/2
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

### Exporting Solutions

After solving:

1. **💾 Save Solution** - Save to local storage
2. **📄 Export PDF** - Create professional PDF report
3. **📝 Export DOCX** - Export to Word document

---

## Visualizer Module

### Creating Plots

1. Navigate to **📊 Visualizer**
2. Enter recurrence relation
3. Set initial conditions
4. Adjust number of terms (default: 20)
5. Customize appearance:
   - Show markers: Plot points as dots
   - Show grid: Add background grid
6. Click **📈 Plot Sequence**

### Saving Plots

- **💾 Save Plot** - Export as PNG or PDF
- High resolution (300 DPI) for presentations

### Interpreting Graphs

**Linear Growth:**
```
a_n = a_(n-1) + c
→ Straight line
```

**Exponential Growth:**
```
a_n = r * a_(n-1)
→ Curved exponential
```

**Fibonacci Pattern:**
```
a_n = a_(n-1) + a_(n-2)
→ Exponential with golden ratio
```

---

## Practice Exercises

### Exercise Types

1. **Computation** - Calculate sequence terms
2. **Closed Form** - Find explicit formulas
3. **Applications** - Real-world problems

### How to Practice

1. Click **🧠 Practice**
2. Filter by difficulty (optional)
3. Select an exercise
4. Enter your answer
5. Click **✓ Check Answer**

### Using Hints

- Click **💡 Show Hint** for help
- Multiple hints available per problem
- No penalty for using hints!

### Scoring

- ✅ Correct answer: **+50 points**
- Exercise marked as complete
- Progress bar updates automatically

---

## Settings & Customization

### Appearance

**Theme:**
- Light Mode (default)
- Dark Mode

**Font Size:** 10-20 pixels

**Graph Colors:** Multiple color schemes

### Solver Options

- ✓ Show step-by-step solutions
- ✓ Auto-save solutions

### Instructor Mode

Access with PIN (default: `1234`):

1. Go to Settings
2. Click **🔓 Access Instructor Mode**
3. Enter PIN
4. Access custom exercises and progress tracking

### Data Management

**Location:** 
- Windows: `C:\Users\<You>\Documents\RecursiveLearn_Data\`
- Linux/Mac: `~/Documents/RecursiveLearn_Data/`

**Features:**
- 📁 Open Data Folder
- 🔄 Reset Progress (use with caution!)

---

## Tips & Tricks

### Learning Tips

1. **Start with Lessons** - Build foundation first
2. **Practice Regularly** - Consistency is key
3. **Use Visualizer** - See patterns visually
4. **Read Step-by-Step** - Understand the process

### Solver Tips

1. **Check Syntax** - Use underscores: `a_n`, `a_(n-1)`
2. **Parentheses** - Always use for terms: `a_(n-2)`, not `a_n-2`
3. **Multiplication** - Use `*` explicitly: `3*a_(n-1)`

### Common Mistakes

❌ `a_n = a_n-1 + 5` (missing parentheses)  
✅ `a_n = a_(n-1) + 5` (correct)

❌ `0=5, 1=10` (wrong separator)  
✅ `0:5, 1:10` (correct)

### Keyboard Shortcuts

- `Ctrl+S` - Save (in solver)
- `Ctrl+E` - Export PDF
- `F5` - Refresh current panel

---

## Badge System 🏆

Earn badges by completing challenges:

| Badge | Requirement |
|-------|------------|
| 🎓 First Steps | Complete first lesson |
| 📚 Lesson Master | Complete all lessons |
| 🔍 Problem Solver | Solve first problem |
| 🧮 Solver Expert | Solve 10 problems |
| 🏆 Practice Champion | Complete 10 exercises |
| 💯 Century Club | Reach 100 points |
| 🌟 High Achiever | Reach 500 points |

---

## Troubleshooting

### Application won't start

1. Check Python is installed: `python --version`
2. Verify dependencies: `pip install -r requirements.txt`
3. Check error messages in console

### Solver not working

1. Verify syntax of recurrence relation
2. Check initial conditions format
3. Try example problems first

### Graphs not displaying

1. Ensure matplotlib is installed
2. Check sequence has valid values
3. Try reducing number of terms

### Export fails

1. Verify write permissions
2. Check disk space
3. Close any open exported files

---

## Getting Help

### Resources

- README.md - Quick start guide
- This guide - Comprehensive documentation
- Example problems - Learn by doing

### Contact

For support or feedback:
- GitHub Issues (if applicable)
- Educational institution support

---

## Quick Reference

### Recurrence Relation Syntax

```
Basic:        a_n = a_(n-1) + c
Second-order: a_n = c1*a_(n-1) + c2*a_(n-2)
Fibonacci:    a_n = a_(n-1) + a_(n-2)
Geometric:    a_n = r*a_(n-1)
```

### Initial Conditions Syntax

```
Format 1: a_0 = 5, a_1 = 10
Format 2: 0:5, 1:10
```

### Common Relations

| Name | Relation | Initial | Closed Form |
|------|----------|---------|-------------|
| Arithmetic | a_n = a_(n-1) + d | a_0 = a | a_n = a + nd |
| Geometric | a_n = r*a_(n-1) | a_0 = a | a_n = a·r^n |
| Fibonacci | a_n = a_(n-1) + a_(n-2) | 0:0, 1:1 | Complex |
| Factorial | a_n = n*a_(n-1) | a_0 = 1 | a_n = n! |

---

## Appendix: Mathematical Notation

### Subscript Notation

- `aₙ` = nth term
- `aₙ₋₁` = previous term (n-1)
- `aₙ₋₂` = two terms back (n-2)

### Common Symbols

- `Σ` - Summation
- `∏` - Product
- `!` - Factorial
- `^` - Exponent

---

**Happy Learning! 🎉**

Master recursive sequences with RecursiveLearn and excel in Discrete Mathematics!
