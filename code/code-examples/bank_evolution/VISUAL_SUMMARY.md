# Progressive Architecture - Visual Summary

## 📖 The Complete Journey

```
┌─────────────────────────────────────────────────────────────────────┐
│  STARTING POINT: Notebook 04 - OOP Basics                          │
│  You know: classes, objects, methods, self                         │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  QUESTION: How do I organize code when it grows?                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  ANSWER: Notebook 07 - Progressive Architecture                    │
│  + Examples v1 → v2 → v3 → v4                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## 🔄 The 4 Versions (At a Glance)

### v1: MONOLITHIC - "Start simple"
```python
┌─────────────────────────┐
│ bank.py (1 file)        │
├─────────────────────────┤
│ • Exceptions            │
│ • Class BankAccount     │
│   ├─ __init__           │
│   ├─ _is_valid_iban ← Inline validation │
│   ├─ deposit            │
│   ├─ withdraw           │
│   └─ transfer           │
└─────────────────────────┘

Problem: All mixed, hard to reuse
```

### v2: FUNCTIONAL - "Separate responsibilities"
```python
┌─────────────────────────┐
│ bank.py (1 file)        │
├─────────────────────────┤
│ GLOBAL FUNCTIONS:       │
│ • validate_iban_format()│
│ • validate_positive_amount() │
│                         │
│ EXCEPTIONS              │
│                         │
│ CLASS BankAccount       │
│   ├─ uses functions ↑   │
│   ├─ deposit            │
│   └─ withdraw           │
└─────────────────────────┘

Improvement: Basic SoC, but still one file
```

### v3: MODULAR - "Complex validation justifies module"
```python
┌─────────────────────────┐  ┌─────────────────────────┐
│ validators.py           │  │ bank.py                 │
├─────────────────────────┤  ├─────────────────────────┤
│ • validate_iban_format()│←─│ from validators import  │
│ • validate_iban_checksum│  │   validate_iban         │
│   (complete MOD-97!)    │  │                         │
│ • validate_iban()       │  │ class BankAccount:      │
│ • validate_positive...  │  │   • uses validate_iban()│
└─────────────────────────┘  └─────────────────────────┘

Improvement: Reusable module, complete validation
```

### v4: PACKAGE - "Scalable and professional"
```python
┌────────────────────────────┐  ┌─────────────────────────┐
│ validators/                │  │ bank.py                 │
├────────────────────────────┤  ├─────────────────────────┤
│ • __init__.py (exports)    │←─│ from validators import  │
│ • iban.py                  │  │   validate_iban         │
│   ├─ validate_iban_format()│  │                         │
│   ├─ validate_iban_checksum│  │ class BankAccount:      │
│   └─ validate_iban()       │  │   • uses validate_iban()│
│ • amount.py                │  └─────────────────────────┘
│   └─ validate_positive...  │
87: └────────────────────────────┘

Improvement: Applied SRP, each module one thing
```

## 📊 Evolution of Complexity

```
IBAN Validation across versions:

v1, v2: FORMAT ONLY
┌──────────────────────────┐
│ pattern = r'^ES\d{22}$'  │
│ return bool(match(iban)) │
└──────────────────────────┘
Simple regex ← Sufficient at start

v3, v4: FORMAT + CHECKSUM
┌──────────────────────────────────────────────┐
│ def validate_iban(iban):                     │
│     # 1. Validate format                     │
│     if not re.match(r'^ES\d{22}$', iban):    │
│         return False                         │
│                                              │
│     # 2. Validate MOD-97 checksum            │
│     rearranged = iban[4:] + iban[:4]         │
│     numeric = ""                             │
│     for char in rearranged:                  │
│         if char.isdigit():                   │
│             numeric += char                  │
│         else:                                │
│             numeric += str(ord(char) - 65 + 10) │
│     return int(numeric) % 97 == 1            │
120: └──────────────────────────────────────────────┘
Complex algorithm ← Justifies separate module!
```

## 🎯 Principles Applied

```
┌────────────┬─────────────────────────────────────────────────┐
│ Principle  │ How it Applies                                  │
├────────────┼─────────────────────────────────────────────────┤
│ DRY        │ v2: Function validate_iban() instead of copying │
│            │ regex in 3 places                               │
├────────────┼─────────────────────────────────────────────────┤
│ SoC        │ v2: Validation separated from banking logic     │
│            │ v3: Validation in its own module                │
├────────────┼─────────────────────────────────────────────────┤
│ SRP        │ v4: iban.py only validates IBANs                │
│            │     amount.py only validates amounts            │
│            │     bank.py only banking logic                  │
└────────────┴─────────────────────────────────────────────────┘
```

## 🚨 Signals for Refactoring

```
You are in v1 → Consider v2 if:
├─ You copy code (same regex in various methods)
├─ The class does "too many things"
└─ Hard to explain what a method does

