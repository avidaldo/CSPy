# GitHub Copilot in VS Code: Basics & Effective Use

## 1. Core Concepts

### The Agent Loop

At the heart of Copilot is the **agent loop**: a cycle where the AI receives a goal, analyses the codebase, invokes tools (file reads, terminal commands, web searches…), observes their output, and decides what to do next. This repeats until the task is complete or the agent asks for user input. Understanding this loop helps you craft better prompts: the more clearly you state the *goal*, the better the loop converges.

### Language Models

Copilot is **multi-model**. You can switch the underlying LLM on a per-session basis (e.g. GPT-4.1, Claude Sonnet, Gemini…) via the model picker in the Chat panel. Different models have different strengths — some excel at planning, others at code generation or reasoning. The model can also be set per-task inside prompt files (see §3).

## 2. Agent Environments: Local, CLI, Cloud, Third-Party

Agents can run in different **environments**, each with different trade-offs between interactivity, isolation, and collaboration.

| Environment | Runs where | Interactive? | Key use case |
|:---|:---|:---|:---|
| **Local Agent** | Inside your VS Code editor | Yes — you see every edit in real time | Day-to-day coding, refactoring, debugging |
| **Copilot CLI** | Background process on your machine | Minimal — works autonomously | Proof-of-concepts, batch tasks, parallel work |
| **Cloud Agent** | Remote (GitHub infrastructure) | No — submits a Pull Request when done | Team collaboration, async tasks, CI-like workflows |
| **Third-Party** | Via extensions (Anthropic, OpenAI…) | Varies | Alternative models, specialized capabilities |

### Local Agents (default)

Run interactively within your editor loop. The built-in local agents include:

- **Agent mode** (default): Autonomously implements changes across files, runs terminal commands, invokes tools, and self-corrects based on linter/compiler feedback.
- **Ask mode**: Answers questions about concepts or your codebase **without** making file changes.
- **Plan mode** (see §6): Analyses the codebase and creates a structured, step-by-step implementation plan before writing any code.

### Copilot CLI

Runs autonomously in the background on your local machine. Useful when you want to:

- Fire off a task and keep working on something else.
- Can use **Git worktrees** (see §8) to isolate the agent's work on a separate branch without touching your working copy.

### Cloud Agents

Run remotely on GitHub infrastructure. They:

- Clone the repository in a cloud environment.
- Implement the requested changes autonomously.
- Automatically create a **Pull Request** with the result.
- Are ideal for team collaboration and asynchronous workflows.

For details on pull requests, code review, and the fork workflow that cloud agents interact with, see [GitHub Collaborative Workflows](git/github_workflows.md).

### Third-Party Agents

Available via VS Code extensions. They can provide agents from providers like Anthropic and OpenAI, bringing alternative models and specialized capabilities.

### Handing Off Between Environments

You can **hand off** a session from one environment to another. For example, a local Plan agent can generate a detailed plan and then hand it off to a Cloud agent to implement and submit as a Pull Request.

## 3. Customization

VS Code provides several mechanisms to make Copilot natively match your project's conventions. The two most important are **instruction files** and **prompt files**.

### Instruction Files

Instruction files define **project-wide coding conventions** that are applied **automatically** to every chat session as background context. Examples: "use Python ≥ 3.13", "prefer functional style", "always write docstrings".

There are different scopes for instructions:

| Scope | File / Setting | Applied to |
|:---|:---|:---|
| **Repository-wide** | `.github/copilot-instructions.md` | All sessions in this workspace |
| **Folder-specific** | `AGENTS.md` (or similar) in any subdirectory | Sessions touching files in that subtree |
| **User-level** | VS Code setting `github.copilot.chat.codeGeneration.instructions` | All your workspaces (personal preference) |

### `AGENTS.md` vs `.github/copilot-instructions.md`

Both serve as instruction files, but they differ in scope and portability:

- **`.github/copilot-instructions.md`** is the **officially supported**, repository-wide configuration file. Copilot reads it natively and applies its contents to every session in the workspace. It is GitHub Copilot-specific.

- **`AGENTS.md`** is a more **tool-agnostic** convention. It can be placed in any directory to provide *localized* instructions for that subtree. Copilot natively discovers and reads `AGENTS.md` files, but the convention is also recognized by other AI coding tools (Claude Code, Gemini CLI, Cursor…), making it a **portable** choice for multi-tool teams. You can use both: a global `.github/copilot-instructions.md` for Copilot-specific settings and `AGENTS.md` files scattered through the repo for folder-specific context that works across tools.

### Prompt Files (`.prompt.md`)

Prompt files encode **common, repeatable tasks** as Markdown files. Unlike instructions, you invoke prompt files **manually** using slash commands in chat (e.g., `/create-api`).

