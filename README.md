# RecursiveLearn

> **An offline Windows desktop application for solving and visualizing recursive sequences**  
> Designed for Discrete Mathematics students • Built with Python & PySide6

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![PySide6](https://img.shields.io/badge/PySide6-6.6.0-green.svg)](https://pypi.org/project/PySide6/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)]()

---

## 🌟 Overview

**RecursiveLearn** is a comprehensive educational tool that helps students master recursive relations and sequences through interactive lessons, step-by-step problem solving, and beautiful visualizations. Everything works offline with no internet connection required.

### ✨ Key Highlights

- 📘 **3 Complete Interactive Lessons** with real-world examples
- 🧮 **Powerful Solver** supporting homogeneous & non-homogeneous relations
- 📊 **Dynamic Visualizer** with high-quality plots
- 🧠 **Practice System** with 6+ exercises and instant feedback
- 🏆 **Gamification** with 15+ badges and scoring system
- 💾 **Export** solutions to PDF, DOCX, and PNG
- 🌙 **Light/Dark Mode** with modern, minimalistic design
- 👨‍🏫 **Instructor Mode** for teachers (PIN-protected)

---

## 🚀 Quick Start

### Windows (Recommended)

```batch
# 1. Install dependencies
install.bat

# 2. Run the application
run.bat
```

### Linux / macOS

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
./run.sh
# or: python3 main.py
```

### First Time Users

1. Start with **📘 Lessons** → Complete Lesson 1
2. Try **🧮 Solver** → Click "Fibonacci" example
3. Use **📊 Visualizer** → Plot a sequence
4. Practice with **🧠 Practice** → Solve beginner exercises

📖 **See [QUICKSTART.md](QUICKSTART.md) for a 3-minute guide**

---

## 🎯 Features

### 📚 Interactive Learning

**3 Complete Lesson Modules:**
1. Sequences and Recurrence Relations
2. Solving Linear Homogeneous Recurrence Relations
3. Applications of Recurrence Relations

Each lesson includes:
- ✓ Clear explanations and definitions
- ✓ Worked examples (Fibonacci, Tower of Hanoi, etc.)
- ✓ Real-world applications
- ✓ Self-assessment exercises
- ✓ Progress tracking (+100 points per lesson)

### 🧮 Powerful Solver

**Solve recurrence relations step-by-step:**

```
Input:  a_n = a_(n-1) + a_(n-2)
        Initial: 0:0, 1:1

Output: Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
        Closed form using golden ratio
        Step-by-step derivation
```

**Supported Types:**
- First-order: `a_n = c*a_(n-1) + k`
- Second-order homogeneous: `a_n = c1*a_(n-1) + c2*a_(n-2)`
- Non-homogeneous relations
- Custom initial conditions

**Export Options:**
- 📄 PDF (professional reports)
- 📝 DOCX (editable documents)
- 💾 JSON (local storage)

### 📊 Sequence Visualizer

**Create beautiful graphs:**
- Plot any sequence (5-100 terms)
- Customizable appearance (markers, grid, colors)
- High-resolution export (300 DPI)
- Interactive zooming and panning
- Point value annotations

**Example Visualizations:**
- Linear growth patterns
- Exponential sequences
- Fibonacci golden spiral
- Compound interest curves

### 🧠 Practice & Assessment

**Three Difficulty Levels:**
- 🟢 Beginner - Basic concepts
- 🟡 Intermediate - Complex relations
- 🔴 Advanced - Challenge problems

**Features:**
- Instant answer validation
- Multi-level hint system
- Progress tracking
- +50 points per correct exercise
- No penalty for hints!

### 🏆 Gamification

**15+ Achievement Badges:**
- 🎓 First Steps - Complete first lesson
- 📚 Lesson Master - Complete all lessons
- 🧮 Solver Expert - Solve 10 problems
- 💯 Century Club - Reach 100 points
- 🌟 High Achiever - Reach 500 points
- ...and more!

**Scoring System:**
- Complete lessons: +100 points
- Solve exercises: +50 points
- Track progress with visual progress bars

### 👨‍🏫 Instructor Mode

**PIN-protected features:**
- Add custom exercises
- View student progress
- Create custom quizzes
- Manage lesson content
- Export progress reports

Default PIN: `1234` (customizable in settings)

### ⚙️ Customization

**Appearance:**
- 🌙 Light/Dark mode toggle
- Font size adjustment (10-20px)
- Graph color schemes
- Accent color customization

**Solver Options:**
- Step-by-step solution display
- Auto-save functionality
- Export format preferences

---

## 📋 Requirements

### System Requirements

- **OS**: Windows 10+, Linux, macOS
- **Python**: 3.8 or higher
- **RAM**: 512 MB minimum
- **Disk**: 100 MB for application + data
- **Display**: 1024x768 minimum (1920x1080 recommended)

### Python Dependencies

```
PySide6==6.6.0          # Modern GUI framework
matplotlib==3.8.2       # Graph plotting
numpy==1.26.2           # Numerical operations
sympy==1.12             # Symbolic mathematics
fpdf2==2.7.6           # PDF export
python-docx==1.1.0     # DOCX export
pillow==10.1.0         # Image handling
```

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [README.md](README.md) | This file - Quick overview |
| [QUICKSTART.md](QUICKSTART.md) | 3-minute getting started guide |
| [USER_GUIDE.md](USER_GUIDE.md) | Comprehensive user manual |
| [EXAMPLES.md](EXAMPLES.md) | 15+ example problems to try |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Technical overview |

---

## 🎓 Educational Content

### Real-World Applications

**Compound Interest:**
```
Problem: $10,000 at 7% annual interest
Relation: a_n = 1.07*a_(n-1), a_0 = 10000
Result: Year 10 = $19,671.51
```

**Tower of Hanoi:**
```
Problem: Minimum moves for n disks
Relation: a_n = 2*a_(n-1) + 1, a_1 = 1
Result: n disks = 2^n - 1 moves
```

**Number of Subsets:**
```
Problem: Subsets of n-element set
Relation: a_n = 2*a_(n-1), a_0 = 1
Result: 2^n subsets
```

### Topics Covered

1. **Sequences**: Definition, notation, types
2. **Recurrence Relations**: Formulation and examples
3. **Solving Methods**: Characteristic equation, iteration
4. **Closed Forms**: Explicit formulas
5. **Applications**: CS, biology, economics, finance

---

## 🖥️ Screenshots

### Main Interface
```
┌────────────────────────────────────────────────┐
│  📚 RecursiveLearn                             │
│  Master Recursive Sequences                    │
├──────────────┬─────────────────────────────────┤
│ 📘 Lessons   │  [Lesson Content Display]       │
│ 🧮 Solver    │                                 │
│ 📊 Visualizer│  • Rich text formatting         │
│ 🧠 Practice  │  • Interactive examples         │
│ ⚙️ Settings  │  • Step-by-step solutions       │
│              │  • Beautiful graphs              │
│ 🏆 Score: 350│                                 │
│ 🎖️ Badges: 5 │                                 │
└──────────────┴─────────────────────────────────┘
```

---

## 💾 Data Storage

**All data stored locally:**

```
Windows: C:\Users\<YourName>\Documents\RecursiveLearn_Data\
Linux:   ~/Documents/RecursiveLearn_Data/
macOS:   ~/Documents/RecursiveLearn_Data/

├── progress.json              # User progress
├── settings.json              # App settings
├── custom_exercises.json      # Instructor content
├── saved_problems/            # Saved solutions
│   ├── solution_1.json
│   └── solution_2.json
└── exports/                   # Exported files
    ├── solution.pdf
    └── graph.png
```

**Privacy:** No internet connection, no data collection, 100% offline

---

## 🧪 Testing

Run the test suite to verify solver functionality:

```bash
python test_solver.py
```

**Tests included:**
- ✓ Simple linear recurrence
- ✓ Fibonacci sequence
- ✓ Geometric sequence
- ✓ Compound interest
- ✓ Second-order homogeneous

---

## 🛠️ Troubleshooting

### Common Issues

**App won't start:**
```bash
# Verify Python installation
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Solver errors:**
- Check syntax: Use `a_(n-1)` not `a_n-1`
- Verify initial conditions format: `0:5, 1:10`
- Try example problems first

**Export fails:**
- Verify write permissions to Documents folder
- Close any open exported files
- Check available disk space

**Graph not displaying:**
- Ensure matplotlib is installed
- Try reducing number of terms
- Check for valid numeric sequences

📖 See [USER_GUIDE.md](USER_GUIDE.md) for detailed troubleshooting

---

## 🎯 Use Cases

### For Students
- Learn recurrence relations interactively
- Solve homework problems step-by-step
- Visualize sequence behavior
- Practice for exams
- Build intuition with real examples

### For Teachers
- Demonstrate concepts in class
- Create custom exercises
- Track student progress
- Generate problem sets
- Export teaching materials

### For Self-Learners
- Master discrete mathematics
- Explore patterns and sequences
- Understand algorithm complexity
- Learn at your own pace
- Earn achievements

---

## 📊 Project Statistics

- **Lines of Code**: 3,000+
- **Python Files**: 14
- **UI Panels**: 5 major panels
- **Lessons**: 3 complete modules
- **Exercises**: 6+ practice problems
- **Badges**: 15 achievements
- **Export Formats**: 3 (PDF, DOCX, PNG)
- **Themes**: 2 (Light, Dark)

---

## 🤝 Contributing

This is an educational project. Suggestions and improvements welcome!

**Ideas for contributions:**
- Additional lesson content
- More example problems
- New badge achievements
- UI/UX improvements
- Bug fixes and optimizations

---

## 📜 License

**Educational Use License**

This software is free for educational purposes. Use in classroom settings, self-study, and academic institutions is encouraged.

---

## 🙏 Acknowledgments

Built for Discrete Mathematics education with focus on:
- Student engagement through gamification
- Conceptual understanding via visualization
- Practical application with real examples
- Self-directed learning with instant feedback

**Powered by:**
- Python 3.8+
- PySide6 (Qt for Python)
- SymPy (Symbolic Mathematics)
- Matplotlib (Scientific Plotting)

---

## 📞 Support

**Documentation:**
- [Quick Start Guide](QUICKSTART.md) - Get started in 3 minutes
- [User Guide](USER_GUIDE.md) - Comprehensive manual
- [Examples](EXAMPLES.md) - 15+ problem examples

**Resources:**
- Test Suite: `python test_solver.py`
- Example Problems: See EXAMPLES.md
- Project Details: See PROJECT_SUMMARY.md

---

## 🎓 Learn More

**Discrete Mathematics Topics:**
- Sequences and Series
- Recurrence Relations
- Difference Equations
- Generating Functions
- Algorithm Analysis

**Related Concepts:**
- Fibonacci Numbers
- Golden Ratio
- Compound Interest
- Dynamic Programming
- Recursive Algorithms

---

<div align="center">

**RecursiveLearn**  
*Master Recursive Sequences Through Interactive Learning*

🎓 Educational • 💻 Offline • 🎨 Modern • 🚀 Powerful

[Get Started](#-quick-start) • [Documentation](#-documentation) • [Examples](EXAMPLES.md)

Made with ❤️ for Discrete Mathematics students

</div>

## 📚 Usage

### For Students

1. **Learn**: Navigate through interactive lessons in the Lessons tab
2. **Solve**: Use the Solver to compute recurrence relations step-by-step
3. **Visualize**: Plot sequences and analyze patterns
4. **Practice**: Complete exercises and self-assessment quizzes
5. **Track Progress**: Earn badges and see your achievements

### For Instructors

1. Access Instructor Mode from Settings (default PIN: 1234)
2. Add custom exercises and quizzes
3. View student progress summaries

## 🎓 Educational Content

Based on the module "Recursive Relations":
- Lesson 1: Sequences and Recurrence Relations
- Lesson 2: Solving Linear Homogeneous Recurrence Relations
- Lesson 3: Applications of Recurrence Relations

## 🔧 Technical Details

- **GUI Framework**: PySide6 (Qt for Python)
- **Plotting**: Matplotlib
- **Mathematics**: SymPy for symbolic computation
- **Data Storage**: Local JSON files in Documents/RecursiveLearn_Data/
- **Export**: FPDF2 for PDF, python-docx for Word documents

## 📁 Data Storage

All data is stored locally in:
- Windows: `C:\Users\<YourUsername>\Documents\RecursiveLearn_Data\`
- Linux/Mac: `~/Documents/RecursiveLearn_Data/`

Files include:
- `progress.json`: User progress and scores
- `settings.json`: Application settings
- `custom_exercises.json`: Custom instructor exercises

## 🎨 Customization

- Toggle Light/Dark mode in Settings
- Customize graph colors and themes
- Adjust font sizes for accessibility

## 📝 License

Educational use - Free and open source

## 👨‍💻 Author

Created for Discrete Mathematics education
