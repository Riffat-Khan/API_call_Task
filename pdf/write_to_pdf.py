from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(data, filename):
    obj = canvas.Canvas(filename, pagesize=letter)

    for record in data:
        obj.drawString(50, 750, f"'Date': {record[0]['date']}")

        obj.drawString(50, 730, "'usd':")
        y_position = 710
        for currency, value in record[1]['usd'].items():
            if y_position < 50:
                obj.showPage()
                y_position = 800
            obj.drawString(70, y_position, f"'{currency}': {value}")
            y_position -= 20

        if len(record) == 3:
            obj.drawString(50, y_position - 20, "Diff:")
            y_position -= 40
            for currency, diff in record[2]['diff'].items():
                if y_position < 50:
                    obj.showPage()
                    y_position = 800
                obj.drawString(70, y_position, f"'{currency}': {diff}")
                y_position -= 20
        obj.showPage()
    obj.save()
