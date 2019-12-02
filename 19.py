

weights = {
		'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 
  		'G': 57, 'H': 137, 'I': 113, 'K': 128, 'L': 113, 
		'M': 131, 'N': 114, 'P': 97, 'Q': 128, 'R': 156, 
 		'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163}



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
	peptide += peptide
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
		for weight in weights.values():
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
	for elem in Peptide_spectrum(peptide):
		if elem in Spectrum:
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
	return leader_peptide
                

def main():

	with open('/home/masha/Загрузки/rosalind_ba4g.txt', 'r') as f: 
		N = int(f.readline())
		Spectrum = [int(elem) for elem in f.readline().split()]

	cyclopeptide = sequence_leaderboard_cyclopeptide(Spectrum, N)
	output = "-".join(str(weight) for weight in cyclopeptide)

	with open('/home/masha/Загрузки/output.txt', 'w') as f: 
    		f.write(output)

if __name__ == "__main__":
		main()

