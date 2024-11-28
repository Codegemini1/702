def multiplication(a,b):
	result = a * b
	return result

def int_filter(*args):
	l = []
	for i in args:
		if type(i)==int:
			l.append(i)
	return l