Key features:
- Stored by default in `.github/prompts/`.
- Support **YAML frontmatter** to specify which model, agent mode, and tools should be used for that specific task.
- Can **reference other files** (e.g., `[schema](../db/schema.sql)`) to pull additional context.
- Are version-controlled and shareable across the team.

Example prompt file (`.github/prompts/create-api.prompt.md`):

```markdown
---
mode: agent
tools: ['githubRepo', 'codebase']
model: gpt-4.1
---

Create a new REST API endpoint based on the following spec.
Follow the patterns in #file:src/routes/users.ts.
Write tests in the `__tests__` directory using the project's existing test framework.
```

### Custom Agents

You can create **dedicated agent personas** with restricted tool sets and specific models, defined as `.agent.md` files. These are useful for specialized workflows like security reviews, documentation generation, or database migrations.

### Agent Skills

Portable capabilities with scripts that work across VS Code, CLI, and Cloud environments. They allow agents to perform specific, well-defined tasks.

### MCP Servers (Model Context Protocol)

MCP extends agents with **external tools** via a standardized protocol. Examples: database queries, API calls, Jira integration, Figma design extraction. MCP servers can be configured at user or workspace level in `settings.json` or `.vscode/mcp.json`.

### Hooks

Custom shell commands executed at specific events in the agent's lifecycle (e.g., before/after file save, before terminal command execution). Useful for enforcing formatting, running linters, or triggering builds automatically.

## 4. Context and Context Engineering

Context is the information the AI sees when processing your request. **Context engineering** — deliberately shaping what the model sees — is the single most important skill for effective Copilot use.

### How Context Is Assembled

Copilot automatically gathers **implicit context** from:

- The currently open and visible files.
- The active selection and cursor position.
- Workspace structure and file names.
- Diagnostics (errors, warnings) from the language server.
- Terminal output from recent commands.
- Instruction files (`.github/copilot-instructions.md`, `AGENTS.md`).
- **Memory** (see §5).

### Workspace Indexing

Copilot builds a **semantic index** of your workspace to support `#codebase` queries and autonomous file discovery. This uses embeddings to find relevant code even when you don't specify exact file names. The index is built incrementally and cached locally.

### Context Window Management

Models have a limited **context window** (the total amount of text they can process). As a conversation grows, several problems emerge:

- **Context drift.** The model gradually loses focus on the original goal. Early instructions and constraints get "pushed away" by newer messages, causing the agent to forget what it was doing or contradict earlier decisions.
- **Noise dilution.** Irrelevant material — old error traces, abandoned approaches, unrelated files — competes for attention with the information that actually matters. The more noise, the less reliably the model uses the right context.
- **Hallucination risk.** When the window is saturated, the model is more likely to fabricate details rather than admitting it can no longer see the relevant source.

Copilot mitigates this automatically by prioritizing the most relevant context, but you should actively help:

- Be specific about which files matter (`#file:path/to/file.py`).
- Keep instruction files concise.
- Structure prompts clearly so the model doesn't waste context on ambiguity.
- Use **`/compact`** to summarize the conversation history, freeing up context space without losing the thread of the session (see Chat Commands below).
- Start a **new session** (`/clear`) when switching to an unrelated task instead of reusing a long conversation.

## 5. Memory

Agents can **remember** facts across sessions through two mechanisms:

- **Memory tool**: The agent can proactively save important context (project conventions, user preferences, architectural decisions) to a local memory store. These memories are automatically retrieved in future sessions.
- **Copilot Memory** (cloud-backed): Persists across machines, synced with your GitHub account.

You can review and manage stored memories via the command palette. Memory is especially useful for long-running projects where the agent learns your preferences over time.


## 6. Planning

The **Plan mode** is designed for complex, multi-step tasks. When activated:

1. The agent analyses the codebase and the request.
2. It produces a structured **implementation plan** — a checklist of steps to accomplish the goal.
3. You review and can edit the plan before execution.
4. Once approved, the agent (or a Cloud agent) implements it step by step.

Planning is recommended for:
- Major refactors that touch many files.
- Feature implementations where you want to validate the approach before code is written.
- Tasks that benefit from breaking down into smaller, verifiable steps.

---

## 7. Tools

Tools are the **capabilities** agents use to interact with the world. They are the bridge between the model's reasoning and actual actions.

### Built-in Tools

| Tool | Purpose |
|:---|:---|
| `editFiles` | Read and write files in the workspace |
| `runTerminalCommand` | Execute shell commands |
| `searchCodebase` | Semantic search across the workspace index |
| `searchWeb` | Web search for documentation, APIs, etc. |
| `useBrowser` | Open and interact with web pages |
| `memory` | Store and retrieve information across sessions |

### MCP Server Tools

External tools provided via the Model Context Protocol (see §3). These can add capabilities like database queries, API calls, or integration with external services.

### Extension Tools

VS Code extensions can register tools that agents can invoke, extending the agent's abilities with language-specific or domain-specific functionality.

---

