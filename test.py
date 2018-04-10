from html import Html
from markdown import MarkDown
from report import Report

class Document():
    def __init__(self, printer, head):
        self.head = head
        self.printer = printer()

    def print_doc(self, body):
        self.printer.print_head(self.head)
        self.printer.print_body(body)

def main():
    md = Document(MarkDown, "md")
    md.print_doc("よい天気ですね!")
    print()
    print()
    html = Document(Html, "html")
    html.print_doc("よい天気ですね!")
    print()
    print()
    rep = Document(Report, "report")
    rep.print_doc("よい天気ですね!")

if __name__ == '__main__':
    main()
