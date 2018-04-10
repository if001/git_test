class Document():
    def init(self, printer):
        self.printer = printer()
        
    def print_doc(self):
        self.printer.print_head()
        self.printer.print_body()

class Html():
    def print_head():
        print("<head></head>")
    def print_body():
        print("<body></body>")


class MarkDown():
    def print_head():
        print("# head")
    def print_body():
        print("# body")

def main():
    html = Document(Html)
    html.print_doc()


if __name__ == '__main__':
    main()
