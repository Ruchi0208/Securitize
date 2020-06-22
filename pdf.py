import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import Main
doc = SimpleDocTemplate("form_letter.pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
def ExportPdf(numPlate, name, phone_no):
    Story = []
    vehicle = "LicPlateImages\\" + Main.getLatestScreenShot()
    logo = "securitize.png"

    formatted_time = time.ctime()
    full_name = "Chandrashekharpur Police Station"
    address_parts = ["Location:", "Familia Apts", "near Adidas showroom", "CSPUR-bbsr road", "BBSR"]

    im = Image(vehicle, 5 * inch, 3 * inch)
    logo = Image(logo, 50, 50)
    Story.append(im)
    Story.append(Spacer(1, 12))
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size=12>%s</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    for part in address_parts:
        ptext = '<font size=12>%s</font>' % part
        Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Dear %s:</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>We found a stolen car in our apartment, which is also in theft vehicle database.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    ptext1 = '<font size=12>Vehicle Details:'\
            '</font>'
    Story.append(Spacer(1, 24))
    ptext2 = '<font size=12>' \
            'Vehicle No: %s' \
            '</font>' % (numPlate)
    Story.append(Spacer(1, 12))
    ptext3 = '<font size=12>' \
            'Name: %s' \
            '</font>' % (name)
    Story.append(Spacer(1, 12))
    ptext4 = '<font size=12>' \
            'Phone No: %s' \
            '</font>' % (phone_no)


    Story.append(Paragraph(ptext1, styles["Justify"]))
    Story.append(Paragraph(ptext2, styles["Justify"]))
    Story.append(Paragraph(ptext3, styles["Justify"]))
    Story.append(Paragraph(ptext4, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Securitize</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    Story.append(logo)
    doc.build(Story)

