""" Clean some temporary folders

Cleans:
    - `__pycache__` folders
    - `susapad.build` folder
    - `susapad.dist` folder
    - experimental files, that starts with `exp`. 
        i.e.: `exp_new_window.py`

To use this module simply run `poetry run clean`.

But, you can also `python susapad/scripts/clean` for Linux
and `py .\\susapad\\scripts\\clear.py` for Windows as well.
"""

import pathlib as path


class ExperimentsDump:

    def __init__(self, root_dir: str):
        self.root = path.Path(root_dir)
        self.files = self.__get_exp_files()

    def __get_exp_files(self) -> list[path.Path]:
        return self.root.rglob("exp_*.py")

    def clear(self):
        for file in self.files:
            file.unlink()


class BuildDump:

    def __init__(self, project: str, root_dir: str):
        self.name = project
        self.root = path.Path(root_dir)

    def __delete(self, directory: path.Path):
        for element in directory.iterdir():
            if element.is_dir():
                self.__delete(element)
            else:
                element.unlink()

        for folder in directory.iterdir():
            folder.rmdir()
        directory.rmdir()

    def clear(self):
        if (self.root / f"{self.name}.build").exists():
            self.__delete(self.root / f"{self.name}.build")
        if (self.root / f"{self.name}.dist").exists():
            self.__delete(self.root / f"{self.name}.dist")


class PyCacheDump:
    """"Stores and cleans the project's __pycache__ folders"""

    def __init__(self, root_dir: str):
        self.directories: list[path.Path] = \
            self.__search_for_pycache(path.Path(root_dir))

    def __search_for_pycache(self, root_dir: path.Path) -> list[path.Path]:
        return sorted(
            root_dir.rglob("**/__pycache__/")
        )

    def __delete_pyc_files(self, directory: path.Path):
        for file in directory.iterdir():
            file.unlink()

    def clear(self):
        """cleans `self.directories`'s folders and files"""
        if not self.directories:
            return

        for directory in self.directories:
            self.__delete_pyc_files(directory)
            directory.rmdir()

# == Callable ==

def run():
    """"Starts the script 
    - use your Current Working Directory as root path
    """
    print("Cleaning __pycache__ ...")
    PyCacheDump(".").clear()

    print("Cleaning build ...")
    BuildDump("susapad", ".").clear()

    print("Cleaning experimental files")
    ExperimentsDump(".").clear()


if __name__ == "__main__":
    run()
