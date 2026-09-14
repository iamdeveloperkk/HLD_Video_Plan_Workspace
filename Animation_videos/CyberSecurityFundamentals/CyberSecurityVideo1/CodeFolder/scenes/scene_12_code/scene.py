"""Programmatic animation scene for Cyber Attack X FAANG Video 1."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SHARED_ROOT = ROOT / "Animation_videos"
if str(SHARED_ROOT) not in sys.path:
    sys.path.insert(0, str(SHARED_ROOT))
VIDEO_ROOT = SHARED_ROOT / "CyberSecurityFundamentals" / "CyberSecurityVideo1" / "CodeFolder"
if str(VIDEO_ROOT) not in sys.path:
    sys.path.insert(0, str(VIDEO_ROOT))

from PIL import ImageDraw
from _common.engine.canvas import BLUE, PANEL, WHITE, MUTED, Canvas
from _common.engine.components import Component
from _common.engine.layout import Rect, LayoutError, assert_inside, validate_elements
from _common.engine.renderer import Renderer
from _common.engine.typography import font, centered_text
from video_config import CANVAS
from scenes.scene_12_code.config import *

RED = (235, 70, 80)
GREEN = (72, 205, 135)
YELLOW = (242, 190, 70)
GRID = (20, 44, 72)

def fade_alpha(elapsed, reveal, duration=0.55):
    x = max(0.0, min(1.0, (elapsed - reveal) / duration))
    return int((x * x * (3 - 2*x)) * 255)

def rgba(rgb, a):
    return (*rgb, max(0, min(255, int(a))))

class Box(Component):
    def __init__(self, name, bounds, label, reveal=0.0, fill=PANEL, border=BLUE, sublabel=None):
        super().__init__(name, bounds, reveal=reveal)
        self.label, self.fill, self.border, self.sublabel = label, fill, border, sublabel
    def input(self): return (self.x, self.y + self.height/2)
    def output(self): return (self.x + self.width, self.y + self.height/2)
    def draw(self, image, elapsed, active=False):
        a = fade_alpha(elapsed, self.reveal)
        if not a: return
        d = ImageDraw.Draw(image)
        fill = RED if active else self.fill
        border = RED if active else self.border
        d.rounded_rectangle((self.x,self.y,self.bounds.right,self.bounds.bottom), radius=12,
                            fill=rgba(fill,a), outline=rgba(border,a), width=2)
        centered_text(d,(self.x+10,self.y+18,self.bounds.right-10,self.y+self.height/2+8),
                      self.label,font(17,True),rgba(WHITE,a))
        if self.sublabel:
            centered_text(d,(self.x+10,self.y+self.height/2+8,self.bounds.right-10,self.bounds.bottom-10),
                          self.sublabel,font(12),rgba(MUTED,a))

class Line(Component):
    def __init__(self, name, p1, p2, reveal=0.0, width=3, fill=BLUE):
        x=min(p1[0],p2[0]); y=min(p1[1],p2[1])
        w=max(1,abs(p2[0]-p1[0])); h=max(1,abs(p2[1]-p1[1]))
        super().__init__(name,Rect(x,y,w,h),reveal=reveal,allow_overlap=True)
        self.p1,self.p2,self.line_width,self.fill=p1,p2,width,fill
    def draw(self,image,elapsed,active=False):
        a=fade_alpha(elapsed,self.reveal,0.45)
        if not a:return
        d=ImageDraw.Draw(image)
        d.line((self.p1[0],self.p1[1],self.p2[0],self.p2[1]),fill=rgba(self.fill,a),width=self.line_width)
        # directional tip
        x1,y1=self.p1; x2,y2=self.p2
        import math
        ang=math.atan2(y2-y1,x2-x1)
        L=10
        pts=[(x2,y2),(x2-L*math.cos(ang-0.45),y2-L*math.sin(ang-0.45)),
             (x2-L*math.cos(ang+0.45),y2-L*math.sin(ang+0.45))]
        d.polygon(pts,fill=rgba(self.fill,a))

class Dot(Component):
    def __init__(self,name,x,y,reveal=0.0,r=7,fill=RED):
        super().__init__(name,Rect(x-r,y-r,2*r,2*r),reveal=reveal,allow_overlap=True)
        self.cx,self.cy,self.r,self.fill=x,y,r,fill
    def draw(self,image,elapsed,active=False):
        a=fade_alpha(elapsed,self.reveal,0.35)
        if not a:return
        d=ImageDraw.Draw(image)
        d.ellipse((self.cx-self.r,self.cy-self.r,self.cx+self.r,self.cy+self.r),fill=rgba(self.fill,a))

class Meter(Component):
    def __init__(self,name,bounds,label,reveal,value=0.0,fill=BLUE):
        super().__init__(name,bounds,reveal=reveal)
        self.label,self.value,self.fill=label,value,fill
    def draw(self,image,elapsed,active=False):
        a=fade_alpha(elapsed,self.reveal,0.55)
        if not a:return
        d=ImageDraw.Draw(image)
        d.rounded_rectangle((self.x,self.y,self.bounds.right,self.bounds.bottom),radius=10,
                            fill=rgba(PANEL,a),outline=rgba(BLUE,a),width=1)
        d.text((self.x+14,self.y+10),self.label,font=font(13,True),fill=rgba(MUTED,a))
        bar_x=self.x+14; bar_y=self.y+43; bar_w=self.width-28; bar_h=18
        d.rounded_rectangle((bar_x,bar_y,bar_x+bar_w,bar_y+bar_h),radius=8,fill=rgba((30,55,82),a))
        fill_w=bar_w*max(0,min(1,self.value))
        color=RED if active else self.fill
        d.rounded_rectangle((bar_x,bar_y,bar_x+fill_w,bar_y+bar_h),radius=8,fill=rgba(color,a))

def draw_header(image, elapsed):
    d = ImageDraw.Draw(image)
    d.text((50,35), "BIG-TECH SECURITY IS LAYERS", font=font(26,True), fill=WHITE)
    d.text((50,70), "Cyber Attack X FAANG  •  Security Fundamentals", font=font(16), fill=MUTED)

def draw_panel(image, title, points, reveals, elapsed):
    x,y,w,h = RIGHT_PANEL
    d=ImageDraw.Draw(image)
    d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill=PANEL,outline=(29,75,121),width=2)
    d.text((x+18,y+18),title,font=font(13,True),fill=BLUE)
    yy=y+58
    for i,(point,rev) in enumerate(zip(points,reveals),1):
        a=fade_alpha(elapsed,rev,0.45)
        if not a: continue
        d.ellipse((x+18,yy+5,x+25,yy+12),fill=rgba(BLUE,a))
        d.text((x+34,yy),point,font=font(13),fill=rgba(WHITE,a))
        yy += 64 if len(point)>45 else 54

def draw_takeaway(image, text, reveal, elapsed):
    if elapsed < reveal:return
    a=fade_alpha(elapsed,reveal,0.7)
    x,y,w,h=MAIN_PANEL
    d=ImageDraw.Draw(image)
    box=(x+35,y+410,x+w-35,y+472)
    d.rounded_rectangle(box,radius=10,fill=rgba(PANEL,a),outline=rgba(BLUE,a),width=1)
    d.text((box[0]+18,box[1]+9),"TAKEAWAY",font=font(11,True),fill=rgba(BLUE,a))
    d.text((box[0]+18,box[1]+28),text,font=font(16,True),fill=rgba(WHITE,a))

def validate_scene(elements):
    try:
        panel=Rect(*MAIN_PANEL)
        validate_elements([e for e in elements if getattr(e,"bounds",None) and not getattr(e,"allow_overlap",False)],panel)
        for e in elements:
            if hasattr(e,"bounds") and e.bounds.x < panel.x-1: assert_inside(e,panel)
    except LayoutError as exc:
        print("LAYOUT VALIDATION: FAILED")
        print(f"- {exc}")
        raise SystemExit(1) from exc
    print("LAYOUT VALIDATION: PASS")

def render(output):
    Renderer(CANVAS).render(lambda elapsed: make_frame(elapsed), output)

def render_scene(output):
    render(output)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path("scene_output.mp4"))
    args=parser.parse_args()
    render(args.output)

if __name__=="__main__":
    main()

def make_frame(elapsed):
    image=Renderer(CANVAS).background(); d=ImageDraw.Draw(image); draw_header(image,elapsed)
    d.rounded_rectangle((MAIN_PANEL[0],MAIN_PANEL[1],MAIN_PANEL[0]+MAIN_PANEL[2],MAIN_PANEL[1]+MAIN_PANEL[3]),radius=14,fill=PANEL,outline=(29,75,121),width=2)
    left=80; top=155; width=730; height=44; gap=10
    layers=[]
    for i,label in enumerate(LAYERS):
        y=top+i*(height+gap)
        b=Box(label,Rect(left,y,width,height),label,LAYER_REVEALS[i],fill=(22+3*i,34+4*i,55+5*i),border=BLUE)
        layers.append(b); b.draw(image,elapsed,active=(elapsed>=ATTACK_REVEAL and i in (2,5)))
        if i>0:
            Line(f"layer{i}",(left+width/2,y-6),(left+width/2,y),LAYER_REVEALS[i],2,BLUE).draw(image,elapsed)
    if elapsed>=ATTACK_REVEAL:
        d.rounded_rectangle((left+230,top+2*(height+gap)-4,left+500,top+2*(height+gap)+height+8),radius=8,outline=rgba(RED,230),width=3)
        d.text((left+245,top+2*(height+gap)+8),"ATTACK STOPPED",font=font(14,True),fill=rgba(RED,240))
    draw_panel(image,SCENE_TITLE,DISCUSSION_POINTS,DISCUSSION_REVEALS,elapsed)
    draw_takeaway(image,TAKEAWAY,TAKEAWAY_REVEAL,elapsed)
    return image
