from logic import greet as logic_greet
from gui import greet as gui_greet

def main():
    print("Hello earth!\n")
    logic_greet()
    gui_greet()

if __name__=="__main__":
    main()
