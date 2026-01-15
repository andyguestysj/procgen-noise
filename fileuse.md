# pyproject.toml - Tooling File

**What it is**

The central configuration file for modern Python projects.

It can define:

- Project metadata (name, version)
- Dependencies
- Build system
- Tool configuration (formatters, linters, test runners)

It replaces:

- setup.py
- setup.cfg
- parts of requirements.txt

**Why it exists**

Python tooling used to be fragmented.
pyproject.toml standardises how projects are built and configured.

Any project you want students to run via `pip install -e`.

# requirements.txt

**What it is**

A plain text list of dependencies.

**Why it exists**

Easy to read

Easy to install

No extra concepts

**How it’s used**
`python -m  pip install -r .\requirements.txt`

# gitignore

**What it is**

Tells Git which files and folders NOT to track.

**Common Python .gitignore**

```txt
__pycache__/
*.pyc
.venv/
.env
```

**Why it exists**

Python generates files automatically

Virtual environments should never be committed

Keeps repositories clean and portable

# __init__.py

**What it is**

Marks a folder as a Python package.

Even if empty:

```txt
# entities/__init__.py
```

**Why it exists**

Enables imports like:

```txt
from entities.player import Player
```

Makes folder structure meaningful to Python