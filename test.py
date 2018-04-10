class Document():
    def __init__(self, printer):
        self.printer = printer()

    def print_doc(self):
        self.printer.print_head()
        self.printer.print_body()

class Html():
    def print_head(self):
        print("<head></head>")

    def print_body(self):
        print("<body></body>")


class MarkDown():
    def print_head(self):
        print("# head")

    def print_body(self):
        print("# body")

def main():
    md = Document(MarkDown)
    md.print_doc()

    html = Document(Html)
    html.print_doc()

if __name__ == '__main__':
    main()
