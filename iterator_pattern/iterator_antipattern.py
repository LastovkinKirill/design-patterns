# client code

def get_squares(n: int) -> list[int]:
	r = []
	# complex algorithm
	# and I don't want to change it in the future, even I need other implementation
	# because it is client code, and we can break it and violate OCP
	for value in range(n):
		r.append(value * 2)

	return r


if __name__ == '__main__':
	print(get_squares(5))
