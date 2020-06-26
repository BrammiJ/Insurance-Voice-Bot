from fpdf import FPDF
pdf =  FPDF()
pdf.add_page(orientation='p')
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt="this is pravin kumar",ln=1,align="C")
pdf.line(10,10,10,100)
pdf.set_line_width(1)
pdf.set_draw_color(255,0,0)

pdf.cell(100,10,txt="this is pravin kumar",ln=2,align="C")
pdf.cell(200,10,txt="this is pravin kumar",ln=2,align="C")
pdf.output("pravinsample.pdf")
