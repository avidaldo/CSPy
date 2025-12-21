# Exercises Notebook: Progressive Architecture

## 📝 General Instructions

This notebook contains practical exercises to apply what you've learned about code architecture. Complete the exercises in order, as each one builds upon the previous one.

---

## Exercise 1: Code Analysis (15 min)

### Task
Analyze the following code and answer the questions:

```python
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, email, password):
        # Validate email
        if "@" not in email or "." not in email.split("@")[1]:
            raise ValueError("Invalid email")
        
        # Validate password
        if len(password) < 8:
            raise ValueError("Password too short")
        if not any(c.isupper() for c in password):
            raise ValueError("Password missing uppercase")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password missing digit")
        
        # Save
        self.users.append({"email": email, "password": password})
    
    def send_welcome_email(self, email):
        # Simulate email sending
        print(f"Sending welcome email to {email}")
```

### Questions

1. **Which architectural principles are violated?**
   - [ ] DRY
   - [ ] SoC
   - [ ] SRP
   - [ ] All of the above

2. **What is the main problem?**
   
   Your answer:
   _________________________________________________________________
   _________________________________________________________________

3. **Which architecture version is this (v1, v2, v3, v4)?**
   
   Answer: _______________

4. **To which version should it evolve first?**
   
   Answer: _______________

---

## Exercise 2: Refactoring to v2 (20 min)

### Task
Refactor the code from Exercise 1 applying v2 architecture (functional).

```python
# Extract validations to separate functions

def validate_email(email):
    """Validates email format."""
    # TODO: Your code here
    pass


def validate_password_length(password):
    """Validates minimum password length."""
    # TODO: Your code here
    pass


def validate_password_uppercase(password):
    """Validates uppercase presence."""
    # TODO: Your code here
    pass


def validate_password_digit(password):
    """Validates digit presence."""
    # TODO: Your code here
    pass


def validate_password(password):
    """Complete password validation."""
    # TODO: Use the functions above
    pass


class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, email, password):
        # TODO: Use validation functions
        pass
    
    def send_welcome_email(self, email):
        print(f"Sending welcome email to {email}")
```

### Self-evaluation
- [ ] Functions are separated from the class
- [ ] Each function does one single thing
- [ ] `add_user()` uses the validation functions
- [ ] The code is easier to test

---

## Exercise 3: Identifying Refactoring Signals (10 min)

### Task
For each case, indicate if you need to refactor and to which version:

| Case | Refactor? | To which version? | Why? |
|------|-----------|------------------|------|
| File with 100 lines, one class | | | |
| File with 600 lines, many functions | | | |
| Module with 15 types of validations | | | |
| You copy the same regex in 5 places | | | |
| You want to use validators in another project | | | |

---

## Exercise 4: Spanish DNI Validator (30 min)

### Context
Spanish DNI has this format: 8 digits + 1 letter
- Example: `12345678Z`
- The letter is calculated: `remainder of (number ÷ 23)` gives the index in `"TRWAGMYFPDXBNJZSQVHLCKE"`

### Task
Implement a DNI validator following v3 architecture (modular).

#### File: `validators.py`
```python
def validate_dni_format(dni):
    """
    Validates format: 8 digits + 1 letter.
    
    Args:
        dni: String with the DNI
    
    Returns:
        bool: True if format is correct
    
    Examples:
        >>> validate_dni_format("12345678Z")
        True
        >>> validate_dni_format("123Z")
        False
    """
    # TODO: Your code here
    pass


def validate_dni_letter(dni):
    """
    Validates that the letter is correct according to the algorithm.
    
    Args:
        dni: String with DNI in valid format
    
    Returns:
        bool: True if the letter is correct
    
    Algorithm:
        1. Extract number (first 8 digits)
        2. Calculate: remainder of (number ÷ 23)
        3. Use index in "TRWAGMYFPDXBNJZSQVHLCKE"
        4. Compare with the DNI letter
    
    Examples:
        >>> validate_dni_letter("12345678Z")
        True
    """
    LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"
    # TODO: Your code here
    pass


def validate_dni(dni):
    """
    Complete validation: format + letter.
    
    Args:
        dni: String with the DNI
    
    Returns:
        bool: True if the DNI is valid
    """
    # TODO: Your code here
    pass


# Tests
if __name__ == "__main__":
    # Test cases
    assert validate_dni("12345678Z") == True  # TODO: Calculate valid DNI
    assert validate_dni("12345678A") == False  # Incorrect letter
    assert validate_dni("123Z") == False  # Incorrect format
    
    print("✓ All tests passed")
```

### Self-evaluation
- [ ] `validate_dni_format()` validates only the format
- [ ] `validate_dni_letter()` validates the letter algorithm
- [ ] `validate_dni()` combines both validations
- [ ] Asserts pass correctly

---

## Exercise 5: Evolving to v4 (Package) (45 min)

### Task
Convert the code from exercises 2 and 4 into a v4 package.

#### Target structure:
```
validators/
    __init__.py
    email.py       ← From exercise 2
    password.py    ← From exercise 2
    dni.py         ← From exercise 4
```

### Step 1: Create `validators/email.py`
```python
"""Email validation."""

def validate_email_format(email):
    """Validates basic email format."""
    # TODO: Move code from exercise 2
    pass


def validate_email(email):
    """Complete email validation."""
    return validate_email_format(email)


if __name__ == "__main__":
    # Tests
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False
    print("✓ Email validation OK")
```

