"""Lesson content for RecursiveLearn."""

from .models import Lesson, LessonSection, Exercise


def get_all_lessons():
    """Return all lesson modules."""
    return [
        get_lesson_1(),
        get_lesson_2(),
        get_lesson_3()
    ]


def get_lesson_1():
    """Lesson 1: Sequences and Recurrence Relations."""
    
    sections = [
        LessonSection(
            title="What is a Sequence?",
            content="""
            <h3>Definition</h3>
            <p>A <b>sequence</b> is an ordered list of numbers. Each number in the sequence is called a <b>term</b>.</p>
            
            <p>We denote a sequence as: a₀, a₁, a₂, a₃, ..., aₙ, ...</p>
            
            <p>Where:</p>
            <ul>
                <li>a₀ is the first term (or a₁ in some conventions)</li>
                <li>aₙ is the nth term</li>
                <li>n is the index (position in the sequence)</li>
            </ul>
            
            <h3>Examples of Sequences</h3>
            <ul>
                <li><b>Natural numbers:</b> 1, 2, 3, 4, 5, ...</li>
                <li><b>Even numbers:</b> 0, 2, 4, 6, 8, ...</li>
                <li><b>Powers of 2:</b> 1, 2, 4, 8, 16, ...</li>
                <li><b>Fibonacci:</b> 0, 1, 1, 2, 3, 5, 8, 13, ...</li>
            </ul>
            """,
            examples=[
                {"sequence": [1, 2, 3, 4, 5], "formula": "aₙ = n"},
                {"sequence": [0, 2, 4, 6, 8], "formula": "aₙ = 2n"},
                {"sequence": [1, 2, 4, 8, 16], "formula": "aₙ = 2ⁿ"}
            ]
        ),
        
        LessonSection(
            title="What is a Recurrence Relation?",
            content="""
            <h3>Definition</h3>
            <p>A <b>recurrence relation</b> is an equation that defines each term of a sequence 
            as a function of preceding terms.</p>
            
            <p><b>General form:</b> aₙ = f(aₙ₋₁, aₙ₋₂, ..., a₀)</p>
            
            <h3>Key Components</h3>
            <ol>
                <li><b>Recurrence equation:</b> The formula relating terms</li>
                <li><b>Initial conditions:</b> Starting values (a₀, a₁, etc.)</li>
            </ol>
            
            <h3>Simple Example</h3>
            <p><b>Recurrence:</b> aₙ = aₙ₋₁ + 5</p>
            <p><b>Initial condition:</b> a₀ = 5</p>
            
            <p><b>Computing the sequence:</b></p>
            <ul>
                <li>a₀ = 5 (given)</li>
                <li>a₁ = a₀ + 5 = 5 + 5 = 10</li>
                <li>a₂ = a₁ + 5 = 10 + 5 = 15</li>
                <li>a₃ = a₂ + 5 = 15 + 5 = 20</li>
            </ul>
            
            <p>This generates the sequence: 5, 10, 15, 20, 25, ...</p>
            """,
            examples=[
                {
                    "relation": "aₙ = aₙ₋₁ + 5",
                    "initial": {"a₀": 5},
                    "sequence": [5, 10, 15, 20, 25]
                }
            ]
        ),
        
        LessonSection(
            title="Real-World Example: Compound Interest",
            content="""
            <h3>The Problem</h3>
            <p>You invest $10,000 in a savings account with 7% annual interest, compounded yearly.
            How much money will you have after n years?</p>
            
            <h3>Solution</h3>
            <p>Let Aₙ = amount after n years</p>
            
            <p><b>Recurrence relation:</b> Aₙ = 1.07 × Aₙ₋₁</p>
            <p><b>Initial condition:</b> A₀ = 10,000</p>
            
            <p><b>Computing:</b></p>
            <ul>
                <li>A₀ = $10,000</li>
                <li>A₁ = 1.07 × 10,000 = $10,700</li>
                <li>A₂ = 1.07 × 10,700 = $11,449</li>
                <li>A₃ = 1.07 × 11,449 = $12,250</li>
            </ul>
            
            <p><b>Closed-form solution:</b> Aₙ = 10,000 × (1.07)ⁿ</p>
            """,
            examples=[
                {
                    "relation": "Aₙ = 1.07 × Aₙ₋₁",
                    "initial": {"A₀": 10000},
                    "application": "Compound Interest"
                }
            ]
        ),
        
        LessonSection(
            title="Example: Number of Subsets",
            content="""
            <h3>The Problem</h3>
            <p>How many subsets does a set with n elements have?</p>
            
            <h3>Analysis</h3>
            <p>Consider a set with n elements. To form subsets:</p>
            <ul>
                <li>Each subset of the first (n-1) elements is still a subset</li>
                <li>We can also add the nth element to each subset</li>
                <li>This doubles the number of subsets!</li>
            </ul>
            
            <p><b>Recurrence relation:</b> Sₙ = 2 × Sₙ₋₁</p>
            <p><b>Initial condition:</b> S₀ = 1 (empty set has 1 subset: itself)</p>
            
            <p><b>Computing:</b></p>
            <ul>
                <li>S₀ = 1</li>
                <li>S₁ = 2 × 1 = 2</li>
                <li>S₂ = 2 × 2 = 4</li>
                <li>S₃ = 2 × 4 = 8</li>
            </ul>
            
            <p><b>Closed-form solution:</b> Sₙ = 2ⁿ</p>
            """,
            examples=[]
        ),
        
        LessonSection(
            title="Example: Tower of Hanoi",
            content="""
            <h3>The Problem</h3>
            <p>In the Tower of Hanoi puzzle, you must move n disks from one peg to another,
            following these rules:</p>
            <ul>
                <li>Only one disk can be moved at a time</li>
                <li>A larger disk cannot be placed on a smaller disk</li>
            </ul>
            
            <p><b>Question:</b> What is the minimum number of moves required?</p>
            
            <h3>Solution</h3>
            <p>To move n disks:</p>
            <ol>
                <li>Move top (n-1) disks to auxiliary peg: Tₙ₋₁ moves</li>
                <li>Move largest disk to destination: 1 move</li>
                <li>Move (n-1) disks from auxiliary to destination: Tₙ₋₁ moves</li>
            </ol>
            
            <p><b>Recurrence relation:</b> Tₙ = 2Tₙ₋₁ + 1</p>
            <p><b>Initial condition:</b> T₁ = 1</p>
            
            <p><b>Computing:</b></p>
            <ul>
                <li>T₁ = 1</li>
                <li>T₂ = 2(1) + 1 = 3</li>
                <li>T₃ = 2(3) + 1 = 7</li>
                <li>T₄ = 2(7) + 1 = 15</li>
            </ul>
            
            <p><b>Closed-form solution:</b> Tₙ = 2ⁿ - 1</p>
            """,
            examples=[]
        )
    ]
    
    exercises = [
        Exercise(
            id="L1E1",
            question="Find the first 5 terms of the sequence defined by aₙ = aₙ₋₁ + n, with a₀ = 5",
            answer="5, 6, 8, 11, 15",
            hints=[
                "Start with a₀ = 5",
                "a₁ = a₀ + 1 = 5 + 1 = 6",
                "a₂ = a₁ + 2 = 6 + 2 = 8"
            ],
            difficulty="beginner",
            relation="a_n = a_(n-1) + n",
            initial_conditions={0: 5}
        ),
        Exercise(
            id="L1E2",
            question="If Aₙ = 1.05 × Aₙ₋₁ with A₀ = 1000, find A₃ (compound interest at 5%)",
            answer="1157.63",
            hints=[
                "This represents 5% annual interest",
                "A₁ = 1.05 × 1000 = 1050",
                "Continue for A₂ and A₃"
            ],
            difficulty="beginner"
        ),
        Exercise(
            id="L1E3",
            question="For the Tower of Hanoi with 5 disks, how many moves are required?",
            answer="31",
            hints=[
                "Use the relation Tₙ = 2Tₙ₋₁ + 1",
                "Or use the closed form: Tₙ = 2ⁿ - 1",
                "T₅ = 2⁵ - 1"
            ],
            difficulty="intermediate"
        )
    ]
    
    return Lesson(
        id=1,
        title="Sequences and Recurrence Relations",
        description="Introduction to sequences and their recurrence relations with real-world examples",
        sections=sections,
        exercises=exercises
    )


