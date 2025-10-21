# RecursiveLearn - Changelog

All notable changes to RecursiveLearn will be documented in this file.

---

## [1.1.0] - 2025 - UI/UX Enhancement Release

### 🎉 Added

- **Student/Instructor Mode Selection Dialog**
  - Beautiful startup dialog to choose user mode
  - Student mode for learners with full learning features
  - Instructor mode (PIN-protected) for teachers with management features
  - Mode indicator in sidebar showing current mode
  - Default PIN: 1234 (customizable)

### ✨ Improved

- **Text Readability**
  - Increased font sizes from 12px to 13-14px throughout app
  - Improved text color contrast (#333 → #212121)
  - Enhanced line height (1.4 → 1.8) for comfortable reading
  - Bold labels (font-weight 700) for better clarity
  - Larger headings (Title: 28px, Sections: 20px)
  
- **Lesson Content**
  - Better HTML rendering with improved spacing
  - Code blocks with light gray background
  - Clearer bullet points and lists
  - Enhanced heading hierarchy
  - Professional formatting

- **Input Fields**
  - Increased height to 45px (from 35-40px)
  - Larger text (14px)
  - Better padding for comfortable typing
  - Clearer placeholder text

- **Buttons**
  - All buttons now properly clickable
  - Minimum height of 40-45px for easier clicking
  - Hand cursor on hover for better UX
  - Fixed lambda closure issues
  - Better hover and pressed states
  - Clear visual feedback

- **Solver Panel**
  - Monospace font for solution display
  - Improved padding and spacing
  - Clearer result presentation
  - Better example button functionality

- **Visualizer Panel**
  - Improved input layout
  - Larger controls
  - Clear, bold labels
  - Fixed example button handlers

- **Practice Panel**
  - Question display with colored background
  - Better feedback display styling
  - Larger answer input field
  - Improved visual hierarchy

### 🔧 Fixed

- **Button Click Issues**
  - Fixed all navigation buttons not responding
  - Fixed example buttons in Solver panel
  - Fixed example buttons in Visualizer panel
  - Proper event handler closures
  - Correct variable capture in lambdas

- **Visual Feedback**
  - Added pointer cursor to all clickable elements
  - Better hover states
  - Clear active/checked states

- **Settings Panel**
  - Removed confusing "Access Instructor Mode" button
  - Now handled through startup mode selection
  - Clear mode-specific settings display
  - Better PIN management for instructors

### 🎨 Changed

- **Mode Selection**
  - Moved from settings to startup dialog
  - More intuitive and user-friendly
  - Clear distinction between modes
  - Beautiful card-based layout

- **Color Scheme**
  - Student mode: Blue theme (#2196F3)
  - Instructor mode: Orange theme (#FF9800)
  - Better semantic color usage

- **Typography**
  - Consistent font weights
  - Better size hierarchy
  - Improved readability scores

### 📚 Documentation

- Added UPDATE_NOTES.md with detailed improvements
- Added CHANGELOG.md (this file)
- Updated README.md with mode selection info
- Updated user experience documentation

---

## [1.0.0] - 2025 - Initial Release

### 🎉 Initial Features

- **Interactive Lesson System**
  - 3 complete lesson modules
  - Rich HTML content
  - Worked examples
  - Self-assessment exercises

- **Recursive Relation Solver**
  - Linear homogeneous relations
  - Non-homogeneous relations
  - Step-by-step solutions
  - Closed-form expressions
  - Characteristic equation method

- **Sequence Visualizer**
  - Matplotlib-based plotting
  - Customizable graphs
  - Export to PNG/PDF
  - High-resolution output

- **Practice Exercise System**
  - 6+ exercises
  - 3 difficulty levels
  - Instant feedback
  - Hint system
  - Progress tracking

- **Gamification**
  - 15+ achievement badges
  - Point-based scoring
  - Progress bars
  - Motivational popups

- **Export Functionality**
  - PDF export (professional format)
  - DOCX export (Word documents)
  - PNG export (graphs)
  - Local JSON storage

- **Settings & Customization**
  - Light/Dark themes
  - Font size adjustment
  - Graph color schemes
  - Auto-save option

- **Instructor Features**
  - PIN-protected access
  - Custom exercise creation
  - Student progress viewing

- **Real-World Examples**
  - Compound Interest
  - Tower of Hanoi
  - Number of Subsets
  - Population Growth

- **Complete Documentation**
  - README.md
  - QUICKSTART.md
  - USER_GUIDE.md
  - EXAMPLES.md
  - PROJECT_SUMMARY.md
  - FEATURES_CHECKLIST.md
  - DEPLOYMENT_GUIDE.md

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.1.0 | 2025 | UI/UX enhancements, mode selection, improved readability |
| 1.0.0 | 2025 | Initial release with all core features |

---

## Upcoming Features

### Planned for Future Releases

- [ ] More lesson modules (Generating Functions, etc.)
- [ ] Advanced solver (higher-order relations)
- [ ] 3D visualizations
- [ ] Animation of sequence growth
- [ ] Timed quizzes
- [ ] Performance analytics
- [ ] Export progress reports
- [ ] Multiple user profiles
- [ ] Custom themes

---

## How to Update

### From 1.0.0 to 1.1.0

1. **Pull latest changes** (if using git)
2. **No data migration needed** - all data compatible
3. **Restart application** - mode selection will appear
4. **Choose your mode** - Student or Instructor
5. **Continue learning!**

Your progress, settings, and saved problems are preserved.

---

## Feedback & Contributions

We welcome feedback and contributions!

**Report Issues:**
- Describe the problem clearly
- Include steps to reproduce
- Mention your Python version and OS

**Suggest Features:**
- Explain the use case
- Describe expected behavior
- Consider educational value

---

**RecursiveLearn** - Continuously improving mathematics education! 🎓✨
