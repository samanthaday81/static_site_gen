from textnode import TextType, TextNode

def main():
    new_text_node_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_text_node_obj)

main()

