from html import Html
from markdown import MarkDown
from report import Report
from report2 import Report2
from report3 import Report3

class Document():
    def __init__(self, printer):
        self.printer = printer()
        self.head = []
        self.body = []

    def print_doc(self):
        self.printer.print_head(self.head)
        self.printer.print_body(self.body)

    def add_head(self, st):
        self.head.append(st)

    def add_body(self, st):
        self.body.append(st)

def main():
    md = Document(MarkDown)
    md.add_head("markdown")
    md.add_body("よい天気ですね!")
    md.print_doc()
    print()
    print()
    html = Document(Html)
    html.add_head("title")
    html.add_body("よい天気ですね!")
    html.print_doc()
    print()
    print()
    rep = Document(Report)
    rep.add_head("たいとる")
    rep.add_body("これはレポートです")
    rep.add_body("今日も良い天気でした。")
    rep.print_doc()
    print()
    print()
    rep2 = Document(Report2)
    rep2.add_head("たいとる")
    rep2.add_body("これはレポートです")
    rep2.add_body("今日も良い天気でした。")
    rep2.print_doc()

if __name__ == '__main__':
    main()
