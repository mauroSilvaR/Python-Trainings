from gui import GuiApp

def main():
    app = GuiApp(
        window_name="My XML-Based GUI",
        bg_color="#E6F7FF",
        label_text="Loaded from XML!",
        label_position=(1, 2)
    )
    app.launch()
    app.greet()
    

if __name__ == "__main__":
    main()
