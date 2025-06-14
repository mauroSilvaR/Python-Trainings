from logic import greet as logic_greet
from gui import greet as gui_greet
from gui import launch_gui

def main():
    print("Hello earth!\n")
    logic_greet()
    gui_greet()
    launch_gui("#A0D8EF")

if __name__=="__main__":
    main()
