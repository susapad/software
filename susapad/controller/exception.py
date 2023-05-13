
from susapad.windows import alert


def susapad_not_found(window, message: str):
    dialog = alert.AlertDialog(window, message)
    dialog.show()


def close_current_window(window):
    window.close()
