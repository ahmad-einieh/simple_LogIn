# Simple Login

A Python/Tkinter login-screen demo with a background image, user/password icons, masked password entry, and validation message boxes.

> **Demo only:** Login checks hardcoded credentials in the source. There is no account database, password hashing, session management, or real authentication. Do not use it to protect an application or enter real passwords.

## Requirements

- Python 3 with Tkinter and a graphical desktop session.
- Pillow for loading the background image.

On Ubuntu/Debian, install `python3-tk` if Tkinter is missing.

## Run

```bash
python -m venv .venv
```

Activate the environment (`source .venv/bin/activate` on Linux/macOS, or `.venv\Scripts\activate` in Windows Command Prompt), then:

```bash
python -m pip install Pillow
python login.py
```

Run from the repository directory so `bg1.png`, `icons8-user-male-24.png`, `icons8-user-locked-32.png`, and `login-icon-3057.gif` can be loaded.

## Try the demo

Use `ahmad` for both username and password. Empty fields and incorrect credentials display error messages; a matching pair displays a welcome message. A successful login does not open another screen.

The interface and validation logic are in [`login.py`](login.py).
