class GraphNode:

	def __init__(self, data, next=None, prev=None):

		self.data = data
		self.visited = False
		if (next):
			self.next = next
		else:
			self.next = []

		if (prev):
			self.prev = prev
		else:
			self.prev = []

		self.simple = False

    
	def degree(self):
		return len(self.prev) + len(self.next)

    
	def indegree(self):
		return len(self.prev)

    
	def outdegree(self):
		return len(self.next)

            
        
def createGraph(Text, k):

	graph = []

	for pattern in Text:
		start_data = pattern[:k - 1]
		finish_data = pattern[1:]

		start = None
		finish = None

		for node in graph:
			if node.data == start_data:
				start = node
			if node.data == finish_data:
				finish = node
                
		if (finish is None):
			finish = GraphNode(finish_data)
			graph.append(finish)

		if (finish_data == start_data):
			start = finish
                
		if (start is None):
			start = GraphNode(start_data)
			graph.append(start)
            
		start.next.append(finish)
		finish.prev.append(start)

	defineSimple(graph)
	return graph


def defineSimple(graph):

	for node in graph:
		if (node.indegree() == 1 and node.outdegree() == 1):
			node.simple = True
		else:
			node.simple = False


def getStart(graph):
	for node in graph:
		if (node.outdegree() == node.indegree() + 1):
			return node
	for node in graph:
		if (not node.simple and node.outdegree()):
    			return node
            
         
        
def getContig(graph, start_node):

	contig = []
	current_node = start_node
	contig.append(current_node)

	while (True):
		next_node = current_node.next.pop(0)
		next_node.prev.remove(current_node)
		current_node = next_node
		contig.append(current_node)
		if ((current_node.outdegree() != 1) or (current_node.indegree() != 0) or (current_node.simple == False)):
			break
	return contig



def getContigs(graph):

	contigs = []
	while (True):

		start_node = getStart(graph)

		if start_node is None:
			break
		else:
			contig = getContig(graph, start_node)
			contigs.append(concatenateContig(contig))
	return contigs



def concatenateContig(contig):

    concatenated_contig = contig[0].data[:-1]
    
    for node in contig:
        concatenated_contig += node.data[-1]

    return concatenated_contig 
    

        
def main():

	with open('/home/masha/Загрузки/rosalind_ba3k.txt', 'r') as f: 
    		Text = [elem.strip() for elem in f.readlines()] 

	k = len(Text[0])
	graph = createGraph(Text, k)
	contigs = getContigs(graph)
	output = " ".join(contigs)

	with open('/home/masha/Загрузки/output.txt', 'w') as f: 
        	f.write(output)

if __name__ == "__main__":
	main()

