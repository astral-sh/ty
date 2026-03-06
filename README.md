# ty

[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![PyPI](https://img.shields.io/pypi/v/ty.svg)](https://pypi.python.org/pypi/ty)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.com/invite/astral-sh)

An extremely fast Python type checker and language server, written in Rust.

<br />

<p align="center">
  <img alt="Shows a bar chart with benchmark results." width="500px" src="https://raw.githubusercontent.com/astral-sh/ty/main/docs/assets/ty-benchmark-cli.svg">
</p>

<p align="center">
  <i>Type checking the <a href="https://github.com/home-assistant/core">home-assistant</a> project without caching.</i>
</p>

<br />

ty is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [Ruff](https://github.com/astral-sh/ruff).

ty is currently in [beta](#version-policy).

---

## Table of Contents

- [Highlights](#highlights)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Editor Integration](#editor-integration)
- [Configuration](#configuration)
- [Getting Help](#getting-help)
- [Contributing](#contributing)
- [Version Policy](#version-policy)
- [FAQ](#faq)
- [License](#license)

---

## Highlights

### Performance

| Feature | Description |
|---------|-------------|
| **10x - 100x faster** | Significantly faster than mypy and Pyright |
| **Incremental analysis** | Fine-grained [incremental analysis](https://docs.astral.sh/ty/features/language-server/#fine-grained-incrementality) designed for fast IDE updates when editing files |

### Diagnostics & Configuration

| Feature | Description |
|---------|-------------|
| **Rich diagnostics** | Comprehensive [diagnostics](https://docs.astral.sh/ty/features/diagnostics/) with rich contextual information |
| **Configurable rules** | Adjustable [rule levels](https://docs.astral.sh/ty/rules/) (error, warn, ignore) |
| **Per-file overrides** | [Override settings](https://docs.astral.sh/ty/reference/configuration/#overrides) for specific files or patterns |
| **Suppression comments** | [Suppress diagnostics](https://docs.astral.sh/ty/suppression/) inline when needed |
| **Project support** | First-class project support with proper configuration discovery |

### Advanced Type System

| Feature | Description |
|---------|-------------|
| **Intersection types** | First-class [intersection types](https://docs.astral.sh/ty/features/type-system/#intersection-types) for precise type narrowing |
| **Type narrowing** | Advanced [type narrowing](https://docs.astral.sh/ty/features/type-system/#top-and-bottom-materializations) for better control flow analysis |
| **Reachability analysis** | [Sophisticated reachability analysis](https://docs.astral.sh/ty/features/type-system/#reachability-based-on-types) to detect unreachable code |
| **Redeclarations** | Support for [redeclarations](https://docs.astral.sh/ty/features/type-system/#redeclarations) for gradual adoption |
| **Gradual typing** | Designed for [partially typed code](https://docs.astral.sh/ty/features/type-system/#gradual-guarantee) with smooth migration paths |

### IDE & Editor Support

| Feature | Description |
|---------|-------------|
| **Language server** | Full [LSP implementation](https://docs.astral.sh/ty/features/language-server/) with code navigation, completions, code actions, auto-import, inlay hints, and on-hover help |
| **Editor integrations** | Ready-to-use integrations for [VS Code](https://docs.astral.sh/ty/editors/#vs-code), [PyCharm](https://docs.astral.sh/ty/editors/#pycharm), [Neovim](https://docs.astral.sh/ty/editors/#neovim), and more |

---

## Requirements

| Requirement | Details |
|-------------|---------|
| **Python version** | Python 3.8+ (for runtime) or standalone via uvx |
| **Python typing** | Supports typing features up to Python 3.13 |
| **Platforms** | Windows, macOS, Linux |

---

## Getting Started

### Quick Try (No Installation)

Try ty directly in your browser at the [ty playground](https://play.ty.dev).

### Run with uvx (Recommended)

The fastest way to get started is using [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools):

```shell
# Check current directory
uvx ty check

# Check a specific directory
uvx ty check src/

# Check a specific file
uvx ty check main.py

# Show all available commands
uvx ty --help
```

### Install Globally

Install ty as a permanent tool:

```shell
# With pip
pip install ty

# With uv (recommended)
uv tool install ty

# Verify installation
ty --version
```

### Basic Usage Examples

```shell
# Type check your project
ty check

# Check with specific Python version
ty check --python-version 3.11

# Output in different formats
ty check --output-format json
ty check --output-format github-actions

# Show rule documentation
ty rule <rule-name>
```

For comprehensive documentation, see [docs.astral.sh/ty](https://docs.astral.sh/ty/).

---

## Installation

For detailed installation instructions, see the [installation documentation](https://docs.astral.sh/ty/installation/).

### Quick Install Options

| Method | Command | Notes |
|--------|---------|-------|
| **uvx** | `uvx ty check` | No installation needed, runs directly |
| **uv tool** | `uv tool install ty` | Recommended for permanent install |
| **pip** | `pip install ty` | Standard pip installation |
| **pipx** | `pipx install ty` | Isolated environment install |

### Pre-built Binaries

Pre-built binaries are available from the [GitHub Releases](https://github.com/astral-sh/ty/releases) page for Windows, macOS, and Linux.

---

## Editor Integration

ty includes a built-in language server for IDE integration.

### Supported Editors

| Editor | Setup Guide |
|--------|-------------|
| **VS Code** | [VS Code integration guide](https://docs.astral.sh/ty/editors/#vs-code) |
| **PyCharm** | [PyCharm integration guide](https://docs.astral.sh/ty/editors/#pycharm) |
| **Neovim** | [Neovim integration guide](https://docs.astral.sh/ty/editors/#neovim) |
| **Other editors** | See [editor integration docs](https://docs.astral.sh/ty/editors/) |

### Language Server Features

- Code navigation (go to definition, find references)
- Auto-completion with type-aware suggestions
- Code actions and quick fixes
- Auto-import suggestions
- Inlay hints for type annotations
- On-hover documentation

---

## Configuration

ty can be configured via `pyproject.toml`, `ty.toml`, or command-line arguments.

### Minimal Configuration Example

Create a `pyproject.toml` in your project root:

```toml
[tool.ty]
# Minimum Python version to type-check against
python-version = "3.11"

# Global rule settings
[tool.ty.rules]
# Ignore specific rules globally
# unresolved-reference = "ignore"

# Per-file overrides
[tool.ty.overrides]
# "tests/**/*.py" = { rules = { "unresolved-reference" = "ignore" } }
```

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `python-version` | Target Python version for type checking | Project's runtime version |
| `rules` | Global rule level settings | See [rules documentation](https://docs.astral.sh/ty/rules/) |
| `overrides` | Per-file/pattern rule overrides | None |

For complete configuration options, see the [configuration reference](https://docs.astral.sh/ty/reference/configuration/).

---

## Getting Help

| Resource | Link |
|----------|------|
| **Documentation** | [docs.astral.sh/ty](https://docs.astral.sh/ty/) |
| **Issue Tracker** | [GitHub Issues](https://github.com/astral-sh/ty/issues) |
| **Community Chat** | [Discord](https://discord.com/invite/astral-sh) |
| **Typing FAQ** | [Typing FAQ](https://docs.astral.sh/ty/reference/typing-faq) |


---

## Version Policy

ty uses `0.0.x` versioning. ty does not yet have a stable API; breaking changes, including changes
to diagnostics, may occur between any two versions.

See the [type system support](https://github.com/astral-sh/ty/issues/1889) tracking issue for a
detailed overview of currently supported features.

---

## FAQ

<!-- We intentionally use smaller headings for the FAQ items -->

<!-- markdownlint-disable MD001 -->

#### Why is ty doing \_\_\_\_\_?

See our [typing FAQ](https://docs.astral.sh/ty/reference/typing-faq).

#### How do you pronounce ty?

It's pronounced as "tee - why" ([`/tiː waɪ/`](https://en.wikipedia.org/wiki/Help:IPA/English#Key))

#### How should I stylize ty?

Just "ty", please.

<!-- markdownlint-enable MD001 -->

---

## License

ty is licensed under the MIT license ([LICENSE](LICENSE) or
<https://opensource.org/licenses/MIT>).

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in ty
by you, as defined in the MIT license, shall be licensed as above, without any additional terms or
conditions.

---

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/uv/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>