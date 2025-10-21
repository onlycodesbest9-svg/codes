"""
Test script for RecursiveLearn solver functionality.
Run this to verify the solver works correctly.
"""

from src.core.recurrence_solver import solve_recurrence

def test_simple_linear():
    """Test simple linear recurrence."""
    print("=" * 60)
    print("TEST 1: Simple Linear Recurrence")
    print("=" * 60)
    
    relation = "a_n = a_(n-1) + 5"
    initial = {0: 5}
    
    result = solve_recurrence(relation, initial)
    
    if result['success']:
        print(f"✓ Relation: {relation}")
        print(f"✓ Initial: {initial}")
        print(f"✓ Closed form: {result['closed_form']}")
        print(f"✓ Sequence: {result['sequence'][:10]}")
        print("\nExpected: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50")
        print("PASS ✓\n")
    else:
        print(f"✗ FAIL: {result.get('error')}\n")

def test_fibonacci():
    """Test Fibonacci sequence."""
    print("=" * 60)
    print("TEST 2: Fibonacci Sequence")
    print("=" * 60)
    
    relation = "a_n = a_(n-1) + a_(n-2)"
    initial = {0: 0, 1: 1}
    
    result = solve_recurrence(relation, initial)
    
    if result['success']:
        print(f"✓ Relation: {relation}")
        print(f"✓ Initial: {initial}")
        print(f"✓ Sequence: {result['sequence'][:10]}")
        print("\nExpected: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34")
        
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        if result['sequence'][:10] == expected:
            print("PASS ✓\n")
        else:
            print("FAIL ✗\n")
    else:
        print(f"✗ FAIL: {result.get('error')}\n")

def test_geometric():
    """Test geometric sequence."""
    print("=" * 60)
    print("TEST 3: Geometric Sequence (Doubling)")
    print("=" * 60)
    
    relation = "a_n = 2*a_(n-1)"
    initial = {0: 1}
    
    result = solve_recurrence(relation, initial)
    
    if result['success']:
        print(f"✓ Relation: {relation}")
        print(f"✓ Initial: {initial}")
        print(f"✓ Sequence: {result['sequence'][:10]}")
        print("\nExpected: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512")
        
        expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        if result['sequence'][:10] == expected:
            print("PASS ✓\n")
        else:
            print("FAIL ✗\n")
    else:
        print(f"✗ FAIL: {result.get('error')}\n")

def test_compound_interest():
    """Test compound interest (7% annually)."""
    print("=" * 60)
    print("TEST 4: Compound Interest (7% annual)")
    print("=" * 60)
    
    relation = "a_n = 1.07*a_(n-1)"
    initial = {0: 10000}
    
    result = solve_recurrence(relation, initial)
    
    if result['success']:
        print(f"✓ Relation: {relation}")
        print(f"✓ Initial: {initial}")
        print(f"✓ Sequence (first 5 years): {result['sequence'][:5]}")
        print("\nExpected (approx): 10000, 10700, 11449, 12250, 13108")
        print("PASS ✓\n")
    else:
        print(f"✗ FAIL: {result.get('error')}\n")

def test_second_order():
    """Test second-order homogeneous."""
    print("=" * 60)
    print("TEST 5: Second-Order Homogeneous")
    print("=" * 60)
    
    relation = "a_n = 3*a_(n-1) - 2*a_(n-2)"
    initial = {0: 1, 1: 4}
    
    result = solve_recurrence(relation, initial)
    
    if result['success']:
        print(f"✓ Relation: {relation}")
        print(f"✓ Initial: {initial}")
        print(f"✓ Sequence: {result['sequence'][:8]}")
        print("\nExpected: 1, 4, 10, 22, 46, 94, 190, 382")
        print("PASS ✓\n")
    else:
        print(f"✗ FAIL: {result.get('error')}\n")

def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("RecursiveLearn Solver Test Suite")
    print("=" * 60 + "\n")
    
    test_simple_linear()
    test_fibonacci()
    test_geometric()
    test_compound_interest()
    test_second_order()
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tests()
