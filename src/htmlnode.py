


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not implemented yet.")

    def props_to_html(self):
        result = ""
        if self.props is None:
            return ""
        else:
            for key, value in self.props.items():
                formatted_attribute = f" {key}=\"{value}\""
                result += formatted_attribute
            return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value},{self.children},{self.props})"



class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