def get_lesson_2():
    """Lesson 2: Solving Linear Homogeneous Recurrence Relations."""
    
    sections = [
        LessonSection(
            title="Linear Homogeneous Recurrence Relations",
            content="""
            <h3>Definition</h3>
            <p>A <b>linear homogeneous recurrence relation</b> of degree k has the form:</p>
            <p><b>aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ</b></p>
            
            <p>Where:</p>
            <ul>
                <li>c₁, c₂, ..., cₖ are constants</li>
                <li>cₖ ≠ 0 (degree is exactly k)</li>
                <li>No constant term (that's what "homogeneous" means)</li>
            </ul>
            
            <h3>Examples</h3>
            <ul>
                <li><b>Degree 1:</b> aₙ = 3aₙ₋₁</li>
                <li><b>Degree 2:</b> aₙ = aₙ₋₁ + aₙ₋₂ (Fibonacci)</li>
                <li><b>Degree 2:</b> aₙ = 3aₙ₋₁ - 2aₙ₋₂</li>
            </ul>
            """,
            examples=[]
        ),
        
        LessonSection(
            title="The Characteristic Equation Method",
            content="""
            <h3>Step-by-Step Process</h3>
            
            <h4>Step 1: Form the Characteristic Equation</h4>
            <p>For aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, assume aₙ = rⁿ and substitute:</p>
            <p>rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻²</p>
            <p>Divide by rⁿ⁻²:</p>
            <p><b>r² - c₁r - c₂ = 0</b></p>
            
            <h4>Step 2: Solve for Roots</h4>
            <p>Solve the characteristic equation to find r₁ and r₂</p>
            
            <h4>Step 3: Write General Solution</h4>
            <p><b>Case 1: Distinct roots r₁ ≠ r₂</b></p>
            <p>aₙ = A·r₁ⁿ + B·r₂ⁿ</p>
            
            <p><b>Case 2: Repeated root r₁ = r₂ = r</b></p>
            <p>aₙ = A·rⁿ + B·n·rⁿ</p>
            
            <h4>Step 4: Apply Initial Conditions</h4>
            <p>Use a₀ and a₁ to solve for A and B</p>
            """,
            examples=[]
        ),
        
        LessonSection(
            title="Worked Example: Fibonacci Sequence",
            content="""
            <h3>Problem</h3>
            <p>Solve: aₙ = aₙ₋₁ + aₙ₋₂ with a₀ = 0, a₁ = 1</p>
            
            <h3>Solution</h3>
            
            <p><b>Step 1: Characteristic equation</b></p>
            <p>r² = r + 1</p>
            <p>r² - r - 1 = 0</p>
            
            <p><b>Step 2: Solve using quadratic formula</b></p>
            <p>r = (1 ± √5) / 2</p>
            <p>r₁ = (1 + √5)/2 ≈ 1.618 (golden ratio φ)</p>
            <p>r₂ = (1 - √5)/2 ≈ -0.618</p>
            
            <p><b>Step 3: General solution (distinct roots)</b></p>
            <p>aₙ = A·r₁ⁿ + B·r₂ⁿ</p>
            
            <p><b>Step 4: Apply initial conditions</b></p>
            <p>a₀ = A + B = 0 → B = -A</p>
            <p>a₁ = A·r₁ + B·r₂ = 1</p>
            <p>Solving: A = 1/√5, B = -1/√5</p>
            
            <p><b>Closed-form solution:</b></p>
            <p>aₙ = (1/√5)[(1+√5)/2]ⁿ - (1/√5)[(1-√5)/2]ⁿ</p>
            """,
            examples=[]
        ),
        
        LessonSection(
            title="Worked Example: Second-Order Relation",
            content="""
            <h3>Problem</h3>
            <p>Solve: aₙ = 3aₙ₋₁ - 2aₙ₋₂ with a₀ = 1, a₁ = 4</p>
            
            <h3>Solution</h3>
            
            <p><b>Step 1: Characteristic equation</b></p>
            <p>r² = 3r - 2</p>
            <p>r² - 3r + 2 = 0</p>
            
            <p><b>Step 2: Factor and solve</b></p>
            <p>(r - 1)(r - 2) = 0</p>
            <p>r₁ = 1, r₂ = 2</p>
            
            <p><b>Step 3: General solution</b></p>
            <p>aₙ = A·1ⁿ + B·2ⁿ = A + B·2ⁿ</p>
            
            <p><b>Step 4: Apply initial conditions</b></p>
            <p>a₀ = A + B = 1</p>
            <p>a₁ = A + 2B = 4</p>
            <p>Solving: B = 3, A = -2</p>
            
            <p><b>Closed-form solution:</b></p>
            <p>aₙ = -2 + 3·2ⁿ = 3·2ⁿ - 2</p>
            
            <p><b>Verification:</b></p>
            <ul>
                <li>a₀ = 3·1 - 2 = 1 ✓</li>
                <li>a₁ = 3·2 - 2 = 4 ✓</li>
                <li>a₂ = 3·4 - 2 = 10 ✓</li>
            </ul>
            """,
            examples=[]
        )
    ]
    
    exercises = [
        Exercise(
            id="L2E1",
            question="Solve aₙ = 2aₙ₋₁ with a₀ = 3. Find the closed form.",
            answer="aₙ = 3·2ⁿ",
            hints=[
                "This is degree 1, very simple",
                "Characteristic equation: r = 2",
                "General solution: aₙ = A·2ⁿ"
            ],
            difficulty="beginner"
        ),
        Exercise(
            id="L2E2",
            question="For aₙ = 5aₙ₋₁ - 6aₙ₋₂ with a₀=1, a₁=2, find a₅",
            answer="626",
            hints=[
                "Form characteristic equation: r² - 5r + 6 = 0",
                "Factor: (r-2)(r-3) = 0",
                "Roots are r₁=2, r₂=3"
            ],
            difficulty="intermediate"
        )
    ]
    
    return Lesson(
        id=2,
        title="Solving Linear Homogeneous Recurrence Relations",
        description="Learn the characteristic equation method for solving recurrence relations",
        sections=sections,
        exercises=exercises
    )


