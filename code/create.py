from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
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
        description = self.project_info['description']
        c.drawString(50, y_pos, description)

        lines = description.split('\n')
        description_height = len(lines) * 16

        table_data = [
            ['DESCRIPTION/MEMO', '', 'AMOUNT'],
            [
                f"Invoice for work between {self.project_info['work_interval'][0]} to {self.project_info['work_interval'][1]}"],
            [self.project_info['description'], '', self.project_info['payment']],
            ['', 'VAT(0%)', 'USD OF VAT'],
            ['', 'TOTAL', self.project_info['payment']]
        ]

        col_widths = [300, 100, 100]

        table = Table(table_data, colWidths=col_widths)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('SPAN', (0, 0), (1, 0)),
            ('SPAN', (0, 1), (2, 1)),
            ('SPAN', (0, 2), (1, 2)),
            ('ALIGN', (2, 3), (2, 4), 'RIGHT'),
            ('ALIGN', (0, 3), (1, 3), 'RIGHT'),
            ('ALIGN', (0, 4), (1, 4), 'RIGHT'),
            ('ALIGN', (2, 2), (2, 2), 'RIGHT')
        ])

        table.setStyle(style)

        # Adjust the table's Y-position based on the description height
        y_pos -= description_height + 50

        # Wrap the table in a list and draw it on the canvas at the calculated position
        table.wrapOn(c, self.width, self.height)
        table.drawOn(c, 50, y_pos)
