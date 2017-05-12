from fontTools.pens.basePen import BasePen

class GlyphToBezPen(BasePen):
	def __init__(self, glyphSet, allowDecimals=False):
		super().__init__(glyphSet)

		self.bezProgram = []
		self.allowDecimals = allowDecimals
		self.markingOpSeen = False

	def _p(self, pt):
		x, y = pt
		if self.allowDecimals:
			return "%.2f  %.2f" % (x, y)
		else:
			x = int(round(x))
			y = int(round(y))
			return "%d %d" % (x, y)

	def _sc(self):
		if not self.markingOpSeen:
			self.markingOpSeen = True
			self.bezProgram.append("sc")

	def _moveTo(self, pt):
		self._sc()
		pt = self._p(pt)
		self.bezProgram.append("%s mt" % pt)

	def _lineTo(self, pt):
		self._sc()
		pt = self._p(pt)
		self.bezProgram.append("%s dt" % pt)

	def _curveToOne(self, pt1, pt2, pt3):
		self._sc()
		pt1 = self._p(pt1)
		pt2 = self._p(pt2)
		pt3 = self._p(pt3)
		self.bezProgram.append("%s %s %s ct" % (pt1, pt2, pt3))

	def _closePath(self):
		self.bezProgram.append("cp")

	def _endPath(self):
		if self.bezProgram and self.bezProgram[-1] != "cp":
			self.bezProgram.append("cp")
		self.bezProgram.append("ed")

	def getBezString(self):
		return "\n".join(self.bezProgram)
