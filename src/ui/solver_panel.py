"""Solver panel for RecursiveLearn."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QGroupBox, QCheckBox, QMessageBox,
    QFileDialog
)
from PySide6.QtCore import Qt

from ..core.recurrence_solver import solve_recurrence
from ..utils.export import PDFExporter, DOCXExporter
from ..utils.file_manager import FileManager


class SolverPanel(QWidget):
    """Panel for solving recurrence relations."""
    
    def __init__(self, file_manager: FileManager):
        super().__init__()
        
        self.file_manager = file_manager
        self.current_solution = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("🧮 Recurrence Relation Solver")
        title.setObjectName("titleLabel")
        layout.addWidget(title)
        
        # Input group
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout(input_group)
        
        # Relation input
        rel_label = QLabel("Recurrence Relation:")
        rel_label.setStyleSheet("font-weight: 600; margin-top: 5px;")
        input_layout.addWidget(rel_label)
        
        hint_label = QLabel("Example: a_n = a_(n-1) + 5  or  a_n = 3*a_(n-1) - 2*a_(n-2)")
        hint_label.setStyleSheet("font-size: 11px; color: #757575; margin-bottom: 5px;")
        input_layout.addWidget(hint_label)
        
        self.relation_input = QLineEdit()
        self.relation_input.setPlaceholderText("Enter recurrence relation...")
        self.relation_input.setMinimumHeight(40)
        input_layout.addWidget(self.relation_input)
        
        # Initial conditions
        init_label = QLabel("Initial Conditions:")
        init_label.setStyleSheet("font-weight: 600; margin-top: 15px;")
        input_layout.addWidget(init_label)
        
        init_hint = QLabel("Format: a_0 = 5, a_1 = 10  or  0:5, 1:10")
        init_hint.setStyleSheet("font-size: 11px; color: #757575; margin-bottom: 5px;")
        input_layout.addWidget(init_hint)
        
        self.initial_input = QLineEdit()
        self.initial_input.setPlaceholderText("Enter initial conditions...")
        self.initial_input.setMinimumHeight(40)
        input_layout.addWidget(self.initial_input)
        
        layout.addWidget(input_group)
        
        # Options
        options_layout = QHBoxLayout()
        
        self.show_steps_cb = QCheckBox("Show step-by-step solution")
        self.show_steps_cb.setChecked(True)
        options_layout.addWidget(self.show_steps_cb)
        
        options_layout.addStretch()
        
        # Solve button
        solve_btn = QPushButton("🔍 Solve")
        solve_btn.setMinimumSize(150, 45)
        solve_btn.clicked.connect(self.solve)
        options_layout.addWidget(solve_btn)
        
        layout.addLayout(options_layout)
        
        # Solution group
        solution_group = QGroupBox("Solution")
        solution_layout = QVBoxLayout(solution_group)
        
        self.solution_display = QTextEdit()
        self.solution_display.setReadOnly(True)
        self.solution_display.setMinimumHeight(300)
        solution_layout.addWidget(self.solution_display)
        
        layout.addWidget(solution_group)
        
        # Action buttons
        action_layout = QHBoxLayout()
        
        save_btn = QPushButton("💾 Save Solution")
        save_btn.clicked.connect(self.save_solution)
        action_layout.addWidget(save_btn)
        
        export_pdf_btn = QPushButton("📄 Export PDF")
        export_pdf_btn.clicked.connect(self.export_pdf)
        action_layout.addWidget(export_pdf_btn)
        
        export_docx_btn = QPushButton("📝 Export DOCX")
        export_docx_btn.clicked.connect(self.export_docx)
        action_layout.addWidget(export_docx_btn)
        
        action_layout.addStretch()
        
        clear_btn = QPushButton("🗑️ Clear")
        clear_btn.setObjectName("secondaryButton")
        clear_btn.clicked.connect(self.clear_inputs)
        action_layout.addWidget(clear_btn)
        
        layout.addLayout(action_layout)
        
        # Add example buttons
        example_layout = QHBoxLayout()
        example_label = QLabel("Quick Examples:")
        example_label.setStyleSheet("font-weight: 600;")
        example_layout.addWidget(example_label)
        
        examples = [
            ("Fibonacci", "a_n = a_(n-1) + a_(n-2)", "0:0, 1:1"),
            ("Simple Linear", "a_n = a_(n-1) + 5", "0:5"),
            ("Compound Interest", "a_n = 1.07*a_(n-1)", "0:10000")
        ]
        
        for name, relation, initial in examples:
            btn = QPushButton(name)
            btn.setObjectName("secondaryButton")
            btn.clicked.connect(lambda checked, r=relation, i=initial: self.load_example(r, i))
            example_layout.addWidget(btn)
        
        example_layout.addStretch()
        layout.addLayout(example_layout)
        
    def load_example(self, relation: str, initial: str):
        """Load an example problem."""
        self.relation_input.setText(relation)
        self.initial_input.setText(initial)
        
    def parse_initial_conditions(self, text: str) -> dict:
        """Parse initial conditions from text."""
        conditions = {}
        
        # Try both formats
        parts = text.replace(" ", "").split(",")
        
        for part in parts:
            if ":" in part:
                # Format: 0:5
                key, val = part.split(":")
                conditions[int(key)] = int(val)
            elif "=" in part:
                # Format: a_0=5
                key_part, val = part.split("=")
                key = key_part.replace("a_", "").replace("a", "")
                conditions[int(key)] = int(val)
        
        return conditions
        
    def solve(self):
        """Solve the recurrence relation."""
        relation = self.relation_input.text().strip()
        initial_text = self.initial_input.text().strip()
        
        if not relation or not initial_text:
            QMessageBox.warning(self, "Input Required", 
                              "Please enter both recurrence relation and initial conditions.")
            return
        
        try:
            initial_conditions = self.parse_initial_conditions(initial_text)
            
            if not initial_conditions:
                QMessageBox.warning(self, "Invalid Input",
                                  "Could not parse initial conditions. Use format: 0:5, 1:10")
                return
            
            # Solve
            result = solve_recurrence(relation, initial_conditions)
            
            if not result['success']:
                self.solution_display.setPlainText(
                    f"Error solving recurrence:\n\n{result.get('error', 'Unknown error')}"
                )
                return
            
            # Display solution
            self.current_solution = {
                'relation': relation,
                'initial_conditions': initial_conditions,
                'closed_form': result['closed_form'],
                'sequence': result['sequence'],
                'steps': result['steps'] if self.show_steps_cb.isChecked() else [],
                'is_homogeneous': result['is_homogeneous']
            }
            
            self.display_solution(result)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n\n{str(e)}")
            
    def display_solution(self, result):
        """Display the solution."""
        output = []
        
        output.append("=" * 60)
        output.append("SOLUTION")
        output.append("=" * 60)
        output.append("")
        
        output.append(f"Type: {'Homogeneous' if result['is_homogeneous'] else 'Non-homogeneous'}")
        output.append("")
        
        output.append("Closed-Form Solution:")
        output.append(f"  a_n = {result['closed_form']}")
        output.append("")
        
        output.append("First 20 Terms:")
        seq_str = ", ".join(str(x) for x in result['sequence'][:20])
        output.append(f"  {seq_str}")
        output.append("")
        
        if self.show_steps_cb.isChecked() and result.get('steps'):
            output.append("=" * 60)
            output.append("STEP-BY-STEP SOLUTION")
            output.append("=" * 60)
            output.append("")
            
            for step in result['steps']:
                output.append(step)
        
        self.solution_display.setPlainText("\n".join(output))
        
    def save_solution(self):
        """Save the current solution."""
        if not self.current_solution:
            QMessageBox.warning(self, "No Solution", "Please solve a problem first.")
            return
        
        name = f"solution_{self.current_solution['relation'][:20]}"
        self.file_manager.save_problem(name, self.current_solution)
        
        QMessageBox.information(self, "Saved", "Solution saved successfully!")
        
    def export_pdf(self):
        """Export solution to PDF."""
        if not self.current_solution:
            QMessageBox.warning(self, "No Solution", "Please solve a problem first.")
            return
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Export PDF", "solution.pdf", "PDF Files (*.pdf)"
        )
        
        if filename:
            exporter = PDFExporter()
            exporter.export_solution(self.current_solution, filename)
            QMessageBox.information(self, "Exported", f"PDF saved to:\n{filename}")
            
    def export_docx(self):
        """Export solution to DOCX."""
        if not self.current_solution:
            QMessageBox.warning(self, "No Solution", "Please solve a problem first.")
            return
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Export DOCX", "solution.docx", "Word Documents (*.docx)"
        )
        
        if filename:
            exporter = DOCXExporter()
            exporter.export_solution(self.current_solution, filename)
            QMessageBox.information(self, "Exported", f"Document saved to:\n{filename}")
            
    def clear_inputs(self):
        """Clear all inputs."""
        self.relation_input.clear()
        self.initial_input.clear()
        self.solution_display.clear()
        self.current_solution = None
