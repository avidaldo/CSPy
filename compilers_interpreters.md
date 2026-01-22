# Compilers vs Interpreters

Before running code, it helps to understand **how** programming languages turn source code into something the computer can execute.

## Compiled languages

A **compiler** translates the entire source code into machine code (or an intermediate form) **before** the program runs.

- Examples: C, C++, Rust, Go
- You run the compiler once, producing an executable file
- The executable runs directly on the CPU—typically very fast
- Errors are caught at compile time (before execution)

```
source.c  →  [compiler]  →  program.exe  →  runs on CPU
```

## Interpreted languages

An **interpreter** reads and executes the source code **line by line** at runtime.

- Examples: JavaScript (in browsers), Ruby, older BASIC
- No separate compilation step—just run the script
- Easier to experiment interactively
- Errors appear only when the faulty line is reached

```
script.js  →  [interpreter]  →  executes immediately
```

## Python: a hybrid approach

Python uses **both** techniques:

1. **Compilation to bytecode**: when you run a `.py` file, Python first compiles it to an intermediate format called **bytecode** (`.pyc` files in `__pycache__/`).
2. **Interpretation by the Python Virtual Machine (PVM)**: the bytecode is then executed by the interpreter.

```
script.py  →  [Python compiler]  →  bytecode (.pyc)  →  [PVM interpreter]  →  runs
```

This happens automatically and transparently each time you run a script.

### Why does this matter?

- Python feels like an interpreted language (quick feedback, interactive REPL).
- Bytecode caching (`.pyc` files) speeds up subsequent runs.
- Advanced tools (PyPy, Cython) can compile Python further for better performance.

### The `__pycache__` folder

When Python compiles your modules, it stores the bytecode in `__pycache__/`. You'll typically:

- **Ignore it in Git**: add `__pycache__/` to `.gitignore`
- **Hide it in VS Code**: use `"files.exclude": { "**/__pycache__": true }` in settings
