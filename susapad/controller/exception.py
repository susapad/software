
from susapad.window import alert


def susapad_not_found(window):
    dialog = alert.AlertDialog(window)
    dialog.show()


def close_current_window(window):
    window.close()
