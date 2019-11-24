import numpy as np
import time
import argparse
import sys

"""
Below is code for the PageRank algorithm (power iteration),

This code assumes that the node IDs start from 0 and are contiguous up to max_node_id.
You will have to implement the functionality in the space provided. 

This code assumes that the node IDs start from 0 and are contiguous up to max_node_id.
You will have to implement the functionality in the space provided. 
You are asked to implement pagerank algorithm using power iteration method iterating 
over probabilities multiple times because Computing the adjacency matrix for large graph 
requires to load large graph dataset to computer memory. In order to calculate the probabilities 
of each node, we will iterate over dataset multiple times and update the probabilities based on 
equation mentioned in the question.
"""
def author():                                                                                             
        return 'skannan65' # replace sroutray3 with your Georgia Tech username.                                                                                             
                                                                                              
def gtid():                                                                                               
    return 903444166 # replace with your GT ID number      

class PageRank:
    def __init__(self, edge_file):

        self.node_degree = {}
        self.in_degree   = {} #DEA Graph: In-degree represents incoming drug flow. It matters in Page-rank so we can account for self-consumption
        self.max_node_id = 0
        self.edge_file   = edge_file

    def read_edge_file(self, edge_file, header=True):
        headerSeen = False
        with open(edge_file) as f:
            for line in f:
                if headerSeen == False and header==True:
                    headerSeen = True
                    continue
                if line[0] != '%':
                    val = line.split(',') #DEA Graph: Its comma separated and not tab separated
                    val = val[0].strip(), val[1].strip(), val[2].strip() #DEA Graph: Strip off whitespace like newlines...(Ah! Athena..)
                    yield int(val[0][1:-1]), int(val[1][1:-1]), int(val[2][1:-1]) # DEA Graph: Added third one for weight, Added 1 to -1 for handling double quotes

    def get_max_node_id(self):
        return self.max_node_id
    '''
    Step1: Calculate the out-degree of each node and maximum node_id of the graph.
    Store the out-degree in class variable "node_degree" and maximum node id to "max_node_id".
    '''
    def calculate_node_degree(self):
        for source,target,weight in self.read_edge_file(self.edge_file): #DEA Graph: Weight Support
            source = source - 1 #DEA Graph: Weight support. DEA Graph starts with 1. Hence the fix.
            target = target - 1 #DEA Graph: Weight support. DEA Graph starts with 1. Hence the fix.
            #print("{} {} {}".format(source, target, weight))
### Implement your code here
#############################################
            ## Update out-degree
            if source in self.node_degree.keys():
                self.node_degree[source] += weight #DEA Graph: Weight support
            else:
                self.node_degree[source] = weight #DEA Graph: Weight support
            if target not in self.node_degree.keys():
                self.node_degree[target] = 0

            ## Update in-degree. Needed for DEA Graph
            if target in self.in_degree.keys():
                self.in_degree[target] += weight #DEA Graph: Weight support
            else:
                self.in_degree[target] = weight #DEA Graph: Weight support
            if source not in self.in_degree.keys():
                self.in_degree[source] = 0
            
            ## Update max node-ids
            if source > self.max_node_id:
                self.max_node_id = source
            if target > self.max_node_id:
                self.max_node_id = target
        #for k in range(self.max_node_id+1):
            #if k not in self.node_degree.keys():
                #self.node_degree[k] = 0
#############################################

        print("Calculated node degrees ")
        print("Max node id : {} with weighted-degree {}".format(self.max_node_id, self.node_degree[self.max_node_id]))


    def run_pagerank(self, node_weights,  damping_factor=0.85, iterations=10):

        scores = [1.0 / (self.max_node_id + 1)] * (self.max_node_id + 1)
        start_time = time.time()
        ''' 
        Step2: Implement pagerank algorithm as mentioned in lecture slides and the question.

        Incoming Parameters:
            node_weights: Probability of each node to flyout during random walk
            damping_factor: Probability of continuing on the random walk
            iterations: Number of iterations to run the algorithm 
        
        Use the calculated out-degree to calculate the score of each node
        '''
        for it in range(iterations):
            
            new_scores = [0.0] * (self.max_node_id + 1)
            for source, target, weight in self.read_edge_file(self.edge_file):#DEA Graph: Weight Support
                source = source - 1 #DEA Graph: Fix for 1-based node-ids
                target = target - 1 #DEA Graph: Fix for 1-based node-ids
