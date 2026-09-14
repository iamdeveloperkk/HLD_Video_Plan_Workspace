"""Programmatic animation scene for Cyber Attack X FAANG — Video 2."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
VIDEO_ROOT = ROOT / "CyberSecurityFundamentals" / "CyberSecurityVideo2"
CODE_ROOT = VIDEO_ROOT / "CodeFolder"
if str(CODE_ROOT) not in sys.path: sys.path.insert(0, str(CODE_ROOT))

from PIL import ImageDraw
from _common.engine.canvas import BLUE, PANEL, WHITE, MUTED
from _common.engine.components import Component
from _common.engine.layout import Rect
from _common.engine.renderer import Renderer
from _common.engine.typography import font, centered_text
from video_config import CANVAS

RED=(235,70,80); GREEN=(72,205,135); YELLOW=(242,190,70)

def fade(reveal, elapsed, duration=.55):
    x=max(0,min(1,(elapsed-reveal)/duration)); return int((x*x*(3-2*x))*255)
def rgba(c,a): return (*c,max(0,min(255,int(a))))

class Box(Component):
    def __init__(self,name,bounds,label,reveal=0,sublabel="",border=BLUE,fill=PANEL):
        super().__init__(name,bounds,reveal=reveal)
        self.label,self.sublabel,self.border,self.fill=label,sublabel,border,fill
    def input(self): return (self.x,self.y+self.height/2)
    def output(self): return (self.x+self.width,self.y+self.height/2)
    def draw(self,image,elapsed,active=False):
        a=fade(self.reveal,elapsed)
        if not a:return
        d=ImageDraw.Draw(image); border=RED if active else self.border
        fill=(65,35,40) if active else self.fill
        d.rounded_rectangle((self.x,self.y,self.bounds.right,self.bounds.bottom),radius=12,
                            fill=rgba(fill,a),outline=rgba(border,a),width=2)
        centered_text(d,(self.x+10,self.y+10,self.bounds.right-10,self.y+self.height*.58),
                      self.label,font(17,True),rgba(WHITE,a))
        if self.sublabel:
            centered_text(d,(self.x+10,self.y+self.height*.58,self.bounds.right-10,self.bounds.bottom-8),
                          self.sublabel,font(12),rgba(MUTED,a))

class Arrow(Component):
    def __init__(self,name,p1,p2,reveal=0,fill=BLUE,width=3):
        super().__init__(name,Rect(min(p1[0],p2[0]),min(p1[1],p2[1]),
                                   max(1,abs(p2[0]-p1[0])),max(1,abs(p2[1]-p1[1]))),
                         reveal=reveal,allow_overlap=True)
        self.p1,self.p2,self.fill,self.line_width=p1,p2,fill,width
    def draw(self,image,elapsed,active=False):
        a=fade(self.reveal,elapsed,.45)
        if not a:return
        d=ImageDraw.Draw(image); d.line((*self.p1,*self.p2),fill=rgba(self.fill,a),width=self.line_width)
        import math
        ang=math.atan2(self.p2[1]-self.p1[1],self.p2[0]-self.p1[0]); L=10
        pts=[self.p2,(self.p2[0]-L*math.cos(ang-.45),self.p2[1]-L*math.sin(ang-.45)),
             (self.p2[0]-L*math.cos(ang+.45),self.p2[1]-L*math.sin(ang+.45))]
        d.polygon(pts,fill=rgba(self.fill,a))

class Dot(Component):
    def __init__(self,name,start,end,reveal,duration=2.8,fill=RED):
        super().__init__(name,Rect(start[0]-8,start[1]-8,16,16),reveal=reveal,allow_overlap=True)
        self.start,self.end,self.duration,self.fill=start,end,duration,fill
    def draw(self,image,elapsed,active=False):
        if elapsed<self.reveal:return
        t=max(0,min(1,(elapsed-self.reveal)/self.duration))
        x=self.start[0]+(self.end[0]-self.start[0])*t
        y=self.start[1]+(self.end[1]-self.start[1])*t
        d=ImageDraw.Draw(image); d.ellipse((x-7,y-7,x+7,y+7),fill=self.fill)

def header(image,title):
    d=ImageDraw.Draw(image)
    d.text((50,35),title,font=font(26,True),fill=WHITE)
    d.text((50,70),"Cyber Attack X FAANG  •  Attack Mechanics",font=font(16),fill=MUTED)

def panel(image,points,reveals,elapsed):
    x,y,w,h=(930,45,300,405); d=ImageDraw.Draw(image)
    d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill=PANEL,outline=(29,75,121),width=2)
    d.text((x+18,y+18),"ATTACK MECHANICS",font=font(13,True),fill=BLUE)
    yy=y+58
    for p,r in zip(points,reveals):
        a=fade(r,elapsed,.45)
        if not a:continue
        d.ellipse((x+18,yy+5,x+25,yy+12),fill=rgba(BLUE,a))
        d.text((x+34,yy),p,font=font(13),fill=rgba(WHITE,a))
        yy+=78 if len(p)>46 else 58

def takeaway_box(image,text,elapsed):
    if elapsed<14:return
    a=fade(14,elapsed,.7); x,y,w,h=(35,105,875,515); d=ImageDraw.Draw(image)
    box=(x+35,y+410,x+w-35,y+472)
    d.rounded_rectangle(box,radius=10,fill=rgba(PANEL,a),outline=rgba(BLUE,a),width=1)
    d.text((box[0]+18,box[1]+9),"TAKEAWAY",font=font(11,True),fill=rgba(BLUE,a))
    d.text((box[0]+18,box[1]+28),text,font=font(15,True),fill=rgba(WHITE,a))

from scenes.scene_03_code.config import *

def make_frame(elapsed):
    image=Renderer(CANVAS).background(); d=ImageDraw.Draw(image)
    header(image,SCENE_TITLE)
    d.rounded_rectangle((35,105,910,620),radius=14,fill=PANEL,outline=(29,75,121),width=2)

    a=Box("browser",Rect(70,245,190,110),"VICTIM BROWSER",1.0,"authenticated")
    b=Box("api",Rect(650,245,180,110),"NEXA API",2.2,"sees session")
    a.draw(image,elapsed); b.draw(image,elapsed); Arrow("q",a.output(),b.input(),2.2).draw(image,elapsed)
    Dot("request",a.output(),b.input(),3.2).draw(image,elapsed)
    if elapsed>=6:
        d.rounded_rectangle((300,205,570,385),radius=12,fill=rgba((65,35,40),235),outline=rgba(RED,240),width=2)
        centered_text(d,(315,220,555,265),"CROSS-SITE ACTION",font(17,True),WHITE)
        centered_text(d,(315,275,555,345),"browser sends a request",font(16),WHITE)
    if elapsed>=9: d.text((335,400),"CSRF TOKEN / SAME-SITE",font=font(14,True),fill=GREEN)

    panel(image,DISCUSSION_POINTS,DISCUSSION_REVEALS,elapsed)
    takeaway_box(image,TAKEAWAY,elapsed)
    return image

def main():
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,default=Path("scene_output.mp4")); a=p.parse_args()
    Renderer(CANVAS).render(make_frame,a.output)

def render_scene(output):
    Renderer(CANVAS).render(make_frame, output)

if __name__=="__main__": main()
