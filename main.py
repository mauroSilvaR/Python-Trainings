from logic import GuiConfigParser
from gui import GuiApp

def main():
    parser = GuiConfigParser("config.xml")
    parser.load()
    config = parser.get_config()

    app = GuiApp(
        window_name=config["title"],
        bg_color=config["bgcolor"],
        label_text=config["label_text"],
        label_position=config["label_position"]
    )
    app.launch()

if __name__ == "__main__":
    main()
