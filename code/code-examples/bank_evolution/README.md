# Bank Architecture Evolution

This directory contains 4 versions of the same bank account code, showing how architecture evolves from monolithic code to a professional structure with packages.

## 📚 Educational Material

**Main Notebook**: [`../modules/07_progressive_architecture.ipynb`](../modules/07_progressive_architecture.ipynb)

This notebook explains each version in detail, introducing clean architecture principles.

## 📁 Versions

### v1_monolithic/ - All in one file
- ✅ Quick to start
- ❌ Mixed code
- ❌ Hard to reuse
- **File**: `bank.py` (150 lines)

**Validation**: Format only (Regex)

### v2_functional/ - Separate functions
- ✅ Separation of Concerns (SoC)
- ✅ Testable functions
- ⚠️ Still all in one file
- **File**: `bank.py` (180 lines)

**Validation**: Format only (Regex)

### v3_modular/ - Separate modules
- ✅ Code in multiple files
- ✅ Reusable module
- ✅ Complete IBAN validation (MOD-97)
- **Files**: `bank.py`, `validators.py`

**Validation**: Format + MOD-97 checksum

### v4_package/ - Package structure
- ✅ Professional architecture
- ✅ Maximum scalability
- ✅ Each module one responsibility (SRP)
- **Structure**:
  ```
  validators/
      __init__.py
      iban.py
      amount.py
  bank.py
  ```

**Validation**: Format + MOD-97 checksum

## 🎯 Principles Taught

| Principle | Description | Applied in |
|-----------|-------------|------------|
| **DRY** | Don't Repeat Yourself | v2, v3, v4 |
| **SoC** | Separation of Concerns | v2, v3, v4 |
| **SRP** | Single Responsibility Principle | v4 |

## 🚀 How to Use

### Run each version

```bash
# Version 1
cd v1_monolithic
python bank.py

# Version 2
cd v2_functional
python bank.py

# Version 3
cd v3_modular
python bank.py

# Version 4
cd v4_package
python bank.py
```

### Test validators independently

```bash
# v3
cd v3_modular
python validators.py

# v4
cd v4_package
python -m validators.iban
python -m validators.amount
```

## 📖 Recommended Learning Flow

1. **Read** the [OOP notebook](../04-oop_basics.ipynb) first
2. **Study** the [progressive architecture notebook](../modules/07_progressive_architecture.ipynb)
3. **Run** each version in order (v1 → v2 → v3 → v4)
4. **Compare** files to see differences
5. **Apply** these principles in your own projects

## 🔍 Key Differences

### Imports

```python
# v1: No internal imports
import re

# v2: No internal imports
import re

# v3: Import from module
from validators import validate_iban

# v4: Import from package
from validators import validate_iban
# (internally: from validators.iban import validate_iban)
```

### IBAN Validation

```python
# v1, v2: Format only
pattern = r'^ES\d{22}$'
return bool(re.match(pattern, iban))

# v3, v4: Format + MOD-97 checksum
def validate_iban(iban):
    return validate_iban_format(iban) and validate_iban_checksum(iban)
```

## 💡 Use Cases

| Version | When to Use |
|---------|-------------|
| v1 | Quick scripts, prototypes, <100 lines |
| v2 | Separate logic, files <500 lines |
| v3 | Medium projects, reusable code |
| v4 | Large projects, libraries, multiple collaborators |

## 📝 Suggested Exercises

1. **Add a new validator** for Spanish DNI in v4
2. **Refactor** your own monolithic code using these patterns
3. **Create tests** for each validation module
4. **Extend** to support other countries' IBANs (FR, DE, IT)

## 🔗 References

- [Notebook 04: OOP Basics](../04-oop_basics.ipynb)
- [Notebook 07: Progressive Architecture](../modules/07_progressive_architecture.ipynb)
- [IBAN Validation Algorithm](https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN)
- [Python Packages Documentation](https://docs.python.org/3/tutorial/modules.html#packages)
