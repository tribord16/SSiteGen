from textnode import *
from htmlnode import *
def main():
    print("hello world")
    node = TextNode("This is a text node", "bold", "https://github.com/tribord16")
    node2 = HTMLNode(tag="a",props={
    "href": "https://github.com/tribord16.com", 
    "target": "_blank",
    })  
    print(node2)


if __name__ == "__main__":
    main()