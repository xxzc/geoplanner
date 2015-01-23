__author__ = 'zhangcheng'

import unittest
from mapcut import *
import globs


class GeoTest(unittest.TestCase):
    def setUp(self):
        read_conf()
        print globs.field
    def test_someins(self):
        print "Intersecton:"
        #self.assertTrue(is_line_seg_intersect(globs.refline, Segment(globs.field.p1, globs.field.p2)))
        #self.assertFalse(is_line_seg_intersect(globs.refline, Segment(globs.field.p2, globs.field.p3)))
        #self.assertTrue(is_line_seg_intersect(globs.refline, Segment(globs.field.p3, globs.field.p4)))
        #self.assertFalse(is_line_seg_intersect(globs.refline, Segment(globs.field.p4, globs.field.p1)))

    def test_ins(self):
        print "Ins point:"
        print line_seg_intersect(globs.refline, Segment(globs.field.p1, globs.field.p2))
        print line_seg_intersect(globs.refline, Segment(globs.field.p2, globs.field.p3))

    def test_field(self):
        print "Field Ins:"
        print field_line_intersects(globs.refline)

    def test_segments(self):
        print "Segment:"
        segments_calc()
        write_segments()

        img = segplot.seg_plot(globs.field, globs.segments_result, globs.refline)
        img.save('plot.png')
        img.show()
        print globs.segments_result

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(GeoTest)
    unittest.TextTestRunner(verbosity=2).run(suite)