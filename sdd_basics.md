# Spec-Driven Development (SDD) & VS Code Workflow

When building software, especially with the help of AI coding assistants, it's easy to start writing code before you fully understand what needs to be built. **Spec-Driven Development (SDD)** is a workflow that prevents this by putting the specification first.

## 1. What is Spec-Driven Development?

Spec-Driven Development is an approach where a formal specification document is the primary driver of every decision: what to build, in what order, and how to verify it is complete.

The central rule is simple:
> *Write the spec first. Then build exactly what the spec says. Then verify against the spec.*

By doing this, the spec becomes the single source of truth, and the code is simply the artifact that satisfies it.

## 2. Key Industry Concepts

Before diving into the workflow, it's important to understand these standard industry terms:

### Proof of Concept (PoC)

A **Proof of Concept** is a minimal, often throwaway implementation built to answer a specific technical or product question: *"Can this actually be done? Does the core idea work?"*

A PoC is **not** meant for production. It trades quality, architecture, and completeness for speed. The goal is to reduce uncertainty and validate assumptions before committing to a full build.

**Key distinction:** A PoC proves an idea is feasible. An MVP delivers actual value to actual users.

### Minimum Viable Product (MVP)

A **Minimum Viable Product** is the simplest version of a product that delivers real value to real users and generates feedback. Every feature in an MVP is there for a reason; nothing extra is built.

Eric Ries, who popularized the term in *The Lean Startup*, defines it as: *"That version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort."*

The word "viable" is important — a PoC is often not viable (a user couldn't actually use it day to day), but an MVP is. It is usable, even if limited.

**Key distinction:** MVP ≠ "bad quality". MVP means minimum *scope*. Quality attributes (correctness, reliability, architecture) still matter.

### Iteration

An **iteration** is a time-boxed cycle of: plan → build → demo → gather feedback → plan again.

Each iteration produces a working increment of the product and ends with a meeting with the stakeholder (client, user representative, or product owner) to:

1. Demonstrate what was built.
2. Validate it against the spec.
3. Collect new requirements, corrections, or priority changes.
4. Update the spec for the next iteration.

Iterations can be driven by time (like in Scrum sprints) or by spec versions (a new major iteration begins when feedback requires a revised spec).

### Technical Debt

**Technical debt** is the accumulated cost of shortcuts taken to deliver faster. Like financial debt, it accrues interest: the longer it stays, the harder it becomes to work with the codebase.

SDD helps control technical debt by keeping scope explicit. When you have a clear spec, you can distinguish between *"this shortcut is deliberate and bounded"* (a PoC decision you plan to revisit) and *"this was never a good idea"* (unintentional debt). Tracking these decisions explicitly (e.g., in an "open questions" document) is a form of honest, controlled technical debt.

## 3. The SDD Lifecycle

A standard SDD iteration follows these phases:

1.  **Gather Requirements**: Understand the problem from the stakeholder/client.
2.  **Write or Update the Spec**: Turn raw notes into structured requirements. A good spec includes Functional Requirements (FRs), Business Rules, Acceptance Criteria, and crucially, **Non-Goals** (what is explicitly *out* of scope).
3.  **Build**: Implement *only* what the spec says. The spec is your shield against "scope creep" (unplanned feature growth).
4.  **Demo and Verify**: Show the software to the stakeholder. Walk through each acceptance criterion to prove it works.
5.  **Update the Spec**: Use the feedback to update the requirements, close open questions, and start the next iteration.

## 4. Why SDD and AI Agents Are a Natural Fit

AI assistants like GitHub Copilot are powerful, but they have a fundamental limitation: **they do not know what you want to build unless you tell them**. SDD solves this perfectly.

*   **Specs as Context**: A structured specification is the perfect AI prompt. "Implement FR-2 from `specs.md`" provides far more accurate results than "Add a login screen".
*   **Bounded Scope**: AI agents often try to be *too* helpful, adding unrequested features ("gold-plating"). The spec's Non-Goals section gives you the authority to reject out-of-scope code.
*   **Verifiable Output**: Because the spec contains Acceptance Criteria, you can immediately test whether the AI-generated code satisfies them.
*   **The Human is the Architect**: The AI handles the typing and implementation details; you own the architecture, trade-offs, and product strategy.

## 5. Basic VS Code Customizations for SDD

To make the most of this workflow, you should customize your VS Code environment. This ensures your tools, your team, and your AI agent are all aligned.

### Workspace Settings (`.vscode/settings.json`)
Store project-specific settings inside the repository so everyone on the team uses the same rules. This prevents arguments over formatting and makes code reviews easier.
```json
{
  "editor.formatOnSave": true,
  "python.analysis.typeCheckingMode": "basic",
  "files.exclude": { "**/__pycache__": true }
}
```

### AI Instruction Files
You can configure VS Code Copilot to automatically read workspace-level instruction files. This makes every chat aware of your SDD workflow.
*   **`.github/copilot-instructions.md`** or **`AGENTS.md`**: Create these files to explain your rules.

**Example Instruction File:**
```markdown
This project follows Spec-Driven Development. The specification is in `specs.md`.
- All changes must satisfy the acceptance criteria in `specs.md`.
- Do not implement features that are not explicitly requested.
- Follow the architecture rules: UI layers must not directly access the database.
```

### Effective Prompting with Specs
When using Copilot Agent mode for multi-file tasks, combine it with your spec:
1.  **Attach the Spec**: Always explicitly include your spec file (e.g., `#file:specs.md`) in the chat.
2.  **Reference the Requirement**: Ask the agent to "Implement FR-3" instead of paraphrasing.
3.  **Provide Acceptance Criteria**: Copy-paste the criteria into the prompt so the agent knows the definition of "done".

## 6. Common Pitfalls

### Spec too vague → AI output too vague

If a spec says *"the system should display stats"*, neither a developer nor an AI agent knows what fields to show, in what format, split by what dimensions, read-only or editable, etc. Good specs are specific enough that a developer could implement a requirement without asking follow-up questions. If you find yourself guessing during implementation, the spec needs more detail.

### Spec too rigid → no room for learning

A spec is not a contract carved in stone. If a client sees the PoC and realizes they actually want something different, the right response is to update the spec, not to defend the old one. Open questions exist precisely because some decisions cannot be made without seeing working software. The spec should be honest about what is known versus what is deferred.

### Implementing beyond the spec

AI agents (and eager developers) may add features that seem useful but were not specified. This is called **gold-plating**, and it creates problems:
- It has not been validated with the client — it may not be what they want.
- It adds code that has no acceptance criteria — it will not be tested.
- It increases the surface area for bugs and maintenance burden.

The Non-Goals section of the spec is your most powerful tool against gold-plating.

### Confusing PoC quality with production quality

A PoC is allowed to have shortcuts: no error handling, no tests, hardcoded values, no migrations. But those shortcuts must be tracked and deliberately removed in the MVP and subsequent iterations. A common failure mode is shipping PoC-quality code as the MVP because "it works". Use the spec's quality attributes section to enforce production standards for the MVP.
