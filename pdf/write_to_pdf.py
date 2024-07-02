from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(data, filename):
    obj = canvas.Canvas(filename, pagesize=letter)

    for record in data:
        obj.drawString(100, 350, f"Currency Record - {record['date']}")

        obj.drawString(50, 320, "'USD[Rate]':")
        y_position = 300
        for currency, value in record['usd'].items():
            if y_position < 20:
                obj.showPage()
                y_position = 300
            obj.drawString(70, y_position, f"'{currency}': {value}")
            y_position -= 20

        if 'diff' in record:
            obj.drawString(350, 320, "Rate Diff:")
            y_position = 300
            for currency, diff in record['diff'].items():
                if y_position < 20:
                    obj.showPage()
                    y_position = 300
                obj.drawString(370, y_position, f"'{currency}': {diff}")
                y_position -= 20
        obj.showPage()
    obj.save()
