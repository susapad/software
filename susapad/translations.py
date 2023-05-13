
EN = {
    "status": {
        "not-found": "SusaPad not found",
        "insider-connected": "SusaPad Insider found at {port}",
        "connected": "SusaPad found at {port}",
    },
    "error": {
        "not-found": "Something went wrong. Make sure that your SusaPad is connected."
    },
    "buttons": {
        "connect": "Connect",
        "try-again": "Try again",
        "settings": "Settings",
        "close": "Close",
        "help": "Help",
        "turn-on": "Turn On",
        "turn-off": "Turn Off",
    },

    "default-config": {
        "input": "Input",
        "rapid-trigger": "Rapid Trigger",
        "continuous-rapid-trigger": "Continuous Rapid Trigger",
        "actuation-point": "Actuation Point: (${value})",
        "sensibility": "Sensibility: Press (${value1}) and Release (${value2})"
    },

    "insider-config": {
        "save": "Save",
        "hysteresis": "Actuation Point: (${value})\n(with rapid trigger disabled)",
        "sensibility": "Sensibility: ${value}"
    }
}


PT = {
    "status": {
        "not-found": "SusaPad não encontrado",
        "insider-connected": "SusaPad Insider encontrado na porta {port}",
        "connected": "SusaPad encontrado na porta {port}",
    },
    "error": {
        "not-found": "Algo deu errado. Certifique-se se seu SusaPad está conectado."
    },
    "buttons": {
        "connect": "Conectar",
        "try-again": "Tentar novamente",
        "settings": "Configurar",
        "close": "Fechar",
        "help": "Ajuda",
        "turn-on": "Ligar",
        "turn-off": "Desligar",
    },

    "default-config": {
        "input": "Input",
        "rapid-trigger": "Rapid Trigger",
        "continuous-rapid-trigger": "Rapid Trigger Contínuo",
        "actuation-point": "Ponto de Atuação: (${value})",
        "sensibility": "Sensibilidade: Pressionar (${value1}) e Soltar (${value2})"
    },

    "insider-config": {
        "save": "Salvar",
        "hysteresis": "Ponto de Atuação: (${value})\n(com rapid trigger desligado)",
        "sensibility": "Sensibilidade: ${value}"
    }
}


ES = {
    "status": {
        "not-found": "SusaPad no encontrado",
        "insider-connected": "SusaPad Insider encontrado en la porta {port}",
        "connected": "SusaPad encontrado en la porta {port}",
    },
    "error": {
        "not-found": "Algo ha ido mal. Asegúrese que su SusaPad está conectado."
    },
    "buttons": {
        "connect": "Conectar",
        "try-again": "Inténtalo de nuevo",
        "settings": "Configurar",
        "close": "Cerrar",
        "help": "Ayuda",
        "turn-on": "Activar",
        "turn-off": "Desactivar",
    },

    "default-config": {
        "input": "Input",
        "rapid-trigger": "Rapid Trigger",
        "continuous-rapid-trigger": "Rapid Trigger Continuo",
        "actuation-point": "Punto de Activación: (${value})",
        "sensibility": "Sensibilidad: Presionar (${value1}) y Soltar (${value2})"
    },

    "insider-config": {
        "save": "Save",
        "hysteresis": "Punto de Activación: (${value})\n(con rapid trigger desactivado)",
        "sensibility": "Punto: ${value}"
    }
}


def get_language():

    try:
        with open("susapad/LANG") as f:
            lang = f.readline().strip()
    except:
        return EN

    if lang == "PT":
        return PT
    elif lang == "ES":
        return ES
    else:
        return EN



__all__ = ["get_language"]
