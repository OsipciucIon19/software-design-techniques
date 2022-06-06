import pdfkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


class ReportFormat:
    PDF = 0
    TEXT = 1


class Report:
    def __init__(self, format_):
        self.title = 'Monthly report'
        self.text = ['Things are going', 'really, really well.']
        self.format_ = format_


class Handler:
    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        self.nextHandler.handle(request)


class PDFHandler(Handler):
    def handle(self, request):
        if request.format_ == ReportFormat.PDF:
            self.output_report(request.title, request.text)
        else:
            super(PDFHandler, self).handle(request)

    def output_report(self, title, text):
        string = '<html>'
        string += ' <head>'
        string += ' <title>%s</title>' % title
        string += ' </head>'
        string += ' <body>'
        for line in text:
            string += ' <p>%s' % line
        string += ' </body>'
        string += '</html>'
        print(string)
        pdfkit.from_string(string, 'GfG.pdf', configuration=config)


class TextHandler(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.TEXT:
            self.output_report(request.title, request.text)
        else:
            super(TextHandler, self).handle(request)

    def output_report(self, title, text):
        print(5 * '*' + title + 5 * '*')
        for line in text:
            print(line)


class ErrorHandler(Handler):
    def handle(self, request):
        print("Invalid request")


if __name__ == '__main__':
    report = Report(ReportFormat.PDF)
    pdf_handler = PDFHandler()
    text_handler = TextHandler()
    pdf_handler.handle(report)
    text_handler.handle(report)
    pdf_handler.nextHandler = text_handler
    text_handler.nextHandler = pdf_handler
    text_handler.handle(report)
