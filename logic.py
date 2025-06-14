import xml.etree.ElementTree as ET

class GuiConfigParser:
    def __init__(self, file_path="config.xml"):
        self.file_path = file_path
        self.color_map = {
            "primary": "#E6F7FF",
            "alert": "#FF4C4C",
            "success": "#4CAF50",
            "neutral": "#F0F0F0",
            "background": "#FFFFFF",
            "text": "#333333"
        }
        self.tree = None
        self.root = None
        self.config = {}

    def load(self):
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()
        self._parse_gui()

    def _parse_gui(self):
        title = self.root.find("title").text
        bgcolor_key = self.root.find("bgcolor").text
        bgcolor = self.color_map.get(bgcolor_key, bgcolor_key)

        label_node = self.root.find("label")
        label_text = label_node.attrib.get("text", "Default Label")
        row = int(label_node.attrib.get("row", 0))
        col = int(label_node.attrib.get("column", 0))

        self.config = {
            "title": title,
            "bgcolor": bgcolor,
            "label_text": label_text,
            "label_position": (row, col)
        }

    def get_config(self):
        return self.config

    def greet(self):
        print("Hello Venus!\n")
