"""Module to manage SusaPad's configuration and connection"""


import time

import serial


class SusaPad:

    def __init__(self):
        self.serial: [serial.Serial | None] = None
        self.sensibility: int = 200
        self.rapid_trigger: bool = True

    
    def find(self) -> str:
        """Looks for connected SusaPad device's port"""
        try:
            ports = serial.tools.list_ports.comports()
            for port, _, hwid in sorted(ports):
                if "VID:PID=0727:0727" in hwid: 
                    return port 
        except:
            return ""
        return ""


    def connect(self, port) -> bool:
        """Connect to SusaPad given a port"""
        try:
            self.serial = serial.Serial(port, 9600)
            return True
        except:
            return False


    def disconnect(self):
        """Set `self.susapad_port` as None, virtually closing the connection"""
        self.serial = None


    def set_rappid_trigger(self, on: True) -> bool:
        """Set if SusaPad is **on** or **off**"""
        n = "1" if on else "0"
        try:
            self.serial.write(f"rt {n}".encode())
            self.serial.flush()
            self.rapid_trigger = True
            time.sleep(0.5)
            return True
        except:
            return False

    def set_sensibility(self, n: int):
        """"Set the Rapid Trigger's sensibility"""

        if 7 > n or 401 < n: 
            return False

        try:
            self.serial.write(f"rts {n}".encode())
            self.serial.flush()
            self.sensibility = n
            time.sleep(0.5)
            return True
        except:
            return False
