

import enum

class ConnectionStatus(enum.Enum):
    Disconnected = 0
    Connected    = 1
    Connecting   = 2
    NotFound     = 3
