from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse=Controller()
    mouse.position=(500,200)
controlMouse()

def controlKeyboard():
    keyword=Controller()
    keyword.type("Hello HF Electronotics")
controlKeyboard()

#Hello HF ElectronoticsHello HF Electronotics