### Step 2: Create `validators/password.py`
```python
"""Password validation."""

def validate_password_length(password, min_length=8):
    """Validates minimum length."""
    # TODO: Move code from exercise 2
    pass


def validate_password_uppercase(password):
    """Validates uppercase presence."""
    # TODO: Move code from exercise 2
    pass


def validate_password_digit(password):
    """Validates digit presence."""
    # TODO: Move code from exercise 2
    pass


def validate_password(password):
    """Complete password validation."""
    # TODO: Combine validations
    pass


if __name__ == "__main__":
    # Tests
    assert validate_password("SecurePass1") == True
    assert validate_password("weak") == False
    print("✓ Password validation OK")
```

### Step 3: Create `validators/dni.py`
```python
"""Spanish DNI validation."""

# TODO: Copy code from exercise 4
```

### Step 4: Create `validators/__init__.py`
```python
"""
Validation package.

Exports main functions from each submodule.
"""

from .email import validate_email
from .password import validate_password
from .dni import validate_dni

__all__ = [
    'validate_email',
    'validate_password',
    'validate_dni'
]
```

### Step 5: Test the package
```python
# test_validators.py
from validators import validate_email, validate_password, validate_dni

# Test imports
print("Testing email:", validate_email("test@example.com"))
print("Testing password:", validate_password("SecurePass1"))
print("Testing DNI:", validate_dni("12345678Z"))  # Adjust valid DNI

print("✓ Package working correctly")
```

### Self-evaluation
- [ ] Directory structure is correct
- [ ] Each submodule works independently
- [ ] `__init__.py` exports correctly
- [ ] External imports work

---

## Exercise 6: Real Application (60 min)

### Task
Create a user management application using the `validators` package from exercise 5.

```python
# user_manager.py

from validators import validate_email, validate_password, validate_dni


class InvalidUserDataError(Exception):
    """Error when user data is invalid."""
    pass


class User:
    """Represents a system user."""
    
    def __init__(self, email, password, dni):
        """
        Creates a new user.
        
        Args:
            email: User email
            password: User password
            dni: Spanish DNI
        
        Raises:
            InvalidUserDataError: If any data is invalid
        """
        # TODO: Validate each field using the validators package
        # TODO: If all valid, save attributes
        pass
    
    def __str__(self):
        # TODO: Return string representation of user
        pass


class UserManager:
    """Manages a collection of users."""
    
    def __init__(self):
        self.users = []
    
    def register_user(self, email, password, dni):
        """
        Registers a new user.
        
        Returns:
            User: The created user
        
        Raises:
            InvalidUserDataError: If data is invalid
            ValueError: If email already exists
        """
        # TODO: Verify email does not exist
        # TODO: Create user
        # TODO: Add to list
        # TODO: Return user
        pass
    
    def find_by_email(self, email):
        """
        Finds a user by email.
        
        Returns:
            User or None
        """
        # TODO: Search in self.users
        pass
    
    def list_all(self):
        """Lists all users."""
        # TODO: Iterate and show
        pass


# Main program
if __name__ == "__main__":
    manager = UserManager()
    
    # Case 1: Successful registration
    try:
        user1 = manager.register_user(
            "alice@example.com",
            "SecurePass1",
            "12345678Z"  # Adjust valid DNI
        )
        print(f"✓ User registered: {user1}")
    except (InvalidUserDataError, ValueError) as e:
        print(f"✗ Error: {e}")
    
    # Case 2: Duplicate email
    try:
        user2 = manager.register_user(
            "alice@example.com",  # Duplicate
            "AnotherPass1",
            "87654321X"  # Adjust valid DNI
        )
    except ValueError as e:
        print(f"✓ Expected error: {e}")
    
    # Case 3: Invalid data
    try:
        user3 = manager.register_user(
            "invalid-email",  # Invalid
            "weak",  # Invalid
            "123"  # Invalid
        )
    except InvalidUserDataError as e:
        print(f"✓ Expected error: {e}")
    
    # List users
    print("\n--- Registered users ---")
    manager.list_all()
```

### Self-evaluation
- [ ] Application uses `validators` package
- [ ] Errors are handled correctly
- [ ] Code is well organized (SoC)
- [ ] Each class has one responsibility (SRP)

---

## Exercise 7: Final Reflection (15 min)

### Reflection Questions

1. **What advantages does v4 architecture have over v1?**
   
   Your answer:
   _________________________________________________________________
   _________________________________________________________________
   _________________________________________________________________

2. **When would you use v2 instead of v4?**
   
   Your answer:
   _________________________________________________________________
   _________________________________________________________________

3. **Which principle seems most important to you and why?**
   
   Principle: ________________
   
   Why:
   _________________________________________________________________
   _________________________________________________________________

4. **Describe a project of yours that would benefit from refactoring:**
   
   Project: ________________
   
   Current state: ________________
   
   Target version: ________________
   
   Reason:
   _________________________________________________________________
   _________________________________________________________________

---

## 🎯 Solutions and Answers

*(Solutions will be provided in a review session)*

### Evaluation Criteria

**Exercise 1**: 10 points
- Identify violations: 5 pts
- Explain problem: 3 pts
- Identify version: 2 pts

**Exercise 2**: 20 points
- Correct functions: 10 pts
- Integration in class: 5 pts
- Clean code: 5 pts

**Exercise 3**: 10 points
- Correct identification: 10 pts

**Exercise 4**: 25 points
- Format validation: 8 pts
- Letter algorithm: 12 pts
- Tests: 5 pts

**Exercise 5**: 20 points
- Package structure: 8 pts
- Submodules work: 8 pts
- Correct `__init__.py`: 4 pts

**Exercise 6**: 15 points
- Package usage: 5 pts
- Error handling: 5 pts
- Organized code: 5 pts

**Total**: 100 points

---

**Estimated total time**: 3-4 hours
**Level**: Intermediate
**Prerequisite**: Completed notebooks 04 (OOP) and 07 (Progressive Architecture)

