from html import Html
from markdown import MarkDown
from report import Report

class Document():
    def __init__(self, printer, head):
        self.head = head
        self.printer = printer()
        self.body = []

    def print_doc(self):
        self.printer.print_head(self.head)
        self.printer.print_body(self.body)

    def add_body(self, st):
        self.body.append(st)


class Printer():
    @classmethod
    def print_body(cls, body):
        for value in body:
            print(value)

def main():
    md = Document(MarkDown, "md")
    md.add_body("よい天気ですね!")
    md.print_doc()
    print()
    print()
    html = Document(Html, "html")
    html.add_body("よい天気ですね!")
    html.print_doc()

    print()
    print()
    rep = Document(Report, "report")
    rep.add_body("これはレポートです")
    rep.add_body("今日も良い天気でした。")
    rep.print_doc()

if __name__ == '__main__':
    main()
