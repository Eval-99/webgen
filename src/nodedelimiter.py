from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue

        text_normal = ""
        text_delimiter = ""
        delimiter_open = False

        node_words = node.text.split()

        for word in node_words:
            index = word
            if word.startswith(delimiter) and delimiter_open is True:
                raise Exception("Invalid Markdown syntax. Delimiter not closed.")
            if word.startswith(delimiter):
                if text_normal != "":
                    node_lst.append(TextNode(text_normal, TextType.TEXT))
                text_normal = ""
                word = word[1:]
                delimiter_open = True
            if word.endswith(delimiter) and delimiter_open is False:
                raise Exception("Invalid Markdown syntax. Delimiter not closed.")
            if delimiter_open is True:
                text_delimiter += word + " "
                if word.endswith(delimiter):
                    node_lst.append(TextNode(text_delimiter[:-2], text_type))
                    text_delimiter = ""
                    delimiter_open = False
                    try:
                        node_words[node_words.index(index) + 1] = (
                            " " + node_words[node_words.index(index) + 1]
                        )
                    except IndexError:
                        continue
            else:
                text_normal += word + " "
        if text_normal != "":
            node_lst.append(TextNode(text_normal[:-1], TextType.TEXT))
        if delimiter_open is True:
            raise Exception("Invalid Markdown syntax. Delimiter not closed.")

    return node_lst


# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# print(new_nodes)
