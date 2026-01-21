# VS Code Basics (for Python + Git + Copilot)

## 1) Opening a project correctly

In VS Code you normally work with a **folder** (a project) rather than individual files.

- **Open Folder**: `File → Open Folder...`
- **Workspace trust**: if VS Code asks whether you trust the folder, choose *Trust* only for folders you control.

Tip: if you open a random file without opening the folder, many features (Git, tests, search, Copilot context) will work poorly.

## 2) Settings (User vs Workspace)

VS Code settings exist at two main scopes:

- **User settings**: apply to all projects on your machine.
- **Workspace settings**: apply only to the current folder/repo (good for class repos).

### Open the Settings UI

- You can search settings by name (e.g., `format on save`, `python default interpreter`).

### Edit `settings.json`

Sometimes it’s better to use the JSON form so settings are explicit and easy to share.

- Open Command Palette: `Ctrl+Shift+P`
- Run: **Preferences: Open User Settings (JSON)** or **Preferences: Open Workspace Settings (JSON)**

Common classroom-friendly settings:

- `Files: Auto Save` (pick `afterDelay` for beginners)
- `Git: Autofetch` (keeps your local view in sync)

## 3) The integrated terminal

- Open terminal: `Terminal → New Terminal` (or `Ctrl+``)
- The terminal opens *inside* the folder you opened in VS Code.

For Python projects, learn to:

- run scripts
- run tests

## 4) Git in VS Code (Source Control view)

VS Code has a Git UI that covers 90% of the daily workflow.

### The Source Control panel

- Open **Source Control**
- You’ll see:
  - changed files
  - diffs
  - staging area
  - commit message box

### The “safe” daily routine

1. **Pull / Sync before you start** (avoid conflicts)
2. Make changes
3. **Stage** the files you intend to include
4. **Commit** with a descriptive message
5. **Push / Sync**

### Common UI actions

- Stage a file: click **+** next to it
- Stage everything: click **+** next to “Changes”
- Discard changes: click the rollback icon (be careful)
- Create/switch branch: click the branch name in the status bar

When you’re confused, use the terminal equivalents (`git status`, `git diff`, `git log`) to understand what’s happening.

## 5) GitHub Copilot in VS Code

Copilot can help in two main ways:

- **Inline suggestions** while typing
- **Chat / Edit / Agent workflows** (depending on your VS Code + Copilot version)

### Enable Copilot

- Install the **GitHub Copilot** extension
- Sign in with GitHub
- Ensure you have an active Copilot license (personal or organization)

### Inline suggestions (autocomplete)

- Accept: `Tab`
- Dismiss: `Esc`
- Cycle alternatives: check your keybindings (varies by setup)

Use inline suggestions for small, local edits (one function, a few lines).

### Chat / Edit / Agent modes (how to choose)

VS Code versions differ, but the idea is consistent:

- **Chat**: ask questions, get explanations, explore options
- **Edit**: apply changes to selected files / areas with supervision
- **Agent**: ask for multi-step, multi-file work (planning + implementation)

Rule of thumb:

- Use **Chat** to clarify requirements and edge cases.
- Use **Edit** when you already know *what* to change.
- Use **Agent** when you want a small “mini project” done end-to-end.

### Selecting a model

If your Copilot setup offers multiple models, you’ll typically see a **model picker** in the Copilot Chat UI. Prefer:

- a stronger reasoning model for architecture/refactors
- a faster model for small edits and quick iterations

If you don’t see a model picker, your plan (or organization policy) may be restricting model choice.

## 6) Using an `AGENTS.md` file

An `AGENTS.md` file is a simple way to tell an AI assistant:

- the goals of the repo (teaching vs production)
- coding standards
- what “done” means

A good `AGENTS.md` is short and specific.

### Example template

```markdown
# Agent instructions

- All student-facing text must be clear, correct English.
- Prefer small, step-by-step notebooks over long cells.
- For Python code: target Python ≥3.13 and use modern type hints.
- Avoid adding new dependencies unless needed.
- If you change links in a README, verify the target path exists.
```

## 7) Prompting basics (practical patterns)

A strong prompt usually includes:

- **Goal**: what you want
- **Context**: where in the repo / which files
- **Constraints**: style, libraries, versions
- **Acceptance criteria**: how to know it’s correct

Examples:

- “Update the navigation in `CSPy/CSPy/README.md` so all links resolve from that folder. Keep it a short bullet list.”
- “Create a new notebook introducing Python functions. Use small cells, show outputs, and add markdown explanations between steps.”

## 8) “Vibe coding” (and how to keep it safe)

“Vibe coding” usually means: iterate quickly with AI suggestions, then refine.

To keep it reliable:

- ask for small changes per iteration
- run the code (or at least validate links)
- keep diffs reviewable
- don’t accept changes you can’t explain
