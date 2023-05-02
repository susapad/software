
# Build instructions

You can build this project with:

```
nuitka --standalone --plugin-enable=pyside6 --follow-imports susapad
```

Then add media

```
mkdir susapad.dist/susapad
mkdir susapad.dist/susapad/media
cp susapad/media/** susapad.dist/susapad/media/
```

## Running without build

You can just run:

```
poetry run susapad
# or
python -m susapad
```

## Running without a keypad

You can pass `True` to `SusaPad()` inside `susapad/__main__.py` module.
