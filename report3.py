from printer import Printer
class Report3():
    def print_head(self, head):
        print("**********************")
        Printer.printer(head)

    def print_body(self, body):
        print("**********************")
        Printer.printer(body)
