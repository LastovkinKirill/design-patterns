from iterator_pattern.iterator.interface import SquareIterator


# Iterator
class SquareIteratorImplementation(SquareIterator):
	def __next__(self):
		if self.current < self.n:
			result = self.current ** 2
			self.current += 1
			return result
		else:
			raise StopIteration


# Iterator
class SquareIteratorImplementation2(SquareIterator):
	def __next__(self):
		if self.current < self.n:
			result = self.current * self.current
			self.current += 1
			return result
		else:
			raise StopIteration
