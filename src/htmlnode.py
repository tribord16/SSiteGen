class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        for keys,values in self.props.items():
            string += f" {keys}=\"{values}\""
        return string
    
    
    def __repr__(self):
        return f"HTML TAG:{self.tag}, VALUE:{self.value}, CHILDREN:{self.children}, PROPS:{self.props}"
    
        