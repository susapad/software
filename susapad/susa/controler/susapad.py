"""Module to manage SusaPad's configuration and connection"""

import time

import serial
import serial.tools.list_ports


class SusaPad:

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.serial: [serial.Serial | None] = None
        self.sensibility: int = 200
        self.rapid_trigger: bool = True

    
    def find(self) -> str:
        """Looks for connected SusaPad device's port"""
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if "VID:PID=0727:0727" in hwid:
                print("Susapad encontrado!")
                print("{}: {} [{}]".format(port, desc, hwid))
                return port 
        return ""

    def connect(self, port) -> bool:
        """Connect to SusaPad given a port"""
        try:
            self.serial = serial.Serial(port, 9600)
            return True
        except:
            if self.debug:
                return True
            else:
                self.disconect
                return False

    def disconnect(self):
        """Set `self.susapad_port` as None, virtually closing the connection"""
        self.serial = None


    # Settings functions

    def set_rapid_trigger(self, on: True) -> bool:
        """Set if SusaPad is **on** or **off**"""
        n = 1 if on else 0
        return self.__configure_susapad("rt", n)

    def set_continuous_rapid_trigger(self, on: True) -> bool:
        """Set if SusaPad is **on** or **off**"""
        n = 1 if on else 0
        return self.__configure_susapad("crt", n)

    def set_release_sensibility(self, value: int) -> bool:
        """"Set the Rapid Trigger's sensibility"""
        return self.__configure_susapad("rtus", value)

    def set_press_sensibility(self, value: int) -> bool:
        """"Set the Rapid Trigger's sensibility"""
        return self.__configure_susapad("rtds", value)

    def set_actuation_point(self, value: int) -> bool:
        """Set Key's Actuation ponit"""

        # NOTE: We need to reset `lh` to avoid undesired side-effects.
        #   Note that `uh` must always be smaller than `lh`.
        #   So bugs may occur if we don't reset this value.
        r2 = self.__configure_susapad("lh", 0)

        r1 = self.__configure_susapad("uh", value)
        r2 = self.__configure_susapad("lh", value - 10)

        return r1 and r2



    # Internal functions

    def __configure_susapad_key(self, key: int, command: str, value: int) -> bool:
        try:
            print(f"key{key}.{command} {value}")
            self.serial.write(f"key{key}.{command} {value}".encode())
            self.serial.flush()
            time.sleep(1)
            return True
        except:
            if self.debug:
                return True
            else:
                return False

    def __configure_susapad(self, command: str, value: int) -> bool:
        k1 = self.__configure_susapad_key(1, command, value)
        k2 = self.__configure_susapad_key(3, command, value)
        return k1 and k2
