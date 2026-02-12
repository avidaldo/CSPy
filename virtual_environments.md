# Virtual Environments in Python (pip, venv, uv, conda) and Docker

Python projects almost always need **dependencies** (libraries like `numpy`, `requests`, `pandas`). A **virtual environment** isolates those dependencies per project so:

- one project can use `numpy==1.x` while another uses `numpy==2.x`
- upgrading libraries doesn’t break other projects
- your “it works on my machine” problems shrink dramatically

This guide focuses on the most common tools you will see:

- **pip**: installs Python packages
- **venv**: creates isolated environments (ships with Python)
- **uv**: a modern, fast tool that can manage environments + dependencies
- **conda / Anaconda**: environments + packages (including non-Python binaries)
- **Docker**: containerizes the whole runtime (not just Python packages)

---

## 0) The key idea: interpreter vs packages

When you run:

- `python your_script.py`

you are using **one specific Python interpreter** (a specific executable). That interpreter has access to **a specific set of installed packages**.

A virtual environment is basically:

- a *copy/overlay* of a Python interpreter
- a private `site-packages/` folder

So the goal is: **make sure the `python` you run is the one from your project environment**.

---

## 1) pip (package installer)

### What pip is

- `pip` installs Python packages from the Python Package Index (PyPI).
- `pip` does **not** create environments by itself.

### Safer invocation

In teaching and automation, prefer:

- `python -m pip install ...`

Because it guarantees pip runs for the same interpreter as `python`.

### Basic tutorial

Install a package:

- `python -m pip install requests`

List installed packages:

- `python -m pip list`

Freeze to a file (common in simpler projects):

- `python -m pip freeze > requirements.txt`

Install from a requirements file:

- `python -m pip install -r requirements.txt`

Upgrade pip itself:

- `python -m pip install --upgrade pip`

### Where pip fits

- Use pip **inside a virtual environment** (recommended)
- Use pip globally only for tooling you truly want system-wide (often better solved with a dedicated tool manager)

---

## 2) venv (standard library virtual environments)

### What venv is

- `venv` is built into Python.
- It creates a project-local environment.
- It’s the most “universal” approach for typical Python apps.

### Basic tutorial (Windows PowerShell)

From the project folder:

1) Create the environment:

- `python -m venv .venv`

2) Activate it:

- `./.venv/Scripts/Activate.ps1`

If PowerShell blocks activation scripts, you can allow them (current user) with:

- `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

3) Confirm you’re using the venv interpreter:

- `python -c "import sys; print(sys.executable)"`

You should see a path containing `.venv`.

4) Install dependencies:

- `python -m pip install -r requirements.txt`

5) Deactivate:

- `deactivate`

### Basic tutorial (macOS/Linux)

1) Create:

- `python3 -m venv .venv`

2) Activate:

- `source .venv/bin/activate`

3) Install:

- `python -m pip install -r requirements.txt`

4) Deactivate:

- `deactivate`

### Recommended project conventions

- Name the folder `.venv/` (common convention)
- Add `.venv/` to `.gitignore`
- Keep dependencies in one of:
  - `requirements.txt` (simple)
  - `pyproject.toml` (modern)

---

## 3) uv (fast environments + dependency workflows)

`uv` is a modern tool that can:

- create virtual environments
- install packages quickly (pip-compatible)
- manage dependencies via `pyproject.toml` in many workflows

If you see projects using `uv`, it’s usually because it is **fast** and offers a clean developer experience.

### Basic tutorial (pip-style)

1) Install uv (one-time, choose one):

- Using pip (simple, but global): `python -m pip install uv`

2) Create a venv:

- `uv venv .venv`

3) Activate the venv (same as venv):

- Windows PowerShell: `./.venv/Scripts/Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

4) Install packages (pip-compatible):

- `uv pip install requests`
- `uv pip install -r requirements.txt`

### Basic tutorial (project-based)

Many `uv` projects use a `pyproject.toml` and lock file.

1) Initialize a project (creates `pyproject.toml`):

- `uv init`

2) Add dependencies:

- `uv add requests`

3) Create/sync the environment from the project definition:

- `uv sync`

4) Run commands inside the managed environment:

- `uv run python -c "import requests; print(requests.__version__)"`

### Where uv fits

- Great default for new projects if your team uses it
- Especially nice when you want “one tool” to create env + install + run

---

## 4) conda and Anaconda

### What conda is

- `conda` is an **environment manager** and a **package manager**.
- It can install packages that are not pure Python (compiled libraries, system-like dependencies).

### What Anaconda is

- **Anaconda** is a distribution that includes Python + conda + many data-science packages.
- **Miniconda** is a smaller distribution: conda + minimal Python.

In many modern setups:

- install **Miniconda** (or a similar lightweight conda distribution)
- create a fresh env per project

### Basic tutorial

Create an environment with a specific Python version:

- `conda create -n myenv python=3.13`

Activate:

- `conda activate myenv`

Install packages:

- `conda install numpy`

You can also use pip inside a conda environment if needed:

- `python -m pip install requests`

Deactivate:

- `conda deactivate`

Export environment (shareable):

- `conda env export > environment.yml`

Recreate later:

- `conda env create -f environment.yml`

### Important caution: mixing conda and pip

Mixing is sometimes necessary, but follow this rule of thumb:

- Prefer `conda install ...` first
- Use `pip` only for packages that conda can’t provide

If you mix heavily, write down the exact steps (or export to `environment.yml`) so others can reproduce.

### Where conda fits

- Data science stacks, scientific computing
- When you need compiled/native dependencies that are painful with pip alone

---

## 5) Virtual environments vs Docker

### What Docker is (and is not)

- A **virtual environment** isolates **Python packages**.
- A **Docker container** isolates the **whole runtime**: OS libraries, system packages, Python, and your app.

Docker solves problems that venv/conda do not:

- “This app needs Ubuntu + system library X + Python 3.13 + package Y”
- reproducible deployments
- consistent runtime across machines and CI

### When to use which

Use **venv** when:

- you’re building a typical Python project
- dependencies are pure Python or easy wheels
- you want the simplest standard solution

Use **uv** when:

- your team wants a fast, modern dependency workflow
- you want consistent installs + an easy `run` experience

Use **conda** when:

- you work with heavy scientific stacks (NumPy/SciPy, ML libraries, compiled tooling)
- you hit build errors installing native dependencies via pip

Use **Docker** when:

- you must match a production runtime exactly
- you need OS-level dependencies (databases, system libraries, services)
- you are deploying a web app / API and want reproducible builds

A common real-world pattern is:

- venv/uv/conda for day-to-day local development
- Docker for deployment and CI reproducibility

---

## 6) VS Code + Jupyter: pick the right interpreter

In VS Code:

- Select the interpreter for the workspace (so terminals, linting, and run/debug use the same env)
- For notebooks, select the **kernel** (often the same env, but it is a separate selection)

If a notebook can’t see your installed packages, you may need `ipykernel` installed in the environment:

- `python -m pip install ipykernel`

Then re-select the kernel.

---

## 7) Quick troubleshooting checklist

If installs “work” but imports fail:

1) Check which Python is running:

- `python -c "import sys; print(sys.executable)"`

2) Check which pip is installing into:

- `python -m pip --version`

3) If you’re in VS Code, ensure the interpreter matches your environment.

4) If you’re in a notebook, ensure the kernel matches your environment.
