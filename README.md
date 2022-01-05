# Graph Algorithm

This project is about graph algorithms. Data structures that utilized is an adjacency list. This project programs to solve three problems, which are to check if the default graph is strongly connected, has a cycle, and compute the shortest path. The main graph functions in this project are add edge, delete edge, reset graph, random edge and print graph.

Default graph:
![image](https://user-images.githubusercontent.com/77534728/148239518-5f11a81f-c416-4d87-9fc8-cdff76e99a18.png)
Implementation of the graph using adjacency list:
{('Tokyo', 'HochiMinh'): 4329, ('HochiMinh', 'Los Angeles'): 13135, ('Los Angeles', 'Asmara'): 14015, ('Prague', 'Asmara'): 4450, ('Tokyo', 'Prague'): 9073, ('Asmara', 'Tokyo'): 9961, ('Los Angeles', 'Tokyo'): 8811

Graph Functions
1)	Add edge 
2)	Remove edge
3)	Strong connectivity in graph
4)	Cycle detection in graph
5)	Shortest path in graph
6)	Reset graph

This program allows user to choose different functions:
<img width="380" alt="image" src="https://user-images.githubusercontent.com/77534728/148240267-8ee900d6-ffe4-4e0c-a30b-10a69ec271b9.png">


Add edge function:
The program will ask source node, destination node and also destination weight for user to enter. Then, the program will display updated adjacency list of the cities with added edge.
<img width="380" alt="image" src="https://user-images.githubusercontent.com/77534728/148241255-ab666746-22d3-4eca-9d7f-a375250c379b.png">


Remove edge function:
The program will ask source node and destination node to delete. Then, the program will display updated adjacency list of current cities.
<img width="380" alt="image" src="https://user-images.githubusercontent.com/77534728/148241379-73026d75-e1f2-49e9-bd67-eb5dde121d23.png">


Strong connectivity function:
This function will determine whether the graph is strong connectivity or not.
<img width="380" alt="image" src="https://user-images.githubusercontent.com/77534728/148242264-a1a7045d-5f73-40ca-8d91-1642f2e1cd2f.png">


Cycle detection function:
This function will determine whether the graph has a cycle or not.
<img width="377" alt="image" src="https://user-images.githubusercontent.com/77534728/148242622-3465ec26-199e-449a-9fd6-175f1153be15.png">


Shortest path function:
This function allow user to select two vertices and compute the shortest path. The program will print the shortest path and add random edges if there is no path between the chosen vertices.
<img width="377" alt="image" src="https://user-images.githubusercontent.com/77534728/148242736-ea9a18ac-33ac-4ee1-a184-5bacfba61ea3.png">


