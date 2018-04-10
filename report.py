from printer import Printer

class Report():
    def print_head(self, head):
        print("-- head -----------------------")
        print(head)
        print("-- head -----------------------")

    def print_body(self, body):
        print("== body =========")
        Printer.print_body(body)
        print("== body =========")

