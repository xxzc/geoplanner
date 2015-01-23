__author__ = 'zhangcheng'

from maputil import *
import globs
import segplot

def read_conf():
    def read_pair(fileo):
        line = fileo.readline()
        return map(float, line.split(','))

    objf = open('mapinfo.cfg', 'r')
    p1 = read_pair(objf)
    p2 = read_pair(objf)
    p3 = read_pair(objf)
    p4 = read_pair(objf)
    if is_line_seg_intersect(Segment(p1, p2), Segment(p3, p4)) and \
       is_line_seg_intersect(Segment(p3, p4), Segment(p1, p2)):
        p3 , p4 = p4 , p3
    globs.field = Field(p1, p2, p3, p4)
    p5 = read_pair(objf)
    p6 = read_pair(objf)
    globs.refline = Segment(p5, p6)
    objf.close()

    cfgf = open('objinfo.cfg', 'r')
    globs.tcfg = Tcfg(*read_pair(cfgf))
    cfgf.close()
    print globs.field

def seg_cut_head(seg):
    s_len = globs.tcfg.cut
    x1, y1 = seg.p1
    x2, y2 = seg.p2
    norm = pnorm((x2 - x1, y2 - y1))
    return Segment(padd(seg.p1, pmul(norm, s_len)), padd(seg.p2, pmul(norm, -s_len)))

def field_line_intersects(line):
    """

    :rtype : Segment
    """
    intersects = []
    ins = line_seg_intersect(line, Segment(globs.field.p1, globs.field.p2))
    if ins is not None:
        intersects.append(ins)

    ins = line_seg_intersect(line, Segment(globs.field.p2, globs.field.p3))
    if ins is not None:
        intersects.append(ins)

    ins = line_seg_intersect(line, Segment(globs.field.p3, globs.field.p4))
    if ins is not None:
        intersects.append(ins)

    ins = line_seg_intersect(line, Segment(globs.field.p4, globs.field.p1))
    if ins is not None:
        intersects.append(ins)

    if len(intersects) < 2:
        return None
    return Segment(intersects[0], intersects[1])


def segments_calc():
    x1, y1 = globs.refline.p1
    x2, y2 = globs.refline.p2
    norm = (y2 - y1, x1 - x2)
    norm = pnorm(norm)
    span = globs.tcfg.ll

    seg_plus = []
    seg_minus = []
    n = 1
    while True:
        try:
            new_seg = field_line_intersects(Segment(
                padd(globs.refline.p1, pmul(norm, n * span)),
                padd(globs.refline.p2, pmul(norm, n * span))))
            if new_seg is None:
                break
            if len(seg_plus)>1000: break
            seg_plus.append(new_seg)
        except:
            pass
        n += 1
    n = 1
    while True:
        try:
            new_seg = field_line_intersects(Segment(
                padd(globs.refline.p1, pmul(norm, -n * span)),
                padd(globs.refline.p2, pmul(norm, -n * span))))
            if new_seg is None:
                break
            seg_minus.append(new_seg)
            if len(seg_minus)>1000: break
        except:
            pass
        n += 1
    seg_minus.reverse()

    globs.segments_result = map(seg_cut_head, seg_minus + [globs.refline, ] + seg_plus)

def write_segments():
    f = open('seginfo.out','w')
    f.writelines(map(Segment.__str__, globs.segments_result))
    f.close()

if __name__ == '__main__':
    read_conf()
    print(globs.field)
    print(globs.refline)
    print(globs.tcfg)