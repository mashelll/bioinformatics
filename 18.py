

weights = {
		'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 
  		'G': 57, 'H': 137, 'I': 113, 'K': 128, 'L': 113, 
		'M': 131, 'N': 114, 'P': 97, 'Q': 128, 'R': 156, 
 		'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163}



def Peptide_spectrum(peptide):
	peptides = [peptide, ""]
	N = len(peptide)
	for length in range(1, N):
		for counter in range(N - length):
			peptides.append(peptide[counter:counter + length])
	Peptide_spectrum = [Mass(peptide) for peptide in peptides]
	return sorted(Peptide_spectrum)

    
def peptide_is_consistent(peptide, Spectrum):
	peptide_spectrum = Peptide_spectrum(peptide)
	for elem in peptide_spectrum:
		if elem not in Spectrum:
			return False
	return True

def Cyclospectrum(peptide):
	peptides = [peptide, ""]
	N = len(peptide)
	peptide += peptide
	for length in range(1, N):
		for i in range(N):
			peptides.append(peptide[i : (i + length)])
	Cyclospectrum = [Mass(peptide) for peptide in peptides]
	return sorted(Cyclospectrum)


def Mass(peptide):
	mass = 0
	for acid in peptide:
		mass += weights[acid]
	return mass


def expand(peptides):
	expanded_peptides = []
	for peptide in peptides:
 		for acid in weights:
 			expanded_peptides.append(peptide + acid)
	return expanded_peptides

        
def sequence_cyclopeptide(Spectrum):
	new_peptides = [""]
	cyclopeptide = []
	ParentMass = max(Spectrum)
	while True:        
		peptides = expand(new_peptides)
		new_peptides = []
		for peptide in peptides:
			if Mass(peptide) == ParentMass:
				if Cyclospectrum(peptide) == Spectrum:
					cyclopeptide.append(peptide)
			if peptide_is_consistent(peptide, Spectrum):
				new_peptides.append(peptide)
		if not new_peptides:
			break
	return cyclopeptide
                

def main():

	with open('/home/masha/Загрузки/rosalind_ba4e.txt', 'r') as f: 
		Spectrum = [int(elem) for elem in f.readline().split()]

	cyclopeptide = sequence_cyclopeptide(sorted(Spectrum))

	result = set()
	for peptide in cyclopeptide:
		formatted = "-".join(str(weights[acid]) for acid in peptide)
		result.add(formatted)
	result = list(result)
	output = " ".join(result)

	with open('/home/masha/Загрузки/output.txt', 'w') as f: 
    		f.write(output)

if __name__ == "__main__":
		main()

