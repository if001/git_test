from printer import Printer
class Report2():
    def print_head(self, head):
        print("^^^^^^^^^^^^^^^^^^^^^^^")
        Printer.printer(head)

    def print_body(self, body):
        print("^^^^^^^^^^^^^^^^^^^^^^^")
        Printer.printer(body)
