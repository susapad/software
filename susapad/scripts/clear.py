
import pathlib as path

class PyCache:

    def __init__(self, root_dir: str):
        self.directories: list[path.Path] = \
            self.__search_for_pycache(path.Path(root_dir))

    def __search_for_pycache(self, root_dir: path.Path) -> list[path.Path]:
        return sorted(
            root_dir.rglob("**/__pycache__/")
        )

    def _delete_pyc_files(self, directory: path.Path):
        for file in directory.iterdir():
            file.unlink()

    def clear_pycache(self):
        for directory in self.directories:
            self._delete_pyc_files(directory)
            directory.rmdir()


# == Callable == 

def run():
    print("Clearing __pycache__...")
    PyCache(".").clear_pycache()


if __name__ == "__main__":
    run()
