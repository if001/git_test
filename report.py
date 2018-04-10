from printer import Printer
class Report():
    def print_head(self, head):
        print("-- head -----------------------")
        Printer.printer(head)
        print("-- head -----------------------")

    def print_body(self, body):
        print("== body =========")
        Printer.printer(body)
        print("== body =========")

