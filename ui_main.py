"""Eto Yung main UI dito nagcoconnect yung style"""


from __future__ import annotations
from PySide6 import QtWidgets, QtCore, QtGui
from typing import List
from pathlib import Path
from hash_table import HashTable, Record
from storage_manager import StorageManager

class ThemeManager:
    def __init__(self, qss_path: Path) -> None:
        self.qss_path = qss_path
        self.full_qss = qss_path.read_text(encoding="utf-8") if qss_path.exists() else ""
        self.dark_marker = "/* DARK THEME */"
        self.light_marker = "/* LIGHT THEME */"

    def get_dark_qss(self) -> str:
        if not self.full_qss:
            return ""
        start = self.full_qss.find(self.dark_marker)
        light = self.full_qss.find(self.light_marker)
        if start == -1:
            return self.full_qss
        return self.full_qss[start: light if light != -1 else len(self.full_qss)]

    def get_light_qss(self) -> str:
        if not self.full_qss:
            return ""
        light = self.full_qss.find(self.light_marker)
        if light == -1:
            return self.full_qss
        return self.full_qss[light:]

class MainAppWindow(QtWidgets.QMainWindow):
    def __init__(self, qss_path: Path) -> None:
        super().__init__()
        self.setWindowTitle("SmartHash Manager")
        self.resize(1100, 720)
        self.setObjectName("mainWindow")

        self.hash_table = HashTable()
        self.storage = StorageManager()
        self.theme_mgr = ThemeManager(qss_path)
        self.is_dark = False

        self._build_ui()
        self._apply_theme(light=True)
        self._load_autosave()

    def _build_ui(self) -> None:
        central = QtWidgets.QWidget(self)
        layout = QtWidgets.QHBoxLayout(central)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)

        # Sidebar column
        self.sidebar = QtWidgets.QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        vside = QtWidgets.QVBoxLayout(self.sidebar)
        vside.setContentsMargins(8, 8, 8, 8)
        vside.setSpacing(8)

        def make_btn(text: str, icon: QtWidgets.QStyle.StandardPixmap) -> QtWidgets.QPushButton:
            btn = QtWidgets.QPushButton(text)
            btn.setIcon(self.style().standardIcon(icon))
            btn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn.setMinimumHeight(36)
            return btn

        self.btn_add = make_btn("Add Item", QtWidgets.QStyle.StandardPixmap.SP_DialogYesButton)
        self.btn_remove = make_btn("Remove Item", QtWidgets.QStyle.StandardPixmap.SP_DialogNoButton)
        self.btn_show = make_btn("Show All", QtWidgets.QStyle.StandardPixmap.SP_FileDialogContentsView)
        self.btn_export = make_btn("Export CSV", QtWidgets.QStyle.StandardPixmap.SP_DialogSaveButton)
        self.btn_import = make_btn("Import CSV", QtWidgets.QStyle.StandardPixmap.SP_DialogOpenButton)
        self.btn_theme = make_btn("Toggle Theme", QtWidgets.QStyle.StandardPixmap.SP_BrowserReload)
        self.btn_theme.setObjectName("themeButton")
        self.btn_remove.setObjectName("removeButton")

        # Sidebar buttons
        for w in [self.btn_add, self.btn_remove, self.btn_show, self.btn_export, self.btn_import, self.btn_theme]:
            vside.addWidget(w)

        vside.addStretch(1)

        # Main contents
        content = QtWidgets.QFrame()
        content.setObjectName("inputFrame")
        v = QtWidgets.QVBoxLayout(content)
        v.setSpacing(8)

        header = QtWidgets.QLabel("SmartHash Manager")
        header.setObjectName("headerTitle")
        header.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        v.addWidget(header)

        # Mode and inputs
        form = QtWidgets.QGridLayout()
        form.setHorizontalSpacing(12)
        form.setVerticalSpacing(8)

        self.mode_combo = QtWidgets.QComboBox()
        self.mode_combo.addItems(["Product", "Item"])

        self.id_edit = QtWidgets.QLineEdit()
        self.id_edit.setPlaceholderText("Numeric ID (required)")
        self.name_edit = QtWidgets.QLineEdit()
        self.name_edit.setPlaceholderText("Name")

        self.price_spin = QtWidgets.QDoubleSpinBox()
        self.price_spin.setPrefix("₱ ")
        self.price_spin.setMaximum(10_000_000)
        self.price_spin.setDecimals(2)
        self.price_spin.setSingleStep(1.0)

        self.desc_edit = QtWidgets.QTextEdit()
        self.desc_edit.setPlaceholderText("Item description")

        form.addWidget(QtWidgets.QLabel("Mode"), 0, 0)
        form.addWidget(self.mode_combo, 0, 1)
        form.addWidget(QtWidgets.QLabel("ID"), 1, 0)
        form.addWidget(self.id_edit, 1, 1)
        form.addWidget(QtWidgets.QLabel("Name"), 2, 0)
        form.addWidget(self.name_edit, 2, 1)
        form.addWidget(QtWidgets.QLabel("Price (₱)"), 3, 0)
        form.addWidget(self.price_spin, 3, 1)
        form.addWidget(QtWidgets.QLabel("Description"), 4, 0)
        form.addWidget(self.desc_edit, 4, 1)

        v.addLayout(form)

        # Search widgets
        search_row = QtWidgets.QHBoxLayout()
        self.search_edit = QtWidgets.QLineEdit()
        self.search_edit.setPlaceholderText("Search by ID or Name")
        self.search_edit.setClearButtonEnabled(True)
        search_row.addWidget(self.search_edit)
        v.addLayout(search_row)

        # Table column
        self.table = QtWidgets.QTableWidget(0, 6)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(["Mode", "ID", "Name", "Price/Desc", "Key", "Hash"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        v.addWidget(self.table)

        layout.addWidget(self.sidebar)
        layout.addWidget(content, 1)
        self.setCentralWidget(central)

        # Tooltips
        self.id_edit.setToolTip("Enter a numeric ID (e.g., 1001)")
        self.mode_combo.setToolTip("Switch between Product and Item modes")
        self.price_spin.setToolTip("Only used in Product mode")
        self.desc_edit.setToolTip("Only used in Item mode")
        self.btn_add.setToolTip("Add or update an item")
        self.btn_remove.setToolTip("Remove the selected item")
        self.btn_export.setToolTip("Export all items to CSV")
        self.btn_import.setToolTip("Import items from CSV")
        self.btn_theme.setToolTip("Toggle light/dark theme")

        # Signals
        self.mode_combo.currentTextChanged.connect(self._on_mode_change)
        self.btn_add.clicked.connect(self._on_add)
        self.btn_remove.clicked.connect(self._on_remove)
        self.btn_show.clicked.connect(self._refresh_table)
        self.btn_export.clicked.connect(self._on_export_csv)
        self.btn_import.clicked.connect(self._on_import_csv)
        self.btn_theme.clicked.connect(self._toggle_theme)
        self.search_edit.textChanged.connect(self._apply_filter)

        # Initialize mode
        self._on_mode_change(self.mode_combo.currentText())

    def _apply_theme(self, light: bool) -> None:
        qss = self.theme_mgr.get_light_qss() if light else self.theme_mgr.get_dark_qss()
        self.setStyleSheet(qss)

    def _toggle_theme(self) -> None:
        self.is_dark = not self.is_dark
        self._apply_theme(light=not self.is_dark)

    def _on_mode_change(self, mode: str) -> None:
        is_product = (mode == "Product")
        self.price_spin.setVisible(is_product)
        self.findChild(QtWidgets.QLabel, None).setVisible(True)
        self.desc_edit.setVisible(not is_product)
        self.name_edit.setPlaceholderText("Product name" if is_product else "Item name")

    def _validate_inputs(self) -> tuple[bool, str]:
        id_text = self.id_edit.text().strip()
        name = self.name_edit.text().strip()
        if not id_text.isdigit():
            return False, "ID must be numeric"
        if not name:
            return False, "Name must not be empty"
        if self.mode_combo.currentText() == "Product" and self.price_spin.value() <= 0:
            return False, "Price must be greater than 0"
        if self.mode_combo.currentText() == "Item" and not self.desc_edit.toPlainText().strip():
            return False, "Description must not be empty"
        return True, ""

    def _on_add(self) -> None:
        ok, msg = self._validate_inputs()
        if not ok:
            QtWidgets.QMessageBox.warning(self, "Validation", msg)
            return
        mode = self.mode_combo.currentText()
        id_val = int(self.id_edit.text().strip())
        name = self.name_edit.text().strip()
        if mode == "Product":
            rec = Record(mode=mode, id=id_val, name=name, price=float(self.price_spin.value()))
        else:
            rec = Record(mode=mode, id=id_val, name=name, description=self.desc_edit.toPlainText().strip())
        self.hash_table.insert(id_val, rec)
        self._refresh_table()

    def _on_remove(self) -> None:
        row = self.table.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.information(self, "Remove", "Select a row to remove.")
            return
        id_item = self.table.item(row, 1)
        if not id_item:
            return
        id_val = int(id_item.text())
        reply = QtWidgets.QMessageBox.question(
            self, "Confirm", f"Remove item with ID {id_val}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            if self.hash_table.remove(id_val):
                self._refresh_table()

    def _apply_filter(self, text: str) -> None:
        text = text.strip().lower()
        for r in range(self.table.rowCount()):
            id_text = self.table.item(r, 1).text().lower() if self.table.item(r, 1) else ""
            name_text = self.table.item(r, 2).text().lower() if self.table.item(r, 2) else ""
            match = (text in id_text) or (text in name_text)
            self.table.setRowHidden(r, not match)

    def _refresh_table(self) -> None:
        items: List[Record] = list(self.hash_table.items())
        self.table.setRowCount(0)
        for rec in items:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(rec.mode))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(rec.id)))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(rec.name))
            fourth = f"₱ {rec.price:.2f}" if rec.mode == "Product" and rec.price is not None else (rec.description or "")
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(fourth))
            self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(rec.key if rec.key is not None else rec.id)))
            self.table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(rec.hash_index if rec.hash_index is not None else "")))
        self.table.resizeColumnsToContents()

    def _on_export_csv(self) -> None:
        fp, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As CSV", "smarthash.csv", "CSV Files (*.csv)")
        if not fp:
            return
        self.storage.export_csv(Path(fp), list(self.hash_table.items()))
        QtWidgets.QMessageBox.information(self, "Export", "Export completed.")

    def _on_import_csv(self) -> None:
        fp, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if not fp:
            return
        records = self.storage.import_csv(Path(fp))
        for rec in records:
            self.hash_table.insert(rec.id, rec)
        self._refresh_table()
        QtWidgets.QMessageBox.information(self, "Import", f"Imported {len(records)} records.")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        try:
            self.storage.autosave_json(list(self.hash_table.items()))
        finally:
            event.accept()

    def _load_autosave(self) -> None:
        records = self.storage.load_autosave()
        for rec in records:
            self.hash_table.insert(rec.id, rec)
        self._refresh_table()
