from reportlab.pdfgen import canvas

class PdfCreator:
    def __init__(self, company_name, address, phone, description, work_interval, total):
        self.company_name = company_name
        self.address = address
        self.ph_num = phone
        self.service = description
        self.work_time = work_interval
        self.money = total

    def create(c):
        c.drawString(100, 100, "Hello World")

    def fill(c):
        pass

c = canvas.Canvas("hello.pdf")
PdfCreator.create(c)
c.showPage()
c.save()