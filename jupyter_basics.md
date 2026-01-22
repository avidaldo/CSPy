# Introduction to Jupyter Notebooks

## What are Jupyter Notebooks?

Jupyter Notebooks are open-source web applications that allow you to create and share documents that contain live code, equations, visualizations, and narrative text. They are widely used for data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

The name "Jupyter" comes from the core supported programming languages: **Ju**lia, **Py**thon, and **R**.

## How they work

A notebook is composed of a sequence of **cells**. The two most common types of cells are:

1.  **Code Cells**: These contain code to be executed in the kernel. When executed, the code is run, and the output is displayed directly below the cell.
2.  **Markdown Cells**: These contain text formatted using Markdown (like this document). They are used for narration, explanations, and adding context to the code.

### The Kernel

Behind every notebook running in an environment (like VS Code or a browser), there is a **kernel**. The kernel is a computational engine that executes the code contained in the notebook cells. When you "run" a cell, the code is sent to the kernel, executed, and the results are returned to the notebook interface.

## Under the Hood: The `.ipynb` Format

Although you view notebooks as a nice interactive interface, the file itself (with the `.ipynb` extension) is actually a plain text file in **JSON** (JavaScript Object Notation) format.

If you were to open a `.ipynb` file in a simple text editor rather than a notebook viewer, you would see a structured collection of keys and values representing the cells, source code, outputs, and metadata.

## Metadata and key considerations for Version Control (Git)

Because Jupyter Notebooks are JSON files, they store more than just your code `source`. They also store:

*   **Cell Outputs**: The images, text, or tables generated when you run the code.
*   **Execution Counts**: The number `[1]`, `[2]`, etc., next to code cells, indicating the order in which they were run.
*   **Widget State**: If you use interactive widgets.
*   **Kernel Metadata**: Information about the specific environment used.

### Be careful with Git!

This structure presents a challenge when working with version control systems like **Git**:

1.  **Noise in Diffs**: If you run a notebook and simply re-execute cells without changing the code, the **execution count** changes (e.g., from `null` to `1` or `1` to `5`). Git recognizes this as a change to the file.
2.  **Large Diffs from Outputs**: If your code generates a large graph or a long table, all that data is embedded into the JSON file. A small change in code might result in a massive change in the file size and diff if the output changes.
3.  **Conflicts**: Merging notebooks with conflicts in the JSON structure or metadata can be very difficult compared to merging plain text code files.

**Best Practice**: It is often recommended to clear the outputs of your notebook before committing changes to Git, unless the output itself is a crucial part of what you want to preserve for others to see. This keeps the diffs clean and focuses on the code and documentation changes.
