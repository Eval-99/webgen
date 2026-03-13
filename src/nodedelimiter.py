from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue

        text_normal = ""
        text_delimiter = ""
        found_delimiter = False

        for word in node.text.split():
            if word.startswith(delimiter):
                node_lst.append(TextNode(text_normal[:-1], TextType.TEXT))
                text_normal = ""
                found_delimiter = True
            if found_delimiter is True:
                text_delimiter += word + " "
                if word.endswith(delimiter):
                    node_lst.append(TextNode(text_delimiter[:-1], text_type))
                    text_delimiter = ""
                    found_delimiter = False
            else:
                text_normal += word + " "
        node_lst.append(TextNode(text_normal[:-1], TextType.TEXT))

    return node_lst


node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)
