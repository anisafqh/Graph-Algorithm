# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:39:00 2021

@author: User
"""
#HEADER
#class to represent a graph object
import random
import matplotlib.pyplot as plt
import networkx
class Graph:
    def __init__(self,edges,n): #constructor
        #no of vertices of graph
        self.vtx = n
        self.adj = {}
        self.weights={}
        
        #allocate memory for adjacency list
        for edge in edges:
            self.adj[edge] = []
        
    def add_edge(self,source,to,weight): #add edge function
        self.adj[source].append(to) #key for element
        self.weights[(source,to)] = weight #key for element
    
    #Function Delete Edges
    def delete_edge(self,source,dest):
       f=False
       if not len(self.adj[source]):
           print("There is no other vertices connected to it.")
           
       else:
          for m in self.adj[source]:
               if dest == m: #if destination vertex is same to m
                   f = True
          if f == False: #if the vertex destination not adjacent to vertex source
              print("Vertex", dest,"is not adjacent to vertex ", source)
              return False
          else: #if path found, then remove
              self.adj[source].remove(dest) #remove edge between 2 vertex
              Temp=(source,dest) #assign the source and destination to temp
              self.weights.pop(Temp) #pop weight of edge between 2 vertex
              print("\nUpdated graph is :\n")
              return True
    
    # Function reset
    def reset(self):
        for source,to,weight in edges: 
            # delete all edges
            self.adj[source].remove(to)
            temp = (source,to)
            self.weights.pop(temp)
            
    
    #Function DFS for strongly connected graph
    def dfs(self, u, visited, stack, temp):
        visited[u] = "G"
        for v in temp[u]:
            if visited[v] == "W":
                cycle = self.dfs(v, visited, stack, temp)
                if cycle == True:
                    return True
            elif visited[v]=="G":
                return True
        visited[u]="B"
        return False
         
    # The main function that returns true if graph is strongly connected
    def check_SC(self):
        temp = self.adj
        visited = {}
        stack = {}
        
        # do for every vertex
        for u in temp.keys():
            visited[u]="W"
            stack[u]=None
            
        # start DFS from the first vertex
        for u in temp.keys():
            if visited[u] == "W":
                cycle = self.dfs(u, visited, stack, temp)#a dummy variable
         
        # If DFS traversal doesn't visit all vertices,
        # then the graph is not strongly connected
        for b in visited.keys():
            if visited[b] != 'G':
                return False
        return True        
    
    
    def cycledetection(self): #function for cycle detection
        temp = self.adj.keys() #ada semua key yang ada kat dalam dict
        visited = {} #array for visited
        track = {} #null #array for track 
        for n in temp: #for node in temp which is in dict 
            visited[n] = False #initialize all node with visited array False
            track[n] =  False #initialize all node with track array False
           
        for n in temp: #for node in temp which is in dict
            go = self.DFS(n,visited,track) #go for DFS function
            if go == True: #if DFS function return true
                return True #then return true because cycle has been detected
        return False #otherwise
    
    def DFS(self,n, visited, track):#DFS function
        visited[n] = True #assign true to visited array that already visited
        track[n] = True #assign true for array track also
        #neigh has nodes
        neigh = self.adj[n] #neighbours of two nodes(adjacency of 2 nodes)
        for m in range(len(neigh)): #length of nodes
            current = neigh[m] # assign particular node to current
            if track[current] == True: #if in array track at current node
                return True #return value
            if visited[current] == False: #if in array visited at current node false 
                #which not visited yet then do recursive
                go = self.DFS(current,visited,track) #repeat
                if go == True: #if already visited
                    return True #return
        track[n]=False #if not in if statement then 
        #backtrack,change back particular node to false in the array track
        return False #then
    
    # Function shortest_path
    # This function use Dijkstra's algorithm to find the shortest 
    #path between two vertices
    def shortest_path(self, first, last):
    
        # shortest paths is a dict of vertices
        # whose value is a tuple of (previous vertex, weight)  
        shortest_paths = {first: (None, 0)}
        current_vertex = first
        visit = set()
        
        while current_vertex != last:
            visit.add(current_vertex)
            destination = self.adj[current_vertex] 
            new_weight = shortest_paths[current_vertex][1]
            
            # calculate adjacent vertex weight 
            for adj_vertex in destination:
                weight = self.weights[(current_vertex, adj_vertex)] + new_weight
                
                if adj_vertex not in shortest_paths:
                    shortest_paths[adj_vertex] = (current_vertex, weight)
                else:
                    current_weight = shortest_paths[adj_vertex][1]
                    
                    # compare the weight of the current shortest vertex 
                    if current_weight > weight:
                        shortest_paths[adj_vertex] = (current_vertex, weight)
                        
            new_destinations = {vertex: shortest_paths[vertex] for vertex in shortest_paths if vertex not in visit}
            if not new_destinations:
                return "Path not found" # when the destination vertex not in the graph
                
            # next vertex is the destination with the smallest weight
            current_vertex = min(new_destinations, key=lambda k: new_destinations[k][1])
            
        # Work back through destinations in shortest path
        final_path = [] 
            
        while current_vertex is not None:
            final_path.append(current_vertex)
            adj_vertex = shortest_paths[current_vertex][0]
            current_vertex = adj_vertex     
                
        # reverse path
        final_path = final_path[::-1]
        return final_path
    
    #Function generate random edges 
    def random_edges(self,edges):
        loop = True
        while loop:
            exist = False
            ran_edges = random.choice(edges)
            for i in self.adj:
                for j in self.adj[i]:
                    if ran_edges[0] == i and ran_edges[1] == j:
                       exist = True
                       
            if exist == False:
               loop = False
        self.add_edge(ran_edges[0],ran_edges[1],ran_edges[2])
            
#Function to print adjacency list representation of graph
def graph_print(graph):
    print("\n\nAdjacency List:\n")
    print(graph.adj) #tak masuk dalam class graph
    print("\nAdjacency list with weighted at edge:\n")
    print(graph.weights)

def menu_list():
    print("\n\n********************************************************************************")
    print("Welcome to Graph System!")
    print("\n\n1 - Add edge into graph ")
    print("\n2 - Remove edge in graph ")
    print("\n3 - Strong conectivity in graph ")
    print("\n4 - Cycle detection in graph ")
    print("\n5 - Shortest path in graph ")
    print("\n6 - Reset graph ")
    print("\n**********************************************************************************")
    
if __name__ == '__main__':
 
    
    edges = [("Tokyo", "HochiMinh", 4329), 
             ("HochiMinh", "Los Angeles", 13135), 
             ("Los Angeles","Asmara", 14015), 
             ("Prague", "Asmara",4450),
             ("Tokyo", "Prague", 9073), 
             ("Asmara", "Tokyo", 9961), 
             ("Los Angeles", "Tokyo", 8811)]
    
    all_edges = [("Tokyo", "HochiMinh", 4329),
                 ("Tokyo","Los Angeles",8811),
                 ("Tokyo","Asmara",9961),
                 ("Tokyo","Prague",9073),
                 ("HochiMinh", "Tokyo",4329),
                 ("HochiMinh", "Los Angeles", 13135),
                 ("HochiMinh", "Asmara",7330),
                 ("HochiMinh", "Prague",9251),
                 ("Los Angeles", "Tokyo", 8811),
                 ("Los Angeles", "HochiMinh",13135),
                 ("Los Angeles","Asmara", 14015),
                 ("Los Angeles","Prague",9566),
                 ("Asmara", "Tokyo", 9961),
                 ("Asmara", "HochiMinh",7330),
                 ("Asmara", "Los Angeles",14015),
                 ("Asmara", "Prague",4450),
                 ("Prague","Tokyo",9073),
                 ("Prague","HochiMinh",9251),
                 ("Prague","Los Angeles",9566),
                 ("Prague", "Asmara",4450)]
    
    city = ["Tokyo","HochiMinh","Los Angeles", "Asmara", "Prague"]
  
    # Input: No of vertices
    N = 5
    # construct a graph from a given list of edges
    graph = Graph(city, N)
   
    for source,to,weights in edges:
        graph.add_edge(source,to,weights)
    
    # print adjacency list representation of the graph
    print("\nDefault Graph:")
    graph_print(graph)
    
    menu_list()
    
    loop=True
    
    while loop:
        c = input("Please Enter your choice [1-6 only]: ")
        
        if c == "1":
            loop1=True
            print("Add edge into graph")
            while loop1:
                v1=input("Enter city to be source: ")
                v2=input("Enter city to be destination(New city): ")
                v3=input("Enter the distance between sourde and destination: ")
                
                graph.add_edge(v1,v2,v3)
                
                k = input("\nDo you want to continue adding the edge? [1-Yes,Otherwise-No]:")
                if k == "1":
                    loop1=True
                else:
                    loop1=False
                    
            print("Updated graph: ")
            graph_print(graph)
                
            l = input("\nDo you wish to return back to the menu?[1-Yes,Otherwise-No]:")
            if l == "1":
                menu_list()
                loop=True
            else:
                loop=False
        
        elif  c == "2":
            #*************************************************************#
            #Funtion Remove Edge in Main
            loop1=True
            print("Remove edge in graph")
            while loop1:
                v1 =input("Enter city to be source: ")
                v2=input("Enter city to be destination: ")
                
                if graph.delete_edge(v1,v2) == True:
                    graph_print(graph)
                else:
                    print("Thus the deletion of edges is invalid. Please try again.")
                
                k = input("\nDo you want to continue deleting the edge? [1-Yes,Otherwise-No]:")
                if k == "1":
                    loop1=True
                else:
                    loop1=False
            l = input("\nDo you wish to return back to the menu?[1-Yes,Otherwise-No]:")
            if l=="1":
                menu_list()
                loop=True
            else:
                loop=False
            
        elif c == "3":
            loop1=True
            while loop1:
                print("\n****This is Strong connectivity Part****")
                if graph.check_SC()==True:
                    print("\nThe graph is strongly connected.")
                else:
                    print("\nThe graph is not strongly connected.")
                    while graph.check_SC()==False:
                        graph.random_edges(all_edges)
                        if graph.check_SC() == True:
                            print("\nRandom edges between random city is generated.")
                            graph_print(graph)
                            print("\nThe graph is strongly connected.")
                            break
                        
                k = input("\nDo you want to continue the strong connectivity? [1-Yes,Otherwise-No]:")
                if k == "1":
                    loop1=True
                else:
                    loop1=False
                    
            l = input("\nDo you wish to return back to the menu?[1-Yes,Otherwise-No]:")
            if l == "1":
                menu_list()
                loop=True
            else:
                loop=False
            
        elif c == "4":
            #*************************************************************#
            #FUNTION 2
            #Display the cycle detection in the graph
            loop1=True
            while loop1:
                print("\n**** This is Cycle Detection Part****")
                if graph.cycledetection() == True:
                    print("The graph has cycle")
                else:
                    print("The graph has no cycle")
                    print("Random edges generator will be called....")
                    while graph.cycledetection()==False:
                        graph.random_edges(all_edges)
                        if graph.cycledetection() == True:
                            print("The graph finally has cycle.")
                            break
                
                k = input("\nDo you want to continue the cycle detection? [1-Yes,Otherwise-No]:")
                if k == "1":
                    loop1=True
                else:
                    loop1=False
                    
            l = input("\nDo you wish to return back to the menu?[1-Yes, Otherwise-No]:")
            if l == "1":
                menu_list()
                loop=True
            else:
                loop=False
            
        elif c == "5":
             #*******************************************************#
             # FUNCTION 3
             # Allow user to select two vertices and compute the shortest path
             # Print the shortest path and add random edges if there is no path
             # between the chosen vertices
             print("\tFunction 3: Shortest Path\t")
             print("\tPlease choose two cities!\t")
             loop1=True
             while True:
                 # input two vertices from user
                 v1 = input("Enter city 1: ")
                 v2 = input("Enter city 2: ")
                 print("\n City 1 is {} \n City 2 is {} \n".format(v1, v2))
                
                 if graph.shortest_path(v1, v2) == True:
                    print("The shortest path from ", v1, " to ", v2, " is ", graph.shortest_path(v1, v2))
                 else:
                    graph.random_edges(all_edges) # random generate path
                    print("The shortest path from ", v1, " to ", v2, " is ", graph.shortest_path(v1, v2))
                
                 k = input("\nDo you want to continue searching shortest path? [1-Yes,Otherwise-No]:")
                 if k == "1":
                    loop1=True
                 else:
                    #loop1=False
                     break
                    
             l = input("\nDo you wish to return back to the menu?[1-Yes,Otherwise-No]:")
             if l == "1":
                menu_list()
                loop=True
             else:
                loop=False
        
        elif c == "6":
            #*******************************************************#
            # RESET FUNCTION
            # reset graph
            print(".....Reset the graph..... \n")
            graph.reset()
            
            graph_print(graph)
            print("\n")
    
            # after reset, add back edges to default graph
            for source,to,weights in edges:
                graph.add_edge(source,to,weights)
    
            #print default graph
            print("The graph after reset (default graph): \n")
            graph_print(graph)
            k = input("\nAre you wish to return back to the menu?[1-Yes,Otherwise-No]:")
            if k == "1":
                menu_list()
                loop=True
            else:
                loop=False
                
        else:
            print("Invalid input")
            print("Please Enter Again")
            k = input("\nAre you wish to return back to the menu?[1-Yes,Otherwise-No]:")
            if k == "1":
                menu_list()
                loop=True
            else:
                loop=False