from collections import Counter

def Peptide_spectrum(peptide):
	peptides = [peptide, tuple()]
	N = len(peptide)
	for length in range(1, N):
		for i in range(N - length):
			peptides.append(peptide[i : i + length])
	Peptide_spectrum = [Mass(peptide) for peptide in peptides]
	return sorted(Peptide_spectrum)


def Cyclospectrum(peptide):
	peptides = [peptide, tuple()]
	N = len(peptide)
	for length in range(1, N):
		for i in range(N):
			peptides.append(peptide[i : (i + length)])
	Cyclospectrum = [Mass(peptide) for peptide in peptides]
	return sorted(Cyclospectrum)


def Mass(peptide):
	mass = 0
	for weight in peptide:
		mass += weight
	return mass


def expand(leaderboard):
	expanded = []
	for peptide in leaderboard:
		for weight in weights:
			expanded.append(peptide + (weight,))
	return expanded

        
def CyclicScore(peptide, Spectrum):
	CyclicScore = 0
	for weight in Cyclospectrum(peptide):
		if weight in Spectrum:
			CyclicScore += 1
	return CyclicScore


def Score(peptide, Spectrum):
	Score = 0
	for weight in Peptide_spectrum(peptide):
		if weight in Spectrum:
			Score += 1
	return Score


def Cut(leaderboard, Spectrum, N):
	Scores = {}

	for peptide in leaderboard:
		Scores[peptide] = Score(peptide, Spectrum)

	leaderboard.sort(reverse = True, key = lambda x: Scores[x])

	if len(leaderboard) <= N:
		return leaderboard

	cutted = leaderboard[:N]

	for i in range(N, len(leaderboard)):
		prev = Score(leaderboard[i - 1], Spectrum)
		curr = Score(leaderboard[i], Spectrum) 
         
		if prev == curr:
			cutted.append(leaderboard[i])
		else:
			break
	return cutted

def sequence_leaderboard_cyclopeptide(Spectrum, N):
	new_leaderboard = [tuple()]
	leader_peptide = tuple()
	ParentMass = max(Spectrum)

	while True:
		leaderboard = expand(new_leaderboard)
		new_leaderboard = []

		for peptide in leaderboard:
			mass = Mass(peptide)

			if mass == ParentMass:
				if CyclicScore(peptide, Spectrum) > CyclicScore(leader_peptide, Spectrum):
					leader_peptide = peptide
			elif mass < ParentMass:
				new_leaderboard.append(peptide)
		new_leaderboard = Cut(new_leaderboard, Spectrum, N)

		if not new_leaderboard:
			break
		leader_peptide = new_leaderboard[0]
	return leader_peptide



def get_convolution(spectrum):

	Convolution = Counter()
	for i in range(1, len(spectrum)):
		for j in range(i):
			diff = spectrum[i] - spectrum[j]
			if  (57 <= diff <= 200):
				Convolution[diff] += 1
	return Convolution


def create_spectrum(Convolution, M):
    
	global weights
	weights = []
	most_common = Convolution.most_common()
	for i in range(len(Convolution)):
		if i < M:
			weights.append(most_common[i][0])
		elif most_common[i][1] == most_common[M - 1][1]:
			weights.append(most_common[i][0])


def sequence_convolution_cyclopeptide(spectrum, N, M):
	Convolution = get_convolution(spectrum)
	create_spectrum(Convolution, M)
	return sequence_leaderboard_cyclopeptide(spectrum, N)
                

def main():

	with open('/home/masha/Загрузки/rosalind_ba4i.txt', 'r') as f: 
		M = int(f.readline())
		N = int(f.readline())
		Spectrum = [int(elem) for elem in f.readline().split()]

	cyclopeptide = sequence_convolution_cyclopeptide(Spectrum, N, M)
	output = "-".join(str(weight) for weight in cyclopeptide)

	with open('/home/masha/Загрузки/output.txt', 'w') as f: 
    		f.write(output)

if __name__ == "__main__":
		main()

