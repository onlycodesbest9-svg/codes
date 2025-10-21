"""Visualizer panel for RecursiveLearn."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QGroupBox, QSpinBox, QCheckBox, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from ..core.recurrence_solver import compute_sequence


class VisualizerPanel(QWidget):
    """Panel for visualizing sequences."""
    
    def __init__(self):
        super().__init__()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("📊 Sequence Visualizer")
        title.setObjectName("titleLabel")
        layout.addWidget(title)
        
        # Input group
        input_group = QGroupBox("Sequence Parameters")
        input_layout = QVBoxLayout(input_group)
        
        # Row 1: Relation
        rel_layout = QHBoxLayout()
        rel_label = QLabel("Recurrence Relation:")
        rel_label.setMinimumWidth(150)
        rel_label.setStyleSheet("font-weight: 700; font-size: 13px; color: #212121;")
        self.relation_input = QLineEdit()
        self.relation_input.setPlaceholderText("e.g., a_n = a_(n-1) + 5")
        self.relation_input.setMinimumHeight(40)
        self.relation_input.setStyleSheet("font-size: 14px; padding: 8px;")
        rel_layout.addWidget(rel_label)
        rel_layout.addWidget(self.relation_input)
        input_layout.addLayout(rel_layout)
        
        # Row 2: Initial conditions
        init_layout = QHBoxLayout()
        init_label = QLabel("Initial Conditions:")
        init_label.setMinimumWidth(150)
        init_label.setStyleSheet("font-weight: 700; font-size: 13px; color: #212121;")
        self.initial_input = QLineEdit()
        self.initial_input.setPlaceholderText("e.g., 0:5, 1:10")
        self.initial_input.setMinimumHeight(40)
        self.initial_input.setStyleSheet("font-size: 14px; padding: 8px;")
        init_layout.addWidget(init_label)
        init_layout.addWidget(self.initial_input)
        input_layout.addLayout(init_layout)
        
        # Row 3: Number of terms
        terms_layout = QHBoxLayout()
        terms_label = QLabel("Number of Terms:")
        terms_label.setMinimumWidth(150)
        terms_label.setStyleSheet("font-weight: 700; font-size: 13px; color: #212121;")
        self.terms_spin = QSpinBox()
        self.terms_spin.setMinimum(5)
        self.terms_spin.setMaximum(100)
        self.terms_spin.setValue(20)
        self.terms_spin.setMinimumHeight(40)
        self.terms_spin.setStyleSheet("font-size: 14px; padding: 5px;")
        terms_layout.addWidget(terms_label)
        terms_layout.addWidget(self.terms_spin)
        terms_layout.addStretch()
        input_layout.addLayout(terms_layout)
        
        layout.addWidget(input_group)
        
        # Options
        options_layout = QHBoxLayout()
        
        self.show_markers_cb = QCheckBox("Show markers")
        self.show_markers_cb.setChecked(True)
        options_layout.addWidget(self.show_markers_cb)
        
        self.show_grid_cb = QCheckBox("Show grid")
        self.show_grid_cb.setChecked(True)
        options_layout.addWidget(self.show_grid_cb)
        
        options_layout.addStretch()
        
        plot_btn = QPushButton("📈 Plot Sequence")
        plot_btn.setMinimumSize(150, 40)
        plot_btn.clicked.connect(self.plot_sequence)
        options_layout.addWidget(plot_btn)
        
        layout.addLayout(options_layout)
        
        # Matplotlib canvas
        self.figure = Figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumHeight(400)
        layout.addWidget(self.canvas)
        
        # Action buttons
        action_layout = QHBoxLayout()
        
        save_btn = QPushButton("💾 Save Plot")
        save_btn.clicked.connect(self.save_plot)
        action_layout.addWidget(save_btn)
        
        action_layout.addStretch()
        
        clear_btn = QPushButton("🗑️ Clear")
        clear_btn.setObjectName("secondaryButton")
        clear_btn.clicked.connect(self.clear_plot)
        action_layout.addWidget(clear_btn)
        
        layout.addLayout(action_layout)
        
        # Example buttons
        example_layout = QHBoxLayout()
        example_label = QLabel("Quick Examples:")
        example_label.setStyleSheet("font-weight: 600;")
        example_layout.addWidget(example_label)
        
        examples = [
            ("Linear Growth", "a_n = a_(n-1) + 3", "0:1"),
            ("Exponential", "a_n = 2*a_(n-1)", "0:1"),
            ("Fibonacci", "a_n = a_(n-1) + a_(n-2)", "0:0, 1:1")
        ]
        
        for name, relation, initial in examples:
            btn = QPushButton(name)
            btn.setObjectName("secondaryButton")
            btn.setMinimumHeight(38)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            # Use default arguments to capture values correctly
            def make_example_handler(rel, init):
                return lambda: self.load_example(rel, init)
            btn.clicked.connect(make_example_handler(relation, initial))
            example_layout.addWidget(btn)
        
        example_layout.addStretch()
        layout.addLayout(example_layout)
        
    def load_example(self, relation: str, initial: str):
        """Load an example."""
        self.relation_input.setText(relation)
        self.initial_input.setText(initial)
        
    def parse_initial_conditions(self, text: str) -> dict:
        """Parse initial conditions."""
        conditions = {}
        parts = text.replace(" ", "").split(",")
        
        for part in parts:
            if ":" in part:
                key, val = part.split(":")
                conditions[int(key)] = int(val)
        
        return conditions
        
    def plot_sequence(self):
        """Plot the sequence."""
        relation = self.relation_input.text().strip()
        initial_text = self.initial_input.text().strip()
        
        if not relation or not initial_text:
            QMessageBox.warning(self, "Input Required",
                              "Please enter recurrence relation and initial conditions.")
            return
        
        try:
            initial_conditions = self.parse_initial_conditions(initial_text)
            n_terms = self.terms_spin.value()
            
            # Compute sequence
            sequence = compute_sequence(relation, initial_conditions, n_terms)
            
            if not sequence:
                QMessageBox.warning(self, "Error", "Could not compute sequence.")
                return
            
            # Plot
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            
            n_values = list(range(len(sequence)))
            
            if self.show_markers_cb.isChecked():
                ax.plot(n_values, sequence, 'bo-', linewidth=2, markersize=8, label='aₙ')
            else:
                ax.plot(n_values, sequence, 'b-', linewidth=2, label='aₙ')
            
            ax.set_xlabel('n', fontsize=12, fontweight='bold')
            ax.set_ylabel('a_n', fontsize=12, fontweight='bold')
            ax.set_title(f'Sequence: {relation}', fontsize=14, fontweight='bold')
            
            if self.show_grid_cb.isChecked():
                ax.grid(True, alpha=0.3, linestyle='--')
            
            ax.legend(fontsize=11)
            
            # Annotate a few points
            for i in range(0, min(5, len(sequence))):
                ax.annotate(f'{sequence[i]}',
                           xy=(i, sequence[i]),
                           xytext=(5, 5),
                           textcoords='offset points',
                           fontsize=9,
                           alpha=0.7)
            
            self.figure.tight_layout()
            self.canvas.draw()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Plotting error:\n\n{str(e)}")
            
    def save_plot(self):
        """Save the current plot."""
        from PySide6.QtWidgets import QFileDialog
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Plot", "sequence_plot.png",
            "PNG Files (*.png);;PDF Files (*.pdf);;All Files (*)"
        )
        
        if filename:
            self.figure.savefig(filename, dpi=300, bbox_inches='tight')
            QMessageBox.information(self, "Saved", f"Plot saved to:\n{filename}")
            
    def clear_plot(self):
        """Clear the plot."""
        self.figure.clear()
        self.canvas.draw()
        self.relation_input.clear()
        self.initial_input.clear()
