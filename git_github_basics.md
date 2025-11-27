# Git and GitHub Basics: Syncing Your Work

This guide introduces the fundamental concepts of **Git** and **GitHub**, focusing on a practical workflow: keeping your coding projects synchronized between different computers (e.g., school and home).

## 1. Concepts: What are Git and GitHub?

- **Git**: A distributed **Version Control System**. Think of it as a "time machine" for your code. It tracks every change you make, allowing you to save snapshots (commits) of your project history. It runs locally on your computer.
- **GitHub**: A cloud platform that hosts Git repositories. Think of it as a specialized "Google Drive" for code. It allows you to store your repositories online, share them, and synchronize them across devices.

## 2. Prerequisites

Before starting, ensure you have:
1. **Git installed**: [Download Git](https://git-scm.com/downloads)
2. **A GitHub account**: [Sign up](https://github.com/signup)
3. **VS Code installed**: [Download VS Code](https://code.visualstudio.com/)

### First-time Git Configuration
Before using Git, configure your identity (only needed once per computer). Open your terminal (in VS Code: `Ctrl+``) and tell Git who you are. This information will appear in your project history.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 3. Scenario: The Sync Workflow

We will cover the following lifecycle to keep your work in sync:

1. **Initialize**: Start a project on Computer A (School).
2. **Push**: Upload it to GitHub.
3. **Clone**: Download it to Computer B (Home).
4. **Sync Loop**: Work, Commit, Push, Pull.

---

## 4. Step 1: Starting a Project (Computer A)

You have a folder with your code, and you want to turn it into a Git repository.

### Option A: Using the Terminal
Navigate to your project folder and run:

```bash
git init
```
This creates a hidden `.git` folder that tracks changes.

### Option B: Using VS Code GUI
1. Open the **Source Control** view (icon looks like a graph node, or `Ctrl+Shift+G`).
2. Click the **Initialize Repository** button.

---

## 5. Step 2: Saving Changes (Committing)

Git doesn't save automatically. You must explicitly tell it to save a snapshot. This is a two-step process:
1. **Stage**: Choose which files to include.
2. **Commit**: Save the snapshot with a message.

### Option A: Using the Terminal
```bash
# 1. Stage all changes
git add .

# 2. Commit with a descriptive message
git commit -m "Initial project structure"
```

### Option B: Using VS Code GUI
1. In **Source Control**, you will see files under "Changes".
2. Click the **+** icon next to files (or "Changes") to **Stage** them.
3. Type a message in the text box (e.g., "Initial commit").
4. Click **Commit** (the checkmark icon or the blue button).

---

## 6. Step 3: Uploading to GitHub (Pushing)

Now your history is saved locally. Let's send it to the cloud.

1. Go to [GitHub.com](https://github.com) and click the **+** icon -> **New repository**.
2. Name it (e.g., `my-project`). Do **not** check "Initialize with README" (since you already have code).
3. Click **Create repository**.

### Option A: Using the Terminal
Copy the commands shown by GitHub under "…or push an existing repository from the command line":

```bash
# Link your local repo to the remote GitHub repo
git remote add origin https://github.com/YOUR_USERNAME/my-project.git

# Push your code
git push -u origin master
```

### Option B: Using VS Code GUI
1. Open **Source Control**.
2. Click the **Publish Branch** button.
3. Select **Publish to GitHub public/private repository**.
4. Follow the prompts to sign in and select the repo name.

---

## 7. Step 4: Getting the Code (Computer B)

Now you are at home. You need to download the repository.

### Option A: Using the Terminal
```bash
# Download the repository
git clone https://github.com/YOUR_USERNAME/my-project.git
```

### Option B: Using VS Code GUI
1. Open VS Code.
2. On the "Welcome" page, click **Clone Git Repository...** (or press `F1` and type `Git: Clone`).
3. Paste the GitHub URL or choose **Clone from GitHub** to search for your repo.
4. Select a folder on your computer to save it.

---

## 8. The Daily Workflow: Syncing

To avoid conflicts and losing work, follow this strict routine:

### 1. BEFORE you start working (Pull)
Always download the latest changes from the cloud to ensure you have the work you did on the other computer.

- **Terminal**: `git pull`
- **VS Code**: Click the **Synchronize Changes** icon (rotating arrows) in the bottom left status bar, or use the Source Control menu (`...`) -> **Pull**.

### 2. DO your work
Write code, test, debug.

### 3. AFTER you finish working (Commit & Push)
Save your changes locally and upload them to the cloud before leaving.

- **Terminal**:
  ```bash
  git add .
  git commit -m "Finished feature X"
  git push
  ```
- **VS Code**:
  1. Stage changes (+).
  2. Commit with message.
  3. Click **Sync Changes** (or Push).

---

## Essential Commands Summary

| Action | Terminal Command | VS Code |
|--------|------------------|---------|
| **Initialize repo** | `git init` | Source Control → Initialize Repository |
| **Clone repo** | `git clone <url>` | Command Palette → Git: Clone |
| **Check status** | `git status` | Source Control panel shows changes |
| **Stage files** | `git add .` | Click **+** next to files/Changes |
| **Commit** | `git commit -m "message"` | Enter message → Click **✓** |
| **Push** | `git push` | **⋯** → Push or **↑** icon |
| **Pull** | `git pull` | **⋯** → Pull or **↓** icon |


## Best Practices

1. **Commit often**: Make small, focused commits with clear messages
2. **Always pull before starting work**: Avoid conflicts by syncing first
3. **Write descriptive commit messages**: "Fix bug in calculate_average function" is better than "fix stuff"
4. **Push regularly**: Don't wait too long—push at the end of each work session
5. **Don't commit sensitive data**: Never push passwords, API keys, or personal information

## Useful Links
- [Official GitHub Documentation](https://docs.github.com/en/get-started)
- [VS Code Version Control Docs](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
