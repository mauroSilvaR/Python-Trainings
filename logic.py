import xml.etree.ElementTree as ET

class GuiConfigParser:
    def __init__(self, file_path="config.xml"):
        self.file_path = file_path #file path is the name with which init is called
        self.tree = None #tree starts empty
        self.root = None #root starts empty
        self.color_map = {}  #color dict starts empty
        self.config = {} #config starts empty

    def load(self):
        self.tree = ET.parse(self.file_path) #load XML
        self.root = self.tree.getroot() #get the root
        self._parse_colors() #create the color dictionary from the XML
        self._parse_gui()

    def _parse_colors(self):
        #first get the entire color element
        colors = self.root.find("colors")
        #store each attribute in our dictionary
        for color in colors:
            name = color.attrib.get("name")
            value = color.attrib.get("value")
            # Only add the colors if they are present. Just a safeguard XML SHOULD be right always
            if name and value:
                self.color_map[name] = value

    def _parse_gui(self):
        gui = self.root.find("gui")

        title = gui.find("title").text
        bgcolor_key = gui.find("bgcolor").text

        if bgcolor_key.startswith("#"):
            bgcolor = bgcolor_key
        elif bgcolor_key in self.color_map:
            bgcolor = self.color_map[bgcolor_key]
        #if the color is neither a hex value or one of the predefined colors, throw an error
        else:
            raise ValueError(f"Color '{bgcolor_key}' not defined in <colors>")

        #return label as an element
        label_node = gui.find("label")
        #get text attrib for the label, if none is declared use "Default Label"
        label_text = label_node.attrib.get("text", "Default Label")
        #get row attrib for the label, if none is declared use 0 as default
        row = int(label_node.attrib.get("row", 0))
        #get col attrib for the label, if none is declared use 0 as default
        col = int(label_node.attrib.get("column", 0))

        #finish the parsing by passing all the characteristics to our label config
        self.config = {
            "title": title,
            "bgcolor": bgcolor,
            "label_text": label_text,
            "label_position": (row, col)
        }

    def get_config(self):
        return self.config

    def get_color_map_type(self):
        print(type(self.color_map))

    def get_current_color_map(self):
        for color in self.color_map:
            print(self.color_map[color])
