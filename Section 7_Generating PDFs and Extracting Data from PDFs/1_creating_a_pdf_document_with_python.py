from fpdf import FPDF

pdf = FPDF(orientation="p", unit="pt", format="A4")

pdf.add_page()

pdf.image(
    "Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_1/tiger.jpeg",
    w=80,
    h=50,
)

pdf.set_font(family="Times", size=24, style="B")
pdf.cell(w=0, h=50, txt="Malayan Tiger", align="C", ln=1)

pdf.set_font(family="Times", size=14, style="B")
pdf.cell(
    w=0,
    h=20,
    ln=1,
    txt="Description",
    align="L",
)

descText = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts of the Malay Peninsula and has been classified as Critically Endangered on the IUCN Red List in 2015. The population was roughly estimated at 250 to 340 adult individuals in 2013, likely comprises less than 200 mature breeding individuals and is considered to be extirpated on the island of Singapore, with no records since the 1930s. The Malayan tiger is the national animal of Malaysia."""

pdf.set_font(family="Times", size=12, style="")
pdf.multi_cell(w=0, h=15, txt=descText, align="L")

pdf.set_font(family="Times", size=12, style="B")
pdf.cell(w=100, h=25, txt="Kingdom: ")

pdf.set_font(family="Times", size=12, style="")
pdf.cell(w=100, h=25, txt="Animalia", ln=1)

pdf.set_font(family="Times", size=12, style="B")
pdf.cell(w=100, h=25, txt="Phylum: ")

pdf.set_font(family="Times", size=12, style="")
pdf.cell(w=100, h=25, txt="Chordata", ln=1)

pdf.output(
    "Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_1/tiger.pdf"
)
