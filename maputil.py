__author__ = 'zhangcheng'

import math,sys
from collections import namedtuple


Field = namedtuple('Field', 'p1,p2,p3,p4')
Segment = namedtuple('Segment', 'p1,p2')
Segment.__str__ = lambda s: '%f,%f,%f,%f\n' % \
            (s.p1[0],s.p1[1],s.p2[0],s.p2[1])
Tcfg = namedtuple('Tcfg', 'cut,ll')


def err_n_quit(e):
    sys.exit(e)

def pnorm(p):
    return (p[0]/math.sqrt(p[0]*p[0]+p[1]*p[1]),
            p[1]/math.sqrt(p[0]*p[0]+p[1]*p[1]))

def padd(a,b): return map(lambda x, y: x+y, a, b)
def pmul(a,n): return (n*a[0], n*a[1])

def is_line_seg_intersect(line, seg):
    def dot(v1, v2):
        return v1[0]*v2[0]+v1[1]*v2[1]

    norm = (line.p2[1]-line.p1[1], line.p1[0]-line.p2[0])
    diff1 = (seg.p1[0]-line.p1[0], seg.p1[1]-line.p1[1])
    diff2 = (seg.p2[0]-line.p1[0], seg.p2[1]-line.p1[1])

    d1, d2 = dot(diff1, norm) , dot(diff2,norm)

    return (d1 > 0 > d2) or (d1 < 0 < d2)
def line_seg_intersect(line, seg):
    return line2_intersect (line, seg) if is_line_seg_intersect(line, seg) else None



def line2_intersect(line1, line2):
    x1,y1 = line1.p1
    x2,y2 = line1.p2
    x3,y3 = line2.p1
    x4,y4 = line2.p2

    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)),
            ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)))

