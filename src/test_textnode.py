import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node", TextType.Bold_text)
        self.assertEqual(node, node2)

    def test_init(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        self.assertEqual(node,TextNode("This is a text node", TextType.Bold_text))

    def test_ineq(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node", TextType.Code_text)
        self.assertNotEqual(node,node2)
if __name__ == "__main__":
    unittest.main()