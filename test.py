class Document():
    def __init__(self, printer, head):
        self.head = head
        self.printer = printer()

    def print_doc(self, body):
        self.printer.print_head(self.head)
        self.printer.print_body(body)

class Html():
    def print_head(self, head):
        print("<head>")
        print(head)
        print("</head>")

    def print_body(self, body):
        print("<body>")
        print(body)
        print("</body>")

class MarkDown():
    def print_head(self, head):
        print("<head>")
        print(head)
        print("</head>")

    def print_body(self, body):
        print("<body>")
        print(body)
        print("</body>")

class Report():
    def print_head(self, head):
        print("-- head ---------")
        print(head)
        print("-- head ---------")

    def print_body(self, body):
        print("== body =========")
        print(body)
        print("== body =========")



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
