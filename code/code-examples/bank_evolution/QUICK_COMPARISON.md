# Quick Comparison: v1 vs v2 vs v3 vs v4

## Quick Decision Table

| Criterion | v1 | v2 | v3 | v4 | Recommendation |
|-----------|----|----|----|----|----------------|
| **Total lines of code** | <150 | <200 | <500 | >500 | Start v1, evolve as it grows |
| **Number of files** | 1 | 1 | 2-3 | 4+ | More files = better organization |
| **Reusability** | ❌ | ⚠️ | ✅ | ✅✅ | v3+ for reusable code |
| **Teamwork** | ❌ | ⚠️ | ✅ | ✅✅ | v3+ for multiple developers |
| **Validation complexity** | Basic | Basic | Complete | Complete | MOD-97 only in v3+ |
| **Implementation time** | 30 min | 45 min | 1-2h | 2-3h | More time = better architecture |
| **Testability** | ❌ | ✅ | ✅✅ | ✅✅ | v2+ allows unit tests |
| **Principles applied** | - | SoC | SoC+DRY | SoC+DRY+SRP | More principles = cleaner code |

## When to Use Each Version

### ✅ Use v1 if:
- [ ] You are prototyping quickly
- [ ] It's a one-off script
- [ ] Code will not exceed 150 lines
- [ ] Only you will work on this
- [ ] You don't need to reuse code

### ✅ Use v2 if:
- [ ] You identified duplicated code in v1
- [ ] You want to separate validation logic
- [ ] Code is between 150-500 lines
- [ ] You want to start applying best practices
- [ ] Still a small/medium project

### ✅ Use v3 if:
- [ ] Validation is complex (e.g. MOD-97)
- [ ] You want to reuse validators in other projects
- [ ] Project has >500 lines
- [ ] Several people work on the code
- [ ] You need clear organization

### ✅ Use v4 if:
- [ ] You have multiple types of validations
- [ ] Validation module grows too much
- [ ] You are distributing this as a library
- [ ] You need scalable structure
- [ ] You are applying SOLID seriously

## Code Comparison

### Creating an account

```python
# v1
account = BankAccount("ES9121000418450200051332", 1000)
# Validation: format only (regex)

# v2
account = BankAccount("ES9121000418450200051332", 1000)
# Validation: format only (regex) but in separate function

# v3
account = BankAccount("ES9121000418450200051332", 1000)
# Validation: format + checksum MOD-97

# v4
account = BankAccount("ES9121000418450200051332", 1000)
# Validation: format + checksum MOD-97 (same functionality as v3)
```

**Key difference v1/v2 vs v3/v4**: Only v3 and v4 validate checksum

### Valildate IBAN directly

```python
# v1
# ❌ You can't - it's inside the class
account = BankAccount(iban, balance)  # Only validated here

# v2
# ⚠️ You can but limited
from bank import validate_iban_format
if validate_iban_format("ES123"):  # Format only
    ...

# v3
# ✅ You can - and complete
from validators import validate_iban
if validate_iban("ES9121000418450200051332"):  # Format + checksum
    ...

# v4
# ✅✅ You can - complete and organized
from validators import validate_iban
if validate_iban("ES9121000418450200051332"):  # Format + checksum
    ...
```

### Adding new validation (e.g. DNI)

```python
# v1
# Add method in BankAccount
class BankAccount:
    def _is_valid_dni(self, dni):
        # ❌ Incorrect responsibility

# v2
# Add global function
def validate_dni(dni):
    # ⚠️ File grows

# v3
# Add in validators.py
def validate_dni(dni):
    # ⚠️ Module grows

# v4
# Create validators/dni.py
def validate_dni(dni):
    # ✅✅ Each type its own module
```

## Imports

```python
# v1
import re
# All internal

# v2
import re
# All in same file

# v3
from validators import validate_iban, validate_positive_amount
import re  # only in validators.py

# v4
from validators import validate_iban, validate_positive_amount
# validators/__init__.py manages internal imports
```

## Directory Structure

```
v1/
└── bank.py                     (everything here)

v2/
└── bank.py                     (functions + class)

v3/
├── validators.py               (all validations)
└── bank.py                     (only banking logic)

v4/
├── validators/
│   ├── __init__.py            (exports functions)
│   ├── iban.py                (IBAN validation)
│   └── amount.py              (amount validation)
└── bank.py                     (only banking logic)
```

## Signals You Need to Evolve

### From v1 to v2
🚨 You copy and paste validation code  
🚨 `BankAccount` class has methods that aren't about "account"  
🚨 You want to test validation without creating full account  

### From v2 to v3
🚨 File exceeds 300-500 lines  
🚨 You need complex validation (MOD-97)  
🚨 You want to use validators in another project  
🚨 Hard to find functions in file  

### From v3 to v4
🚨 `validators.py` module exceeds 500 lines  
🚨 You have many different types of validations  
🚨 You want to distribute as library  
🚨 You need subcategories (iban, card, dni, email...)  

## IBAN Examples to Test

```python
# Valid (format + checksum correct)
"ES9121000418450200051332"  # ✅ v1, v2, v3, v4
"ES7921000813610123456789"  # ✅ v1, v2, v3, v4

# Correct format but incorrect checksum
"ES1234567890123456789012"  # ✅ v1, v2 | ❌ v3, v4

# Incorrect format
"ES123"                      # ❌ All versions
"FR1234567890123456789012"  # ❌ All (only ES supported)
```

## Tests That Should Pass

```python
# All should pass
assert BankAccount("ES9121000418450200051332", 1000)  # OK

# v1, v2 pass | v3, v4 fail
try:
    BankAccount("ES1234567890123456789012", 1000)
    print("v1 or v2: accepts incorrect checksum")
except ValueError:
    print("v3 or v4: rejects incorrect checksum")

# All fail
try:
    BankAccount("ES123", 1000)
    print("ERROR: should fail")
except ValueError:
    print("OK: invalid format detected")
```

## Code Complexity

### Cyclomatic Complexity (approximate)

| Function/Method | v1 | v2 | v3 | v4 |
|-----------------|----|----|----|----|
| validate_iban | 2 | 2 | 8 | 8 |
| BankAccount.__init__ | 4 | 4 | 3 | 3 |
| Total module bank | 15 | 18 | 12 | 12 |
| Total validation | - | - | 10 | 10 |

**Interpretation**: Low individual complexity, but total distributed better in v3/v4

## Maintainability Metrics

| Metric | v1 | v2 | v3 | v4 |
|--------|----|----|----|----|
| Coupling | High | Medium | Low | Very Low |
| Cohesion | Low | Medium | High | Very High |
| Testability | Low | High | Very High | Very High |
| Reusability | 0% | 30% | 80% | 95% |
| Maintainability | 40% | 60% | 80% | 90% |

## Summary: Which One to Choose?

```
Small Personal Project (<500 lines)    → v1 or v2
Medium Project (500-2000 lines)        → v3
Large Project (>2000 lines)            → v4
Library for Distribution               → v4
Learning architecture                  → Start v1, evolve to v4
```

## Estimated Development Time

```
v1: 30 minutes  (quick start)
v2: +15 minutes (refactor to functions)
v3: +1 hour     (create module, implement MOD-97)
v4: +1 hour     (create package, organize submodules)

Total cumulative:
v1: 30 min
v2: 45 min
v3: 1h 45min
v4: 2h 45min
```

**Conclusion**: Time investment pays off in large or reusable projects.

---

**Use this table as quick reference when deciding how to organize your code.**
