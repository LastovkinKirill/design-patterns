from collections.abc import Iterable

from iterator_pattern.iterator.interface import SquareIterator


class Squares(Iterable):
	def __init__(self, n, iterator_cls: type[SquareIterator]):
		self.iterator = iterator_cls(n)

	# do not need next, abc Iterable do not violate
	# def __next__(self):
	# 	pass

	def __iter__(self):
		return self.iterator
