# "I know this is trash; I don’t even know why I made this—probably inspired by the Einstein two-door puzzle, but with a cat twist LOL"

# Junk - Universal Cleanup Executor

```bash
junk
```

<img width="1584" height="396" alt="Junk-modified" src="https://github.com/user-attachments/assets/f3285a85-ceab-4091-91d1-04d65305daa8" />

[![PyPI version](https://badge.fury.io/py/junk-remover-cli.svg)](https://pypi.org/project/junk-remover-cli/)
[![Python Version](https://img.shields.io/pypi/pyversions/junk-remover-cli.svg)](https://pypi.org/project/junk-remover-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A zero-friction Python CLI tool for automated cleanup of unwanted files and directories.


## Problem Statement

Development repositories often accumulate unwanted files and directories:
- `/target/` build directories
- `*.log` files
- `__pycache__/` Python cache directories  
- `/temp/` temporary directories
- Build artifacts and cache files

Manual deletion of these files is time-consuming and error-prone. Organizations need an automated solution that works universally across different project types and environments.

## Solution Overview

**Junk** is a PyPI-distributed command-line tool that provides automated cleanup with zero user intervention required.

Execute with a single command:
```bash
junk
```

The tool operates by:
1. Locating a `junk.fat` configuration file in the current directory
2. Reading the specified list of files and directories for removal
3. Executing deletions as specified
4. Self-removing the configuration file upon successful completion

## Installation

Install from the Python Package Index:
```bash
pip install junk-remover-cli
```

The tool is immediately available system-wide:
```bash
junk
```

## Usage Instructions

### Step 1: Create Configuration File

Create a `junk.fat` file in your project root directory. List files and directories to be removed, one per line:

*Use a AI Agent to create junk.fat*

```AI AGENT

List junk files (that is no longer need for production) and folders as root-prefixed paths, one per line save as junk.fat

```

```
images/
__pycache__/
*.log
.DS_Store
.env.example
node_modules/
test_pinecone.py
check_pinecone.py
```

### Step 2: Execute Cleanup

Run the cleanup command:
```bash
junk
```

### Step 3: Verification

All specified items are removed, and the `junk.fat` configuration file is automatically deleted upon successful completion.

## Key Features

- **Zero User Interaction**: No confirmation prompts or manual intervention required
- **Universal Compatibility**: Functions in any directory containing a `junk.fat` configuration file
- **Self-Managing**: Automatically removes configuration file after successful execution
- **Error Handling**: Preserves configuration file when deletions fail for retry capability
- **Cross-Platform**: Compatible with Windows, macOS, and Linux environments
- **Encoding Support**: Handles multiple file encodings automatically

## Operational Behavior

### Success Case
When all specified items are successfully deleted, the `junk.fat` configuration file is automatically removed.

### Partial Failure Case  
When some items cannot be deleted, the `junk.fat` configuration file is preserved to allow for retry operations.

### Missing Configuration Case
When no `junk.fat` file is present, the tool exits gracefully with an informative status message.

## Integration with Development Workflows

This tool is designed for integration with automated development workflows:
- **Configuration Generation**: AI code assistants or scripts generate project-specific `junk.fat` files
- **Execution**: The junk tool executes cleanup operations without human intervention
- **Universal Application**: Consistent workflow across different programming languages and project types

## Configuration Examples

### Web Development Projects
```
node_modules/
dist/
.cache/
*.log
.DS_Store
```

### Python Projects
```
__pycache__/
*.pyc
.pytest_cache/
build/
*.egg-info/
```

### Java Projects
```
target/
*.class
*.jar
*.war
```

## Safety and Security

- Operations are limited to explicitly listed items in the configuration file
- No wildcard expansion or pattern matching beyond exact path specification
- Non-existent files and directories are gracefully ignored
- Comprehensive logging provides clear feedback on all operations performed

## License

This project is distributed under the MIT License. See the LICENSE file for complete terms and conditions.

## Contributing

Contributions are welcome through standard open-source channels. This tool maintains a focused scope centered on the core principle of zero-friction cleanup execution. Please ensure any proposed changes align with this fundamental design philosophy.

## Support

For issues, feature requests, or technical support, please utilize the project's issue tracking system on the source code repository.

---

Made by 🪙