You are in v2 → Consider v3 if:
├─ The file exceeds 500 lines
├─ You want to reuse functions in another project
├─ You need complex validation (MOD-97)

You are in v3 → Consider v4 if:
├─ A module does too many different things
├─ You need hierarchy (validation subcategories)
└─ You are going to distribute as library
```

## 📁 Files Created (Checklist)

```
✅ code/code-examples/bank_evolution/
   ✅ README.md                    ← Usage guide
   ✅ TEACHING_GUIDE.md            ← Complete pedagogical guide
   ✅ VISUAL_SUMMARY.md            ← This file
   
   ✅ v1_monolithic/
      ✅ bank.py                   ← All in one
   
   ✅ v2_functional/
      ✅ bank.py                   ← Separate functions
   
   ✅ v3_modular/
      ✅ bank.py                   ← Main class
      ✅ validators.py             ← Module with MOD-97
   
   ✅ v4_package/
      ✅ bank.py                   ← Main class
      ✅ validators/
         ✅ __init__.py            ← Exports functions
         ✅ iban.py                ← IBAN validation
         ✅ amount.py              ← Amount validation

✅ code/modules/
   ✅ 07_progressive_architecture.ipynb  ← Teaching notebook

✅ code/04-oop_basics.ipynb
   ✅ (Updated with reference to new material)
```

## 🎓 How to Teach This

### 2-Hour Session

```
┌────────────────┬──────────────────────────────────────────┐
│ Time           │ Activity                                 │
├────────────────┼──────────────────────────────────────────┤
│ 00:00 - 00:15  │ Review: OOP from notebook 04             │
│                │ - Classes, methods, self                 │
├────────────────┼──────────────────────────────────────────┤
│ 00:15 - 00:30  │ v1: The monolithic code problem          │
│                │ - Show bank.py                           │
│                │ - Discuss: What could be improved?       │
├────────────────┼──────────────────────────────────────────┤
│ 00:30 - 00:45  │ v2: Separation of responsibilities       │
│                │ - Live coding: extract functions         │
│                │ - SoC Principle                          │
├────────────────┼──────────────────────────────────────────┤
│ 00:45 - 01:00  │ ☕ Break                                  │
├────────────────┼──────────────────────────────────────────┤
│ 01:00 - 01:20  │ v3: Modules and complex validation       │
│                │ - Explain MOD-97 (why we need it)        │
│                │ - Show validators.py                     │
│                │ - DRY Principle                          │
├────────────────┼──────────────────────────────────────────┤
│ 01:20 - 01:40  │ v4: Professional packages                │
│                │ - Directory structure                    │
│                │ - Role of __init__.py                    │
│                │ - SRP Principle                          │
├────────────────┼──────────────────────────────────────────┤
│ 01:40 - 02:00  │ Exercise: Refactor your code             │
│                │ + Q&A                                    │
└────────────────┴──────────────────────────────────────────┘
```

## 💻 Quick Commands

```bash
# Run all versions at once
cd code/code-examples/bank_evolution
python v1_monolithic/bank.py
python v2_functional/bank.py
python v3_modular/bank.py
python v4_package/bank.py

# Test validators independently
python v3_modular/validators.py
python -m v4_package.validators.iban
python -m v4_package.validators.amount
```

## 🔗 Quick References

| You want to...                 | Look at...                        |
|--------------------------------|-----------------------------------|
| Understand concepts            | `07_progressive_architecture.ipynb` |
| See real code                  | Folders `v1/`, `v2/`, `v3/`, `v4/` |
| Usage guide                    | `README.md`                       |
| Teaching guide                 | `TEACHING_GUIDE.md`               |
| Visual summary                 | `VISUAL_SUMMARY.md` (this)        |
| OOP Prerequisite               | `../04-oop_basics.ipynb`          |

## 🎉 Final Result

Students will learn:

✅ **WHEN** to refactor (problematic code signals)  
✅ **HOW** to organize (functions → modules → packages)  
✅ **WHY** it matters (maintainability, scalability, reusability)  
✅ **Principles** (DRY, SoC, SRP) with practical examples  

And the best part: with a **real** example (IBAN validation) showing why complexity justifies better organization.

---

**Complete material ready to teach** 🚀
