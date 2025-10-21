"""
Recurrence relation solver using SymPy.
Supports linear homogeneous and non-homogeneous recurrence relations.
"""

import sympy as sp
from typing import List, Dict, Tuple, Optional
import re


class RecurrenceSolver:
    """Solver for recurrence relations."""
    
    def __init__(self):
        self.n = sp.Symbol('n', integer=True)
        self.steps = []
        
    def parse_relation(self, relation_str: str) -> Tuple[Dict, bool]:
        """
        Parse a recurrence relation string.
        Examples: 
            "a_n = a_(n-1) + 5"
            "a_n = 3*a_(n-1) - 2*a_(n-2)"
            "a_n = 7*a_(n-1) + 3*a_(n-2) + 5"
        
        Returns: (coefficients dict, is_homogeneous)
        """
        self.steps = []
        self.steps.append(f"Parsing relation: {relation_str}")
        
        # Clean up the string
        relation_str = relation_str.replace(" ", "").replace("a_n=", "").replace("a_", "a")
        
        # Check if homogeneous (no constant term)
        has_constant = bool(re.search(r'[+-]\d+(?![n\)])', relation_str))
        
        # Extract coefficients
        coeffs = {}
        
        # Find patterns like 3*a(n-1) or a(n-2)
        pattern = r'([+-]?\d*)\*?a\(n-(\d+)\)'
        matches = re.findall(pattern, relation_str)
        
        for coeff, order in matches:
            if coeff in ['', '+']:
                coeff = 1
            elif coeff == '-':
                coeff = -1
            else:
                coeff = int(coeff)
            coeffs[int(order)] = coeff
            
        # Extract constant term
        constant_pattern = r'([+-]\d+)$'
        constant_match = re.search(constant_pattern, relation_str)
        if constant_match:
            coeffs['constant'] = int(constant_match.group(1))
        else:
            coeffs['constant'] = 0
            
        is_homogeneous = (coeffs['constant'] == 0)
        
        self.steps.append(f"Coefficients: {coeffs}")
        self.steps.append(f"Type: {'Homogeneous' if is_homogeneous else 'Non-homogeneous'}")
        
        return coeffs, is_homogeneous
    
    def solve_homogeneous(self, coeffs: Dict, initial_conditions: Dict) -> Tuple[str, List[int]]:
        """
        Solve a linear homogeneous recurrence relation.
        
        Args:
            coeffs: Dictionary of coefficients {order: coefficient}
            initial_conditions: Dictionary {0: a0, 1: a1, ...}
        
        Returns:
            (closed_form_solution, sequence_terms)
        """
        self.steps.append("\n=== Solving Homogeneous Recurrence Relation ===")
        
        # Build characteristic equation
        # For a_n = c1*a_(n-1) + c2*a_(n-2), char eq is: r^2 - c1*r - c2 = 0
        r = sp.Symbol('r')
        
        # Get the order (maximum k in a(n-k))
        orders = [k for k in coeffs.keys() if k != 'constant']
        if not orders:
            return "Cannot solve: no recurrence terms found", []
        
        max_order = max(orders)
        
        # Build characteristic equation: r^n - c1*r^(n-1) - c2*r^(n-2) - ... = 0
        char_eq = r**max_order
        for order in orders:
            char_eq -= coeffs[order] * r**(max_order - order)
        
        self.steps.append(f"\nStep 1: Characteristic equation")
        self.steps.append(f"r^{max_order} - " + " - ".join([f"{coeffs[o]}*r^{max_order-o}" for o in orders]) + " = 0")
        self.steps.append(f"Simplified: {char_eq} = 0")
        
        # Solve characteristic equation
        roots = sp.solve(char_eq, r)
        self.steps.append(f"\nStep 2: Solve for characteristic roots")
        self.steps.append(f"Roots: {roots}")
        
        # Build general solution
        if len(roots) == len(set(roots)):  # Distinct roots
            self.steps.append("\nStep 3: Distinct roots - general solution")
            # General solution: a_n = c1*r1^n + c2*r2^n + ...
            general = sum(sp.Symbol(f'c{i}') * root**self.n for i, root in enumerate(roots))
            self.steps.append(f"a_n = {general}")
        else:
            # Handle repeated roots (simplified)
            self.steps.append("\nStep 3: Repeated roots detected")
            general = sum(sp.Symbol(f'c{i}') * root**self.n for i, root in enumerate(roots))
        
        # Apply initial conditions to find constants
        self.steps.append(f"\nStep 4: Apply initial conditions {initial_conditions}")
        
        # Solve for constants (simplified approach)
        c_symbols = [sp.Symbol(f'c{i}') for i in range(len(roots))]
        equations = []
        
        for n_val, a_val in initial_conditions.items():
            eq = general.subs(self.n, n_val) - a_val
            equations.append(eq)
            self.steps.append(f"When n={n_val}: {eq} = 0")
        
        # Solve system of equations
        try:
            solution = sp.solve(equations[:len(c_symbols)], c_symbols)
            self.steps.append(f"\nConstants: {solution}")
            
            # Build closed form
            closed_form = general
            for symbol, value in solution.items():
                closed_form = closed_form.subs(symbol, value)
            
            closed_form_str = str(closed_form)
            self.steps.append(f"\n✓ Closed-form solution: a_n = {closed_form_str}")
            
            # Generate sequence terms
            sequence = [int(closed_form.subs(self.n, i)) for i in range(20)]
            
            return closed_form_str, sequence
            
        except Exception as e:
            self.steps.append(f"\nError solving for constants: {e}")
            return "Could not determine closed form", []
    
    def solve_non_homogeneous(self, coeffs: Dict, initial_conditions: Dict) -> Tuple[str, List[int]]:
        """Solve a non-homogeneous recurrence relation."""
        self.steps.append("\n=== Solving Non-Homogeneous Recurrence Relation ===")
        self.steps.append("This requires finding homogeneous + particular solution")
        
        # For now, compute iteratively
        return self.solve_iteratively(coeffs, initial_conditions)
    
    def solve_iteratively(self, coeffs: Dict, initial_conditions: Dict) -> Tuple[str, List[int]]:
        """Solve by iteration (fallback method)."""
        self.steps.append("\n=== Iterative Solution ===")
        
        # Build sequence iteratively
        sequence = [0] * 30
        
        # Set initial conditions
        for n_val, a_val in initial_conditions.items():
            sequence[n_val] = a_val
        
        # Get max order
        orders = [k for k in coeffs.keys() if k != 'constant']
        max_order = max(orders) if orders else 0
        
        # Compute subsequent terms
        for i in range(max_order, 30):
            term = 0
            for order in orders:
                if i - order >= 0:
                    term += coeffs[order] * sequence[i - order]
            term += coeffs.get('constant', 0)
            sequence[i] = term
            
            if i < 10:
                self.steps.append(f"a_{i} = {term}")
        
        return f"Sequence computed iteratively (first 30 terms)", sequence
    
    def solve(self, relation: str, initial_conditions: Dict) -> Dict:
        """
        Main solving method.
        
        Args:
            relation: Recurrence relation string
            initial_conditions: Dict of initial values {0: a0, 1: a1, ...}
        
        Returns:
            Dictionary with solution info
        """
        self.steps = []
        
        try:
            coeffs, is_homogeneous = self.parse_relation(relation)
            
            if is_homogeneous:
                closed_form, sequence = self.solve_homogeneous(coeffs, initial_conditions)
            else:
                closed_form, sequence = self.solve_non_homogeneous(coeffs, initial_conditions)
            
            return {
                'success': True,
                'closed_form': closed_form,
                'sequence': sequence[:20],  # First 20 terms
                'steps': self.steps,
                'is_homogeneous': is_homogeneous,
                'coefficients': coeffs
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'steps': self.steps
            }
    
    def get_steps(self) -> List[str]:
        """Return the solution steps."""
        return self.steps


# Simple interface functions
def solve_recurrence(relation: str, initial_conditions: Dict) -> Dict:
    """Convenience function to solve a recurrence relation."""
    solver = RecurrenceSolver()
    return solver.solve(relation, initial_conditions)


def compute_sequence(relation: str, initial_conditions: Dict, n_terms: int = 20) -> List[int]:
    """Compute sequence terms from a recurrence relation."""
    result = solve_recurrence(relation, initial_conditions)
    if result['success']:
        return result['sequence'][:n_terms]
    return []
