## Release

- I placed *Nuitka* as optional for *Poetry* because
  it was breaking when tried `poetry install`. (CI and local)
- I installed *Nuitka* via `pip` instead of `pipx` because
  it was breaking in CI...
- So the best approach was install via pip in CI
  (but, please, use pipx in your local enviroment)
