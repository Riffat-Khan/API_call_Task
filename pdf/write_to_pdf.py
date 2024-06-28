import json
from reportlab.pdfgen import canvas

def writing_to_pdf(data):
    obj = canvas.Canvas("record_currency.pdf")
    y_position = 800
    for record in data:
        for each in record:
            line = json.dumps(each)
            obj.drawString(100, y_position, line)
            y_position -= 15 
        obj.showPage()
    # obj.showPage()
    obj.save()

# def writing_to_pdf(data):
#     obj = canvas.Canvas("record_currency.pdf")
#     y_position = 800
#     for record in data:
#         for count in range(0,15, 3):
#             split_record = record[count : count+3]
#             line = json.dumps(split_record)
#             if y_position < 50: 
#                 obj.showPage()
#                 y_position = 800 
#             obj.drawString(50, y_position, line)
#             y_position -= 15 
#         y_position -= 20 
#     obj.showPage()
#     obj.save()
    