import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode()
        self.assertEqual(node.__repr__(),HTMLNode().__repr__())

    def test_print(self):
        node = HTMLNode(tag="a",props={
    "href": "https://github.com/tribord16.com", 
    "target": "_blank",
    })            
        self.assertEqual(node.__repr__(),f"HTML TAG:a, VALUE:None, CHILDREN:None, PROPS:{node.props}")

    def test_props_to_html(self):
        node = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(node.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()