# Pedagogical Guide: Progressive Architecture with IBAN

## 🎓 Overview of Created Material

This material teaches software architecture evolution using bank accounts with IBAN validation as a practical example.

## 📂 Complete Structure

```
CSPy/
├── code/
│   ├── 04-oop_basics.ipynb                    ← Prerequisite (already existed)
│   ├── modules/
│   │   └── 07_progressive_architecture.ipynb  ← NEW: Main notebook
│   └── code-examples/
│       └── bank_evolution/                    ← NEW: Progressive examples
│           ├── README.md                      ← NEW: Usage guide
│           ├── v1_monolithic/
│           │   └── bank.py                    ← All in one class
│           ├── v2_functional/
│           │   └── bank.py                    ← Separate functions
│           ├── v3_modular/
│           │   ├── bank.py                    ← Main class
│           │   └── validators.py              ← Validation module (with MOD-97)
│           └── v4_package/
│               ├── bank.py                    ← Main class
│               └── validators/                ← Structured package
│                   ├── __init__.py
│                   ├── iban.py                ← IBAN validation
│                   └── amount.py              ← Amount validation
```

## 🎯 Pedagogical Objectives

### Concepts Taught

1. **Code Evolution**
   - From monolithic to modular
   - When and how to refactor
   - Signals of code needing organization

