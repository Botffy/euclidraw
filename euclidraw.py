from PIL import Image, ImageDraw
from euclid import *

class EucliDraw(ImageDraw.ImageDraw):
	def __init__(self, im, mode=None):
		ImageDraw.ImageDraw.__init__(self, im, mode)
		self.__maxlen = (self.im.size[0]**2 + self.im.size[1]**2)**0.5

	def line(self, xy, **kwargs):
		if isinstance(xy, LineSegment2):
			xy = (xy.p1.x, xy.p1.y, xy.p2.x, xy.p2.y)
		elif isinstance(xy, Ray2):
			p2 = xy.p + (xy.v * self.__maxlen)
			xy = (xy.p.x, xy.p.y, p2.x, p2.y)
		elif isinstance(xy, Line2):
			p1 = xy.p + (xy.v * -self.__maxlen)
			p2 = xy.p + (xy.v * self.__maxlen)
			xy = (p1.x, p1.y, p2.x, p2.y)
		ImageDraw.ImageDraw.line(self, xy, **kwargs)

	def circle(self, bbox, **kwargs):
		if isinstance(bbox, Circle):
			bbox = (bbox.c.x-bbox.r, bbox.c.y-bbox.r, bbox.c.x+bbox.r, bbox.c.y+bbox.r)
		ImageDraw.ImageDraw.ellipse(self, bbox, **kwargs)

if __name__ == "__main__":
	image = Image.new("RGB", (800, 600), "white")
	draw = EucliDraw(image)

	line = Line2(Point2(1,0), Point2(10, 10))
	draw.line(line, fill="red")

	ray = Ray2(Point2(200,50), Point2(20, 20))
	draw.line(ray, fill="blue")

	image.show()
