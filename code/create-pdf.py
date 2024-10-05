from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from settings import *

class PdfCreator:
    def __init__(self, company_name, address, phone, description, work_interval, total):
        self.company_name = company_name
        self.address = address
        self.ph_num = phone
        self.service = description
        self.work_time = work_interval
        self.money = total

        pdfmetrics.registerFont(TTFont('Captions', INVOICE_CAP_FONT))
        pdfmetrics.registerFont(TTFont('Bold', BOLD_FONT))
        pdfmetrics.registerFont(TTFont('Normal', NORMAL_FONT))


    def create(c):
        c.drawString(100, 100, "Hello World")

    def fill(c):
        pass

c = canvas.Canvas("hello.pdf")
PdfCreator.create(c)
c.showPage()
c.save()