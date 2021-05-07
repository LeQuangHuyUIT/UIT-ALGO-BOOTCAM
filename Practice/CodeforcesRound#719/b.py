def precompute():
	L = []
	for i in range(1, 12):
		for digit in range(1, 10):
			L.append(int(str(digit)*i))
	return L

if __name__ == '__main__':
	L = precompute()
	t = int(input())
	while t > 0:
		t -= 1
		n = int(input())
		cnt = 0
		for x in L:
			if x <= n:
				cnt += 1
			else:
				break
		print(cnt)	