def get_lesson_3():
    """Lesson 3: Applications of Recurrence Relations."""
    
    sections = [
        LessonSection(
            title="Applications in Computer Science",
            content="""
            <h3>Algorithm Analysis</h3>
            <p>Recurrence relations are essential for analyzing recursive algorithms.</p>
            
            <h4>Example: Binary Search</h4>
            <p>Time complexity: T(n) = T(n/2) + 1</p>
            <p>Solution: T(n) = O(log n)</p>
            
            <h4>Example: Merge Sort</h4>
            <p>Time complexity: T(n) = 2T(n/2) + n</p>
            <p>Solution: T(n) = O(n log n)</p>
            """,
            examples=[]
        ),
        
        LessonSection(
            title="Population Growth Models",
            content="""
            <h3>Discrete Population Model</h3>
            <p>Population growth can be modeled with recurrence relations.</p>
            
            <p><b>Simple growth:</b> Pₙ = r·Pₙ₋₁</p>
            <p>Where r is the growth rate</p>
            
            <p><b>Logistic growth:</b> Pₙ = r·Pₙ₋₁(1 - Pₙ₋₁/K)</p>
            <p>Where K is the carrying capacity</p>
            """,
            examples=[]
        )
    ]
    
    exercises = [
        Exercise(
            id="L3E1",
            question="A bacteria population doubles every hour. Starting with 100, how many after 6 hours?",
            answer="6400",
            hints=[
                "This is Pₙ = 2·Pₙ₋₁",
                "Closed form: Pₙ = 100·2ⁿ",
                "P₆ = 100·2⁶"
            ],
            difficulty="beginner"
        )
    ]
    
    return Lesson(
        id=3,
        title="Applications of Recurrence Relations",
        description="Real-world applications in computer science, biology, and economics",
        sections=sections,
        exercises=exercises
    )