### Implement your code here
#############################################
                #print(self.node_degree.keys())
                degreeFactor = max(self.in_degree[source] , self.node_degree[source])
                if degreeFactor != 0:
                    degreeFactor = 1./degreeFactor
                if self.node_degree[source] != 0:
                    ptarget = (damping_factor)*scores[source]*(weight*degreeFactor) #DEA Graph: Weight Support
                else:
                    ptarget = 0
                new_scores[target] = new_scores[target] + ptarget
            for nodeid in range(self.max_node_id + 1):
                new_scores[nodeid] += (1-damping_factor)*node_weights[nodeid]
            scores = new_scores
#############################################

        
        print ("Completed {0}/{1} iterations. {2} seconds elapsed." \
            .format(it + 1, iterations, time.time() - start_time))

        return scores

def dump_results(command, iterations, result):
    print("Sorting...", file=sys.stderr)
    sorted_result = sorted(enumerate(result), key=lambda x: x[1], reverse=True)
    output_result = "node_id\tscore"
    for node_id, score in sorted_result[:10]:
        output_result += "\n{}\t{}".format(node_id, score)
    print(output_result)

    with open(command+str(args.iterations)+".txt","w") as output_file:
        output_file.write(output_result)

def dump_results_dea(command, iterations, result):
    print("Sorting...", file=sys.stderr)
    sorted_result = sorted(enumerate(result), key=lambda x: x[1], reverse=True)
    rank = 1
    with open(command+str(args.iterations)+".csv","w") as output_file:
        header = "node_id,pr_score,page_rank"
        output_file.write(header)
        for node_id, score in sorted_result:
            this_result = "\n{},{},{}".format(node_id+1, score, rank)#DEA Graph: Fix for node-id. Adding 1 while dumping
            rank += 1
            output_file.write(this_result)
    print("Results persisted in " + command + str(args.iterations) + ".csv")

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='sample command:  python pagerank.py -i 5 -d 0.85 simplified_pagerank soc-wiki-elec.edges')
    parser.add_argument("command", help="Sub-command to execute. Can be  simplified_pagerank or personalized_pagerank.")
    parser.add_argument("filepath", help="path of the input graph file(soc-wiki-elec.edges)")

    parser.add_argument("-i", "--iterations", dest="iterations",
                        help="specify the number of iterations to  the algorithm. Default: 10",
                        default=10, type=int)

    parser.add_argument("-d", "--damping-factor", dest="damping_factor",
                        help="specify the damping factor for pagerank. Default: 0.85",
                        default=0.85, type=float)

    args = parser.parse_args()

    if args.command == 'simplified_pagerank':
        pr = PageRank(args.filepath)
        pr.calculate_node_degree()
        max_node_id = pr.get_max_node_id()
        node_weights = np.ones(max_node_id + 1) / (max_node_id + 1)
        result = pr.run_pagerank(node_weights=node_weights, iterations=args.iterations, damping_factor=args.damping_factor)
        dump_results_dea(args.command, args.iterations, result ) #DEA Graph: Using new function to dump since we are dumping everything

    elif args.command == 'personalized_pagerank':
        pr = PageRank(args.filepath)
        pr.calculate_node_degree()
        max_node_id = pr.get_max_node_id()

        np.random.seed(gtid())
        node_weights = np.random.rand(max_node_id+1)
        node_weights = node_weights/node_weights.sum()
        result = pr.run_pagerank(node_weights=node_weights, iterations=args.iterations, damping_factor=args.damping_factor)
        dump_results_dea(args.command, args.iterations, result ) #DEA Graph: Using new function to dump since we are dumping everything

    else:
        sys.exit('Incorrect command')