## 8. Git Worktrees and Isolated Agent Work

**Git worktrees** allow you to check out multiple branches of the same repository simultaneously in different directories. This is particularly useful with Copilot agents:

- **Copilot CLI** can work in a worktree, making changes on a separate branch without disturbing your main working copy.
- You can fire off a background agent task on a worktree and continue your own work in the main checkout.
- When the agent finishes, you review its branch and merge (or discard) as needed.

VS Code has first-class support for worktrees in the Source Control panel (see *Branches & Worktrees* in the VS Code docs).

---

## 9. Chat Surfaces and Workflows

### Chat Panel (main)

The primary interface. Supports agent mode, ask mode, and plan mode. Conversations are persistent and can be resumed.

### Inline Chat

Press `Ctrl+I` (or `Cmd+I` on macOS) to open a lightweight chat overlay directly in the editor. Ideal for quick, localized edits ("rename this variable", "add error handling here"). The model sees the surrounding code automatically.

### Quick Chat

A transient, floating chat window for fast questions without opening the full panel.

### Chat Sessions

Conversations are organized into **sessions**. Each session maintains its own context and history. You can:
- Start new sessions for unrelated tasks.
- Restore previous sessions to continue earlier work.

### Chat Commands (Slash Commands)

Typing `/` in the chat input reveals a menu of built-in slash commands. The most useful ones:

| Command | Purpose |
|:---|:---|
| `/compact` | Summarize the current conversation to free up context-window space without starting over. |
| `/clear` | Reset the conversation, discarding all history and context. |
| `/new` | Scaffold a new project or file structure from a description. |
| `/fix` | Diagnose and propose patches for errors in the selected code. |
| `/explain` | Explain the selected code or concept. |
| `/tests` | Generate unit tests for the selected code. |
| `/doc` | Generate documentation (docstrings, JSDoc, READMEs…). |
| `/model` | Switch the underlying language model for the current session. |

> **Tip:** In Copilot CLI sessions, additional commands are available: `/resume` (continue a previous session) and `/compact` (especially important there, since CLI sessions tend to accumulate long histories).

### Reviewing Edits

Copilot shows proposed changes as diffs. You can:
- **Accept** or **reject** individual edits.
- Use **checkpoints** to snapshot the workspace state before an agent starts working, and roll back if needed.

---

## 10. Inline Suggestions (Autocomplete)

Beyond the chat-based agentic workflow, Copilot still provides **inline code suggestions** as you type. These are context-aware completions that appear as ghost text in the editor. You accept them with `Tab`.

Tips for better suggestions:
- Write a clear comment or docstring before the code — the model uses it as a prompt.
- Open related files so the model picks up patterns from your codebase.
- Use meaningful variable and function names.

---

## 11. Smart Actions

Copilot integrates into VS Code's existing UI with context-sensitive actions:

- **Fix** errors directly from the Problems panel or code diagnostics.
- **Explain** selected code via the right-click context menu.
- **Generate** tests, documentation, or commit messages.
- **Refactor** code with AI-powered suggestions.

---

## 12. Best Practices for Effective Use

1. **Be specific in your prompts.** Vague requests produce vague results. Include file paths, function names, and constraints.
2. **Use instruction files.** Invest time in writing a good `.github/copilot-instructions.md` and `AGENTS.md` files. They pay off on every interaction.
3. **Reference context explicitly.** Use `#file`, `#codebase`, and `#problems` to guide the model to the right information.
4. **Plan before implementing.** For complex tasks, use Plan mode to validate the approach.
5. **Review diffs carefully.** The agent can make mistakes. Always review before accepting changes.
6. **Use checkpoints.** Before a large agent task, create a checkpoint so you can roll back.
7. **Iterate.** If the first result isn't right, provide feedback and ask the agent to adjust.
8. **Choose the right model.** Different models have different strengths. Experiment with the model picker.
9. **Use worktrees for parallel work.** Keep your main branch clean while the agent works on a feature branch.
10. **Write prompt files for recurring tasks.** If you scaffold components, run reviews, or generate boilerplate often, encode the workflow in a `.prompt.md` file.

---

*References:*
- [VS Code Copilot Overview](https://code.visualstudio.com/docs/copilot/overview)
- [Agents Concepts](https://code.visualstudio.com/docs/copilot/concepts/agents)
- [Context Concepts](https://code.visualstudio.com/docs/copilot/concepts/context)
- [Tools Concepts](https://code.visualstudio.com/docs/copilot/concepts/tools)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Copilot CLI](https://code.visualstudio.com/docs/copilot/agents/copilot-cli)
- [Cloud Agents](https://code.visualstudio.com/docs/copilot/agents/cloud-agents)
- [Planning](https://code.visualstudio.com/docs/copilot/agents/planning)
- [Memory](https://code.visualstudio.com/docs/copilot/agents/memory)
- [Context Engineering Guide](https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide)
