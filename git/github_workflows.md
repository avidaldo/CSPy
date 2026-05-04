# GitHub Collaborative Workflows

## 1. Branches

A **branch** is an independent line of development. Think of it as a parallel copy of your project where you can make changes without affecting the main codebase.

### Why use branches?

- **Isolation**: Work on a feature or bug fix without risking the stability of `main`.
- **Parallel work**: Multiple people (or tasks) can progress simultaneously.
- **History clarity**: Each branch tells a story about a single piece of work.

## 2. Forks

A **fork** is a full copy of a repository under your own GitHub account. Unlike a branch (which lives inside the original repository), a fork is a completely separate repository that you own and control.

### Fork vs. Branch

| | Branch | Fork |
|---|---|---|
| **Where it lives** | Inside the original repository | In your own GitHub account |
| **Who can create one** | Collaborators with write access | Anyone |
| **Typical use case** | Team members working on the same project | Contributing to a project you don't own |
| **Merging back** | `git merge` or PR within the same repo | Pull Request from your fork to the original |

### When to use a fork

- **Open-source contributions**: You don't have write access to the upstream repository.
- **Experimenting safely**: You want to try large changes without affecting the original.
- **Classroom assignments**: The instructor owns the template repository; students fork it.

### Creating a fork

1. Go to the repository on GitHub.
2. Click the **Fork** button (top-right).
3. GitHub creates a copy under your account (e.g., `your-username/project`).

## 3. Pull Requests (PRs)

A **Pull Request** is a proposal to merge changes from one branch (or fork) into another. It is the central mechanism for collaboration on GitHub: it bundles your code changes, a description, a discussion thread, and (optionally) automated checks into a single reviewable unit.

### Creating a Pull Request

1. Push your branch to GitHub:
   ```bash
   git push origin feature/add-login
   ```
2. Go to the repository on GitHub. You will see a banner: **"Compare & pull request"**. Click it.
3. Fill in:
   - **Title**: A concise summary (e.g., "Add user login page").
   - **Description**: Explain *what* you changed and *why*. Reference the Issue if there is one (e.g., "Closes #42").
   - **Reviewers**: Assign team members to review your code.
4. Click **Create pull request**.

**From a fork**: The process is the same, but the PR targets the *upstream* repository's branch instead of your own.

### Anatomy of a good Pull Request

| Element | Good example | Bad example |
|---------|-------------|------------|
| **Title** | "Add password validation to login form" | "Changes" |
| **Description** | Explains the approach, links to Issue #12 | Empty |
| **Scope** | One focused change (login validation) | 5 unrelated features in one PR |
| **Size** | ~100–300 lines changed | 2,000+ lines |

Small, focused PRs are reviewed faster, contain fewer bugs, and are easier to merge.

### Draft Pull Requests

If your work is still in progress and you want early feedback (or to trigger automated tests), open a **Draft PR**. Draft PRs:
- Signal that the code is not ready for final review.
- Allow teammates to comment and suggest changes early.
- Can be converted to a regular PR when you are ready.

### `CONTRIBUTING.md` and PR templates

Many projects include a `CONTRIBUTING.md` file that explains how to contribute: branching conventions, commit-message format, testing requirements, etc. Always check for this file before opening your first PR.

Projects can also provide **PR templates** (stored in `.github/PULL_REQUEST_TEMPLATE.md`) that pre-fill the description with a checklist or structure.

## 4. Code Review

Code review is the process of having another person examine your changes before they are merged. It is one of the most valuable practices in software development.

### Why review code?

- **Quality**: Catch bugs, logic errors, and edge cases before they reach `main`.
- **Knowledge sharing**: Reviewers learn about parts of the codebase they didn't write.
- **Consistency**: Enforce team conventions (naming, architecture, style).
- **Learning**: Both the author and the reviewer improve their skills.

### Reviewing a Pull Request

When you are assigned as a reviewer:

1. **Read the description** to understand the intent.
2. Go to the **Files changed** tab.
3. For each file, read the diff and leave comments:
   - **Comment**: General observation or question (non-blocking).
   - **Suggestion**: Propose a specific code change — the author can apply it with one click.
   - **Request changes**: Flag something that must be fixed before merging.
4. When finished, click **Review changes** and choose:
   - **Approve**: The code is ready to merge.
   - **Request changes**: The author needs to address your feedback.
   - **Comment**: General feedback without explicit approval or rejection.

### Resolving conversations

Each comment thread on a PR is a **conversation**. GitHub lets you mark conversations as **Resolved**:
- If you *requested a change*, resolve the conversation after verifying the author's fix.
- If you *asked a question*, resolve it once the answer is provided.

Resolving conversations keeps the PR clean and makes it easy to see what is still outstanding.

## 5. Issues and Project Management

### Issues

An **Issue** is a trackable unit of work: a bug report, a feature request, a task, or a question. Issues are the standard way to plan and discuss work on GitHub.

Key elements of an Issue:
- **Title and description**: What needs to be done and why.
- **Labels**: Categorize work (e.g., `bug`, `enhancement`, `documentation`, `good first issue`).
- **Assignees**: Who is responsible.
- **Milestone**: Group Issues into a release or sprint.

### Linking PRs to Issues

When your PR addresses an Issue, reference it in the PR description using a closing keyword:

```
Closes #42
```

When the PR is merged, Issue #42 is automatically closed. Other keywords that work: `Fixes`, `Resolves`.

## 6. Connecting to AI-Assisted and Spec-Driven Development

The workflows described above are not just "manual" processes — they integrate directly with modern AI-assisted development and spec-driven workflows.

### AI agents and Pull Requests

AI coding agents (like GitHub Copilot's [cloud agents](../github-copilot.md)) can autonomously implement changes and open Pull Requests. The review process is exactly the same: a human reviews the AI-generated PR, leaves comments, requests changes, and approves when satisfied. This makes code review even more important — the human is the quality gate, whether the author is a person or an AI.

### SDD iterations map to GitHub workflows

If you follow [Spec-Driven Development](../software-engineering/sdd_basics.md), each iteration maps naturally to GitHub's collaboration tools:

| SDD phase | GitHub tool |
|-----------|------------|
| Gather requirements | **Issue** — capture the requirement |
| Write/update the spec | **Commit** to a spec file on a branch |
| Build | **Branch** — isolate the implementation work |
| Demo and verify | **Pull Request** — present the changes for review |
| Update the spec | **Issue comments / new Issues** — track feedback |

This alignment means you don't need separate tools for project management and version control — GitHub handles both.

---

## 7. A Typical Contribution Workflow

Here is the end-to-end flow for contributing to a project you don't own (the **fork and PR model**):

```
 ┌──────────────────────────────────────────────────────┐
 │                   UPSTREAM REPO                      │
 │                  (original project)                  │
 └──────────┬──────────────────────────┬────────────────┘
            │  Fork                    ▲  Pull Request
            ▼                          │  (review → merge)
 ┌──────────────────────┐              │
 │    YOUR FORK         │              │
 │  (GitHub copy)       │              │
 └──────────┬───────────┘              │
            │  Clone                   │  Push
            ▼                          │
 ┌──────────────────────────────────────────────────────┐
 │              YOUR LOCAL MACHINE                      │
 │                                                      │
 │   1. git switch -c fix/typo-in-readme                │
 │   2. (make changes)                                  │
 │   3. git add . && git commit -m "Fix typo in README" │
 │   4. git push origin fix/typo-in-readme              │
 │   5. Open PR on GitHub                               │
 └──────────────────────────────────────────────────────┘
```
