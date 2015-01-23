import cartesius.main as cartesius
import cartesius.elements as elements
import globs
# import cartesius.charts as charts
#
# coordinate_system = cartesius.CoordinateSystem()
#
# coordinate_system.add(elements.Line((0, 0), (-.7, -.7)))
# coordinate_system.add(elements.Line((.5, -.5), (-.5, .5), color=(0, 255, 0)))
# coordinate_system.add(elements.Line((0, 0), (7, 3), color=(0, 0, 255)))
# image = coordinate_system.draw(600, 400, antialiasing=True)
# image.show()
#
# image.save('gpx_elevations.png')
def get_bounds():
    f = globs.field
    r = globs.refline
    xlist = [f.p1[0], f.p2[0],f.p3[0], f.p4[0], r.p1[0], r.p2[0]]
    ylist = [f.p1[1], f.p2[1],f.p3[1], f.p4[1], r.p1[1], r.p2[1]]
    scale = 0.2
    bound =  (min(xlist), max(xlist), min(ylist), max(ylist))
    width, height = bound[1]- bound[0], bound[3] - bound[2]
    return (bound[0] - scale*width, bound[1]+scale*width,
            bound[2] - scale*height, bound[3]+scale*height)

def seg_plot(field, seg, ref):
    coord = cartesius.CoordinateSystem(bounds=get_bounds())
    coord.add(elements.Line(field.p1, field.p2, color=(0, 255, 0)))
    coord.add(elements.Line(field.p2, field.p3, color=(0, 255, 0)))
    coord.add(elements.Line(field.p3, field.p4, color=(0, 255, 0)))
    coord.add(elements.Line(field.p4, field.p1, color=(0, 255, 0)))

    for s in seg:
        coord.add(elements.Line(s.p1, s.p2, color=(255, 0, 0)))
    coord.add(elements.Line(ref.p1, ref.p2, color=(0, 0, 255)))

    return coord.draw(600, 400 ,antialiasing=True)

