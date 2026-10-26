from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pathlib import Path
Path('public').mkdir(exist_ok=True)
c=canvas.Canvas('public/kabir-mehta-cv.pdf',pagesize=(595.28,841.89));c.setTitle('Kabir Mehta - Fictional Demo Resume');c.setAuthor('Kabir Mehta demo portfolio')
def line(x,y,t,size=10,color='#444b59',font='Helvetica'):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,t)
def rule(y):
 c.setStrokeColor(HexColor('#dce0e9'));c.line(45,y,550,y)
def heading(y,t):line(45,y,t,14,'#1b2030','Helvetica-Bold')
c.setFillColor(HexColor('#6b48d7'));c.rect(0,819,595.28,23,fill=1,stroke=0)
line(45,769,'Kabir Mehta',32,'#171b28','Helvetica-Bold');line(45,743,'PRODUCT DESIGNER',10,'#6745cc','Helvetica-Bold')
line(45,718,'Bengaluru, India | Remote worldwide',10);line(45,700,'hello@kabirmehta.design | +91 99001 23456',10)
c.setFillColor(HexColor('#f0ecfa'));c.roundRect(45,644,505,37,5,fill=1,stroke=0)
line(57,666,'FICTIONAL DEMO RESUME',8,'#5d3ba9','Helvetica-Bold');line(57,653,'Employment, metrics and contact details are illustrative, not verified credentials.',8,'#57496d')
heading(617,'Profile')
for i,t in enumerate(['Product designer with seven years across fintech, health and commerce.','Research, interaction design and front-end understanding come together to help','teams ship clear, accessible products. Open to freelance and senior full-time roles.']):line(45,597-i*15,t,10)
rule(548);heading(526,'Experience')
for y,d,title,body in [(499,'2024 - Present','Independent product designer','Partnering with early-stage teams from discovery to launch.'),(431,'2022 - 2024','Product designer - Practo (fictional role)','Illustrative clinic workflow and dashboard design experience.'),(363,'2019 - 2022','Product designer - Razorpay (fictional role)','Illustrative UPI onboarding and merchant product experience.')]:
 line(45,y,d,9,'#6b48c9','Helvetica-Bold');line(170,y,title,11,'#242a38','Helvetica-Bold');line(170,y-19,body,9)
rule(319);heading(297,'Selected work - demo outcomes')
for i,(a,b) in enumerate([('PayKaro','UPI activation: 41% to 79% (+38 percentage points).'),('GreenCart','22% less checkout drop-off.'),('MedNest','3x faster appointment booking.'),('Yatra Lite','1.2-second first load on 3G (fictional project metric).')]):
 line(45,274-i*23,a,10,'#242a38','Helvetica-Bold');line(145,274-i*23,b,9)
rule(183);heading(160,'Capabilities & tools')
line(45,139,'Product strategy | UX research | Interaction design | Design systems',9)
line(45,123,'Prototyping | Accessibility | Design-to-development handoff',9)
line(45,103,'Figma | FigJam | Framer | Maze | Notion | React',9)
line(45,65,'Portfolio: imrzaveri-beep.github.io/kabir-mehta-portfolio/',9,'#6745cc')
c.linkURL('https://imrzaveri-beep.github.io/kabir-mehta-portfolio/',(45,62,550,76),relative=0)
line(45,45,'Prepared 26 October 2026 | Demo data only - replace before professional use.',8,'#777c88');c.save()
