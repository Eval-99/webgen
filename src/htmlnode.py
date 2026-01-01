class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = " ".join([f'{k}="{v}"' for k, v in self.props.items()])
        return f"{props_str}"

    def __repr__(self):
        return (
            f"HTMLNode({self.tag}, "
            f"{self.value}, "
            f"{self.children}"
            f"{', {' + self.props_to_html() + '}' if self.props_to_html() else self.props_to_html()})"
        )
