
from susapad.windows import alert


def susapad_not_found(window):
    #window.setEnabled(False)
    dialog = alert.AlertDialog(window)
    dialog.show()


def close_current_window(window):
    window.close()
