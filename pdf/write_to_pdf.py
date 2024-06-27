from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 

def writing_to_pdf(content):
    fileName = 'currencies_record.pdf'
    documentTitle = 'currencies'
    title = 'CURRENCIES RECORD'
    textLines = content

    pdf = canvas.Canvas(fileName) 
    pdf.setTitle(documentTitle) 

    pdfmetrics.registerFont( 
        TTFont('abc', 'SakBunderan.ttf') 
    ) 
    pdf.setFont('abc', 36) 
    pdf.drawCentredString(300, 770, title)


    pdf.line(30, 710, 550, 710) 
    text = pdf.beginText(40, 680) 
    text.setFont("Courier", 18) 
    text.setFillColor(colors.red) 
    for line in textLines: 
        text.textLine(line)
        
    
