codons = {
	"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
	"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
	"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
	"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
	"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
	"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
	"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
	"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
	"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
	"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
	"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
	"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
	"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
	"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
	"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
	"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def transcription(dna):
	rna_nucleotids = {"A":"A", "T":"U", "G":"G", "C":"C"}
	rna = ""
	for nucleotid in dna:
		rna += rna_nucleotids[nucleotid]
	return rna

def antitranscription(rna_substring):
	anti_rna_nucleotids = {"A":"A", "U":"T", "G":"G", "C":"C"}
	dna_substring = ""
	for nucleotid in rna_substring:
		dna_substring += anti_rna_nucleotids[nucleotid]
	return dna_substring



def get_reverse_complement(dna):
	reverse_complement = ""
	nucleotids = {"A":"T", "T":"A", "G":"C", "C":"G"}
	for nucleotid in dna[::-1]:
		reverse_complement += nucleotids[nucleotid]
	return reverse_complement


def translation(substring):
	peptide = ""
	for i in range(0, len(substring), 3):
		codon = substring[i : (i + 3)]
		peptide += codons[codon]
	return peptide


def get_substrings(rna, peptide):
	substrings = []
	n = len(peptide)
	for i in range(len(rna) - 3 * n + 1):
		substring = rna[i : (i + 3 * n)]
		if translation(substring) == peptide:
			substrings.append(substring)
	return substrings 
    


def main():    

	with open('/home/masha/Загрузки/rosalind_ba4b.txt', 'r') as f: 
		info = f.read().splitlines()
		dna = info[0]
		peptide = info[1]
	
	rna = transcription(dna)
	rna_substrings = get_substrings(rna, peptide)
	dna_substrings = []
	for rna_substring in rna_substrings:
		dna_substrings.append(antitranscription(rna_substring))

	reverse_complement = transcription(get_reverse_complement(dna))
	substrings_from_reverse_complement = get_substrings(reverse_complement, peptide)

	for substring in substrings_from_reverse_complement:
   		dna_substrings.append(get_reverse_complement(antitranscription(substring)))
	output = "\n".join(dna_substrings)


	with open('/home/masha/Загрузки/output.txt', 'w') as f: 
    		f.write(output)

if __name__ == "__main__":
	main()

