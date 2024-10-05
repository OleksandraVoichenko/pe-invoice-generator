from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from datetime import date
from settings import *

class PdfCreator:
    def __init__(self, personal_info, client_info, project_info):
        self.personal_info = personal_info
        self.client_info = client_info
        self.project_info = project_info

        self.width, self.height = A4

        pdfmetrics.registerFont(TTFont('Captions', INVOICE_CAP_FONT))
        pdfmetrics.registerFont(TTFont('Bold', BOLD_FONT))
        pdfmetrics.registerFont(TTFont('Normal', NORMAL_FONT))


    def create_base(self, c):
        # invoice cap
        c.setFont('Captions', 40)
        c.drawString(self.width - 220, self.height - 100, 'INVOICE')
        c.setFont('Bold', 16)
        c.drawString(self.width - 220, self.height - 125, str('# INV-' + date.today().isoformat()))
        c.drawString(self.width - 220, self.height - 150, str('Issue date: ' + date.today().isoformat()))

        # personal
        c.setFont('Normal', 16)
        y_pos = self.height - 100
        for label, value in self.personal_info.items():
            c.drawString(50, y_pos, value)
            y_pos -= 22

        # client
        c.setFont('Normal', 16)
        c.drawString(50, self.height - 220, 'Bill to:')
        y_pos = self.height - 240
        for label, value in self.personal_info.items():
            c.drawString(50, y_pos, value)
            y_pos -= 22


    def fill(self, c):
        y_pos = 500
        # project
        c.setFont('Normal', 16)
        c.drawString(50, y_pos, 'Service description:')
        y_pos -=20
        c.drawString(50, y_pos, self.project_info['description'])

