from iterator_pattern.iterator import Squares, SquareIteratorImplementation, SquareIteratorImplementation2

"""
1. Hide complex algorithm for client code
2. Separate iteration algorithm from collection 

"""


# client code

def get_squares(squares: Squares) -> tuple[int]:
	return tuple(squares)


if __name__ == '__main__':
	print(get_squares(Squares(5, SquareIteratorImplementation)))
	print(get_squares(Squares(5, SquareIteratorImplementation2)))
