import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     node_lst = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             node_lst.append(node)
#             continue
#
#         text_normal = ""
#         text_delimiter = ""
#         delimiter_open = False
#
#         node_words = node.text.split()
#         if node_lst != []:
#             node_words[0] = " " + node_words[0]
#
#         for word in node_words:
#             index = word
#             if word.startswith(delimiter) and delimiter_open is True:
#                 raise Exception("Invalid Markdown syntax. Delimiter not closed.")
#             if word.startswith(delimiter):
#                 if text_normal != "":
#                     node_lst.append(TextNode(text_normal, TextType.TEXT))
#                 text_normal = ""
#                 delimiter_open = True
#             if word.endswith(delimiter) and delimiter_open is False:
#                 raise Exception("Invalid Markdown syntax. Delimiter not closed.")
#             if delimiter_open is True:
#                 text_delimiter += word + " "
#                 if word.endswith(delimiter):
#                     node_lst.append(
#                         TextNode(
#                             str(text_delimiter[:-1]).replace(delimiter, ""), text_type
#                         )
#                     )
#                     text_delimiter = ""
#                     delimiter_open = False
#                     try:
#                         node_words[node_words.index(index) + 1] = (
#                             " " + node_words[node_words.index(index) + 1]
#                         )
#                     except IndexError:
#                         continue
#             else:
#                 text_normal += word + " "
#         if text_normal != "":
#             node_lst.append(TextNode(text_normal[:-1], TextType.TEXT))
#         if delimiter_open is True:
#             raise Exception("Invalid Markdown syntax. Delimiter not closed.")
#
#     return node_lst


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_title(text):
    lines = text.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("No title heading in markdown file")


def split_nodes_link(old_nodes):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue
        matches = extract_markdown_links(node.text)
        for match in matches:
            sections = node.text.split(f"[{match[0]}]({match[1]})", 1)
            if sections[0] != "":
                node_lst.append(TextNode(sections[0], TextType.TEXT))
            node_lst.append(TextNode(match[0], TextType.LINK, match[1]))
            node.text = sections[1]
        if node.text != "":
            node_lst.append(TextNode(node.text, TextType.TEXT))
    return node_lst


def split_nodes_image(old_nodes):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue
        matches = extract_markdown_images(node.text)
        for match in matches:
            sections = node.text.split(f"![{match[0]}]({match[1]})", 1)
            if sections[0] != "":
                node_lst.append(TextNode(sections[0], TextType.TEXT))
            node_lst.append(TextNode(match[0], TextType.IMAGE, match[1]))
            node.text = sections[1]
        if node.text != "":
            node_lst.append(TextNode(node.text, TextType.TEXT))
    return node_lst


def text_to_nodes(text):
    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        [TextNode(text, TextType.TEXT)], "**", TextType.BOLD
                    ),
                    "_",
                    TextType.ITALIC,
                ),
                "`",
                TextType.CODE,
            )
        )
    )
