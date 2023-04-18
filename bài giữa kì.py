CHARS = 256

def getNextState(pat, M, state, x):
	if state < M and x == ord(pat[state]):
		return state+1

	i=0
	for y in range(state,0,-1):
		if ord(pat[y-1]) == x:
			while(i<y-1):
				if pat[i] != pat[state-y+1+i]:
					break
				i+=1
			if i == y-1:
				return y
	return 0
def computeTF(pat, M):
	global CHARS
	TF = [[0 for i in range(CHARS)]\
		for _ in range(M+1)]

	for state in range(M+1):
		for x in range(CHARS):
			z = getNextState(pat, M, state, x)
			TF[state][x] = z
	return TF
  
def search(pat, txt):
	global CHARS
	M = len(pat)
	N = len(txt)
	TF = computeTF(pat, M)

	state=0
	for i in range(N):
		state = TF[state][ord(txt[i])]
		if state == M:
			print("Pattern found at index: {}".\
				format(i-M+1))
	
def main():
	txt = "ABAACAADAABAAABAA"
	pat = "AABA"
	search(pat, txt)

if __name__ == '__main__':
	main()
