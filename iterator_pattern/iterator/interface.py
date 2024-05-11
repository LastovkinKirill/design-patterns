from collections.abc import Iterator


class SquareIterator(Iterator):
	def __init__(self, n: int):
		self.n = n
		self.current = 0

	# method do not need in iterator, abc Iterator do not violate
	# def __iter__(self):
	# 	pass

	def __next__(self):
		raise NotImplemented
