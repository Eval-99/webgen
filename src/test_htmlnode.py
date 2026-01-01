import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    pass

    def test_html_props_eq(self):
        html_node = HTMLNode(None, None, None, {"key1": "val1", "key2": "val2"})
        html_str = 'HTMLNode(None, None, None, {key1="val1" key2="val2"})'
        self.assertEqual(str(html_node), str(html_str))

    def test_html_props_not_eq(self):
        html_node = HTMLNode(None, None, None, {"key1": "val1", "key2": "val2"})
        html_str = 'HTMLNode(None, None, None, {key1="val1")'
        self.assertNotEqual(str(html_node), str(html_str))

    def test_html_props_none_eq(self):
        html_node = HTMLNode(None, None, None)
        html_str = "HTMLNode(None, None, None)"
        self.assertEqual(str(html_node), str(html_str))

    def test_html_props_none_not_eq(self):
        html_node = HTMLNode(None, None, None)
        html_str = 'HTMLNode(None, None, None, {key1="val1")'
        self.assertNotEqual(str(html_node), str(html_str))

    def test_html_props_empty(self):
        html_node = HTMLNode()
        html_str = "HTMLNode(None, None, None"
        self.assertNotEqual(str(html_node), str(html_str))

    def test_html_props_only(self):
        html_node = HTMLNode(None, None, None, {"key1": "val1", "key2": "val2"})
        html_props = html_node.props_to_html()
        html_str = 'key1="val1" key2="val2"'
        self.assertEqual(str(html_props), str(html_str))


#         self.assertEqual(node, node2)
#         self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
