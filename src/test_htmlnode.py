import unittest

from src.htmlnode import LeafNode
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="Hello")
        actual_html_props = node.props_to_html()
        expected_html_props = ""
        self.assertEqual(actual_html_props, expected_html_props)

    def test_props_empty(self):
        node = HTMLNode(tag="p", value="Hello", props={})
        actual_html_props = node.props_to_html()
        expected_html_props = ""
        self.assertEqual(actual_html_props, expected_html_props)


    def test_props_has_value(self):
        node = HTMLNode(tag="p", value="Hello", props= {"href": "https://www.google.com", "target": "_blank"})
        actual_html_props = node.props_to_html()
        expected_html_props = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(actual_html_props, expected_html_props)

    def test_to_html(self):
        node = HTMLNode(tag="p", value="Hello")
        with self.assertRaises(NotImplementedError):  # This checks if NotImplementedError is raised
            node.to_html()


    def test_tag_is_none(self):
        node = LeafNode(tag=None, value="Hello")
        actual_to_leaf_html = node.to_html()
        expected_to_leaf_html = "Hello"
        self.assertEqual(actual_to_leaf_html, expected_to_leaf_html)

    def test_value_is_none(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
