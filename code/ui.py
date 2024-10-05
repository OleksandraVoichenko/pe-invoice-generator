# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello world!</p>"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
from create import PdfCreator
from reportlab.pdfgen import canvas

personal_info = {'company name': '[company name]',
                 'street address': '[street address]',
                 'city, zip': '[city, zip]',
                 'website': '[website]'}

client_info = {'client company': '[client company]',
                'street address': '[street address]',
                'city, zip': '[city, zip]'}

project_info = {'work_interval': '[work_interval]',
                'description': '[description]',
                'payment': '[payment]'}

c = canvas.Canvas("invoice.pdf")
pdf_creator = PdfCreator(personal_info, client_info, project_info)
pdf_creator.create_base(c)
c.showPage()
c.save()


