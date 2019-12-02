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

	def __repr__(self):
		return self.data + " " + str(self.degree()) + \
			" In:" + str(self.indegree()) + \
			" Out:" + str(self.outdegree())

    
	def degree(self):
		return len(self.prev) + len(self.next)

    
	def indegree(self):
		return len(self.prev)

    
	def outdegree(self):
		return len(self.next)
    
    
def createGraph(patterns, k):

	graph = []

	for pattern in patterns:
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

            
	return graph
            
    
def createEulerPath(graph, k):

	EulerPath = []

	while (True):
		for node in graph:
			if node.degree() > 0:
				new_start_node = node
				break
			else:
				new_start_node = None
				break

		if (new_start_node is None):
			break
        
		if (EulerPath):
 			path = generatePath(graph, new_start_node)
		else:
			for node in graph:
				if node.outdegree() == node.indegree() + 1:
					new_start_node = node
			path = generatePath(graph, new_start_node)

		EulerPath = insertPath(path, EulerPath)
        
	return concatenatePath(EulerPath)


def insertPath(path, EulerPath):

	if (not EulerPath):
		return path

	for counter in range(len(EulerPath)):

		if (EulerPath[counter].data == path[0].data):
			EulerPath.pop(counter)
			EulerPath[counter:counter] = path
			return EulerPath
    
    
def generatePath(graph, start_node):

	current_node = start_node
	path = []
	path.append(current_node)

	while (current_node.outdegree() != 0):
		next_node = current_node.next.pop(0)
		next_node.prev.remove(current_node)
		current_node = next_node
		path.append(current_node)

	return path

        
def concatenatePath(EulerPath):
	result = EulerPath[0].data[:-1]
    
	for node in EulerPath:
		result += node.data[-1]
	return result 


def getBinaries(k):

	current = [""]
	new = []

	for _ in range(k):

		for val in current:
			new.append(val + "0")
			new.append(val + "1")

		current = new
		new = []

	return current

def main():

	with open('/home/masha/Загрузки/test.txt', 'r') as f: 
   		 k = int(f.readline())

	graph = createGraph(getBinaries(k), k)
	print(graph)
	path = createEulerPath(graph, k)
	with open('//home/masha/Загрузки/output.txt', 'w') as f: 
    		f.write(path)
	
if __name__ == "__main__":
	main()