2. **Architecture Principles**
   - **DRY** (Don't Repeat Yourself) - Do not duplicate code
   - **SoC** (Separation of Concerns) - Separate responsibilities
   - **SRP** (Single Responsibility Principle) - One responsibility per module

3. **Python Organization**
   - Functions vs methods
   - Modules (.py files)
   - Packages (directories with __init__.py)
   - Clean imports

4. **Real Validation**
   - Spanish IBANs (ES + 22 digits)
   - MOD-97 algorithm for checksum
   - Difference between format and complete validation

## 🚀 Learning Flow

### For Students

```
1. Study OOP Basics (04-oop_basics.ipynb)
   └─> Understand classes, methods, self
   
2. Read Progressive Architecture (07_progressive_architecture.ipynb)
   └─> See conceptual evolution with examples
   
3. Run versions in order (v1 → v2 → v3 → v4)
   └─> Compare real code
   
4. Apply in own projects
   └─> Recognize when to refactor
```

### For Teachers

```
Session 1: Introduction
├─> Review OOP concepts from notebook 04
├─> Show example v1 (all together)
└─> Discuss: What problems do you see?

Session 2: SoC Principle
├─> Introduce Separation of Concerns
├─> Refactor v1 → v2 live
└─> Exercise: students identify responsibilities

Session 3: Modules and DRY
├─> Explain MOD-97 (complexity justifying module)
├─> Show v3 with separate module
└─> Exercise: create email validator in module

Session 4: Packages and SRP
├─> Introduce Single Responsibility Principle
├─> Show v4 with package structure
└─> Project: refactor own code
```

## 💡 Use Cases by Version

### v1 - Monolithic
**Context**: Quick MVP prototype

```python
# Single file, basic validation
class BankAccount:
    def _is_valid_iban(self, iban):
        pattern = r'^ES\d{22}$'
        return bool(re.match(pattern, iban))
```

**Pros**: Fast, everything in one place
**Cons**: Scales poorly, not reusable

### v2 - Functional
**Context**: Small project with clear logic

```python
# Separate functions in same file
def validate_iban_format(iban): ...
def validate_positive_amount(amount): ...

class BankAccount:
    def __init__(self, iban, balance):
        if not validate_iban_format(iban): ...
```

**Pros**: Basic separation, testable
**Cons**: Still all in one file

### v3 - Modular
**Context**: Medium project, complex validation

```
v3_modular/
    validators.py  ← Reusable module with MOD-97
    bank.py        ← Imports from validators
```

**Pros**: Reusable, well organized
**Cons**: A module can grow a lot

### v4 - Package
**Context**: Large project, multiple validations

```
v4_package/
    validators/
        __init__.py    ← Exports main functions
        iban.py        ← Only IBAN validation
        amount.py      ← Only amount validation
    bank.py
```

**Pros**: Scalable, applied SRP
**Cons**: More files (not a disadvantage in large projects)

## 📊 Technical Comparison

### Lines of Code

| Version | Total | Validation | Bank Logic |
|---------|-------|------------|------------|
| v1      | 150   | ~30 (inline) | 120        |
| v2      | 180   | ~40 (functions) | 140     |
| v3      | 220   | 100 (module) | 120        |
| v4      | 250   | 120 (package) | 130       |

### Validation Complexity

| Version | Format | Checksum | Algorithm |
|---------|--------|----------|-----------|
| v1      | ✅ Regex | ❌      | -         |
| v2      | ✅ Regex | ❌      | -         |
| v3      | ✅ Regex | ✅      | MOD-97    |
| v4      | ✅ Regex | ✅      | MOD-97    |

## 🔍 Technical Details

### IBAN MOD-97 Validation

The complete algorithm (implemented in v3 and v4):

```python
def validate_iban_checksum(iban):
    # ES9121000418450200051332
    
    # 1. Move first 4 characters to the end
    # → 21000418450200051332ES91
    rearranged = iban[4:] + iban[:4]
    
    # 2. Convert letters to numbers (E=14, S=28)
    # → 210004184502000513321428 91
    numeric = ""
    for char in rearranged:
        if char.isdigit():
            numeric += char
        else:
            numeric += str(ord(char) - ord('A') + 10)
    
    # 3. MOD 97 must be 1
    # → int(numeric) % 97 == 1
    return int(numeric) % 97 == 1
```

### __init__.py Structure (v4)

```python
# validators/__init__.py
from .iban import validate_iban, validate_iban_format
from .amount import validate_positive_amount

__all__ = ['validate_iban', 'validate_positive_amount']
```

**Benefit**: Clean imports
```python
# Instead of:
from validators.iban import validate_iban

# We can write:
from validators import validate_iban
```

## 📝 Proposed Exercises

### Basic
1. Run each version and compare output
2. Modify initial balance and test operations
3. Try using invalid IBANs

### Intermediate
4. Add a `get_formatted_iban()` method that returns IBAN with spaces
   - `ES9121000418450200051332` → `ES91 2100 0418 4502 0005 1332`
5. Create a Spanish DNI validator in v4
6. Add logging to bank operations

### Advanced
7. Extend v4 to support French (FR) IBANs
8. Create unit tests for each validator
9. Implement a transaction system with history
10. Refactor your own project using these patterns

## 🎨 SOLID Principles Applied

| Principle | Where | How |
|-----------|-------|-----|
| **S**ingle Responsibility | v4 | Each module one responsibility |
| **O**pen/Closed | v3, v4 | Extensible without modifying |
| **L**iskov Substitution | - | Not applied (no inheritance) |
| **I**nterface Segregation | - | Not applied (Python duck typing) |
| **D**ependency Inversion | v3, v4 | BankAccount depends on validate_iban interface |

## 🔗 Connections with Other Notebooks

### Prerequisites
- [03-functions.ipynb](../code/03-functions.ipynb) - Functions, parameters, return
- [04-oop_basics.ipynb](../code/04-oop_basics.ipynb) - Classes, objects, methods

### Next Steps
- `05_packages_and_structure.ipynb` - Deep dive into packages
- `06_real_world_data_analysis.ipynb` - Apply in data analysis

## 🚀 Class Implementation

### Suggested Timing (2 hours)

```
0:00-0:15  OOP Review (notebook 04)
0:15-0:30  Presentation v1 (problem)
0:30-0:45  Evolution v1→v2 (SoC)
0:45-1:00  Break
1:00-1:20  Evolution v2→v3 (modules + MOD-97)
1:20-1:40  Evolution v3→v4 (packages)
1:40-2:00  Practical Exercise + Q&A
```

### Suggested Evaluation

**Quiz (10 points)**
- Name 3 architecture principles
- When to use modules vs packages?
- Explain the MOD-97 algorithm

**Practical Exercise (40 points)**
- Refactor given v1 code to v3
- Add new validator in v4
- Explain design decisions

**Project (50 points)**
- Refactor own project
- Apply at least 2 principles
- Document evolution

## 📚 Additional References

- [PEP 8](https://peps.python.org/pep-0008/) - Style Guide
- [Python Module Documentation](https://docs.python.org/3/tutorial/modules.html)
- [IBAN Validation](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [Clean Code Principles](https://en.wikipedia.org/wiki/SOLID)

---

**Created**: December 2025  
**Author**: Educational Material for CSPy  
**Version**: 1.0
