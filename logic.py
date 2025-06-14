import xml.etree.ElementTree as ET

class GuiConfigParser:
    def __init__(self, file_path="config.xml"):
        self.file_path = file_path
        self.tree = None
        self.root = None
        self.color_map = {}  # will now come from XML
        self.config = {}

    def load(self):
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()
        self._parse_colors()
        self._parse_gui()

    def _parse_colors(self):
        for color in self.root.find("colors"):
            name = color.attrib.get("name")
            value = color.text.strip()
            if name:
                self.color_map[name] = value

    def _parse_gui(self):
        gui = self.root.find("gui")

        title = gui.find("title").text
        bgcolor_key = gui.find("bgcolor").text.strip()

        if bgcolor_key.startswith("#"):
            bgcolor = bgcolor_key  # raw hex
        else:
            bgcolor = self.color_map.get(bgcolor_key)
            if not bgcolor:
                raise ValueError(f"Color '{bgcolor_key}' not defined in <colors>")

        label_node = gui.find("label")
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
