#!/usr/bin/env python3
"""Rebuild the first Republic of Alba SAMA-only PDF layout prototype.

Requires: pip install reportlab
Not an enacted constitution; SAMA 0.16.0 supports only a limited text.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

output = Path(__file__).resolve().parents[1] / "constitution" / "Constitution_Alba_Draft_v0.1.pdf"
output.parent.mkdir(parents=True, exist_ok=True)
W, H = A4
red = HexColor("#5B1623")
gold = HexColor("#C8AA72")
ink = HexColor("#1E1B19")
c = canvas.Canvas(str(output), pagesize=A4)
c.setTitle("Alba: constitutional design prototype 0.1; NOT ENACTED")
c.setSubject("SAMA-only preliminary layout with five vocabulary-bounded statements")
c.setFillColor(red)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setStrokeColor(gold)
c.rect(22*mm, 22*mm, W-44*mm, H-44*mm)
c.rect(25*mm, 25*mm, W-50*mm, H-50*mm)
x, y = W/2, H-270
c.circle(x,y,27*mm)
c.circle(x,y,20*mm)
p=c.beginPath();p.moveTo(x,y+16*mm);p.lineTo(x+14*mm,y-10*mm);p.lineTo(x-14*mm,y-10*mm);p.close();c.drawPath(p)
c.setFillColor(gold)
c.setFont("Times-Bold",37);c.drawCentredString(W/2,H*.49,"ALBA")
c.setFont("Times-Roman",18);c.drawCentredString(W/2,H*.405,'LAWI DE "Alba"')
c.setFont("Times-Roman",12);c.drawCentredString(W/2,H*.38,"DOKU 0.1")
c.setFont("Times-Roman",10);c.drawCentredString(W/2,52*mm,"SAMA 0.16.0");c.drawCentredString(W/2,44*mm,"22.11.2026")
c.showPage()
c.setFillColor(HexColor("#F7F4EB"));c.rect(0,0,W,H,fill=1,stroke=0)
L,R=30*mm,W-15*mm; X=(L+R)/2
c.setFillColor(ink);c.setFont("Times-Roman",10);c.drawCentredString(W/2,H-10*mm,"2")
c.setStrokeColor(gold);c.line(L,H-28*mm,R,H-28*mm)
c.setFont("Times-Bold",14);c.drawCentredString(X,H-43*mm,"ALBA")
c.setFont("Times-Roman",17);c.drawCentredString(X,H-57*mm,'LAWI DE "Alba"')
c.setFont("Times-Italic",10);c.drawCentredString(X,H-65*mm,"SAMA 0.16.0 / DOKU 0.1")
y=H-89*mm
for title, verses in [
    ("KOMA",['"Alba" bi koma de sitano li.',"Sitano li bi soma.","Tawa sitano li bi sama."]),
    ("LAWI",['Lawi de "Alba" bi yoma.']),
    ("ELEKA",["Eleka bi yoma."]),
]:
    c.setFont("Times-Bold",14);c.drawCentredString(X,y,title);y-=13*mm
    for verse in verses:
        n=1+sum(len(part) for heading,part in [("KOMA",['a','b','c'])] if False)
        c.setFont("Times-Roman",14);c.drawString(L+12.5*mm,y,verse);y-=12*mm
    y-=8*mm
c.setFont("Times-Roman",10);c.drawCentredString(X,27*mm,"ALBA / SAMA / DOKU 0.1")
c.save()
print(output)
