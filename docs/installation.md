# Installing ty

## Running ty without installation

Use [uvx](https://docs.astral.sh/uv/guides/tools/) to quickly get started with ty:

```shell
uvx ty
```

## Installation methods

### Adding ty to your project

!!! tip

    Adding ty as a dependency ensures that all developers on the project are using the same version
    of ty.

Use [uv](https://github.com/astral-sh/uv) (or your project manager of choice) to add ty as a
development dependency:

```shell
uv add --dev ty
```

Then, use `uv run` to invoke ty:

```shell
uv run ty
```

To update ty, use `--upgrade-package`:

```shell
uv lock --upgrade-package ty
```

### Installing globally with uv

Install ty globally with uv:

```shell
uv tool install ty@latest
```

To update ty, use `uv tool upgrade`:

```shell
uv tool upgrade ty
```

### Installing globally with pipx

Install ty globally with pipx:

```shell
pipx install ty
```

To update ty, use `pipx upgrade`:

```shell
pipx upgrade ty
```

### Installing with pip

Install ty into your current Python environment with pip:

```shell
pip install ty
```

### Installing in Docker

Install ty in Docker by copying the binary from the official image:

```dockerfile title="Dockerfile"
COPY --from=ghcr.io/astral-sh/ty:latest /ty /bin/
```

The following tags are available:

- `ghcr.io/astral-sh/ty:latest`
- `ghcr.io/astral-sh/ty:{major}.{minor}.{patch}`, e.g., `ghcr.io/astral-sh/ty:0.0.2`
- `ghcr.io/astral-sh/ty:{major}.{minor}`, e.g., `ghcr.io/astral-sh/ty:0.0` (the latest patch
    version)

## Adding ty to your editor

See the [editor integration](./editors.md) guide to add ty to your editor.

## Shell autocompletion

!!! tip

    You can run `echo $SHELL` to help you determine your shell.

To enable shell autocompletion for ty commands, run one of the following:

=== "Bash"

    ```bash
    echo 'eval "$(ty generate-shell-completion bash)"' >> ~/.bashrc
    ```

=== "Zsh"

    ```bash
    echo 'eval "$(ty generate-shell-completion zsh)"' >> ~/.zshrc
    ```

=== "fish"

    ```bash
    echo 'ty generate-shell-completion fish | source' > ~/.config/fish/completions/ty.fish
    ```

=== "Elvish"

    ```bash
    echo 'eval (ty generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv
    ```

=== "PowerShell / pwsh"

    ```powershell
    if (!(Test-Path -Path $PROFILE)) {
      New-Item -ItemType File -Path $PROFILE -Force
    }
    Add-Content -Path $PROFILE -Value '(& ty generate-shell-completion powershell) | Out-String | Invoke-Expression'
    ```

Then restart the shell or source the shell config file.
