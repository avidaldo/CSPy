# Basic Software Engineering Concepts

When developing applications like our [Bank Example](code/code-examples/bank/), writing code that "just works" is often not enough. As projects grow, we need to organize code so it satisfies three key quality attributes:

1.  **Maintainability**: How easy it is to fix bugs, update libraries, or modify existing features without breaking other parts of the system.
2.  **Readability**: How easily a human developer (including "future you") can understand the code's intent. Code is read much more often than it is written.
3.  **Scalability**: How well the software handles growth—whether that's adding new features (complexity scalability), handling more data, or serving more users.

## 1. Separation of Concerns (SoC)

**Separation of Concerns** is a design principle for separating a computer program into distinct sections such that each section addresses a separate concern. A "concern" is a set of information that affects the code of a computer program.

### In the Bank Example
We moved away from a monolithic script where logic, data, and user interaction were mixed together. Instead, we separated the application into distinct layers:

*   **Domain Layer (`bank_domain.py`)**: Defines the core business concepts (e.g., `Account`, `Customer`). It knows *nothing* about how the data is displayed or stored.
*   **Logic/Manager Layer (`bank_manager.py`)**: Handles the "business rules" and orchestration (e.g., transferring funds, creating accounts). It connects the domain to the outside world.
*   **Presentation Layer (`bank_gui.py`)**: Handles the User Interface. It knows how to draw buttons and windows but delegates actual work to the Manager.

## 2. Single Responsibility Principle (SRP)

The **Single Responsibility Principle** states that a module, class, or function should have responsibility over a single part of the functionality provided by the software. A popular paraphrase is: *"A class should have only one reason to change."*

### In the Bank Example
*   **Before SRP**: A single `Bank` class might have handled storing balances, printing statements to the console, and saving data to a file.
*   **After SRP**:
    *   The `Account` class is responsible only for holding account data and valid state changes (deposit/withdraw).
    *   The UI code is responsible only for displaying widgets.
    *   If we want to change how the GUI looks, we only modify `bank_gui.py`—we don't touch the logic. If we change interest rate rules, we touch the domain/manager, not the GUI.

## 3. Cohesion

**Cohesion** refers to the degree to which the elements inside a module belong together. We strive for **high cohesion**.

*   **High Cohesion**: A file or class contains functions/data that are closely related and work toward a common goal.
*   **Low Cohesion**: A "Utility" file that contains a random mix of math functions, string formatting, database connection code, and UI helpers.

### In the Bank Example
`bank_domain.py` has high cohesion because it contains only classes related to the banking entities (`Account`, `Customer`). It doesn't contain unrelated utility functions.

## 4. Coupling

**Coupling** is the degree of interdependence between software modules; a measure of how closely connected two routines or modules are. We strive for **loose coupling**.

*   **Tight Coupling**: Changing one module requires changing many others. For example, if `bank_gui.py` directly modified variables inside `Account`, changing the variable name in `Account` would break the GUI.
*   **Loose Coupling**: Modules interact through well-defined interfaces (methods).

### In the Bank Example
The GUI doesn't reach effectively into the "guts" of the database or domain objects. It asks the `BankManager` to perform actions. This means we could potentially swap out the GUI for a Command Line Interface (CLI) or a Web API without rewriting the core banking logic.
