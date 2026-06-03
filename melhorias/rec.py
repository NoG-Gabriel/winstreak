import os
import sys

def recurso(caminho):
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(__file__)
    
    return os.path.join(base, caminho)