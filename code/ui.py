from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from create import PdfCreator

app = Flask(__name__)

personal_info = {'company name': '[company name]',
                 'street address': '[street address]',
                 'city, zip': '[city, zip]',
                 'website': '[website]'}

client_info = {'client company': '[client company]',
                'street address': '[street address]',
                'city, zip': '[city, zip]'}

project_info = {'work_interval': '[work_interval]',
                'scope': '[scope]',
                'description': '[description/memo]',
                'payment': '[payment]'}



class UI:
    @staticmethod
    def create_pdf(self):
        c = canvas.Canvas("invoice.pdf")
        pdf_creator = PdfCreator(personal_info, client_info, project_info)
        pdf_creator.create_base(c)
        pdf_creator.fill(c)
        c.showPage()
        c.save()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':



if __name__ == "__main__":
    app.run(debug=True)



