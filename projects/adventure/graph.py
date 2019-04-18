"""
Simple graph implementation
"""

class Graph:
  """Represent a graph as a dictionary of vertices mapping labels to edges."""
  def __init__(self):#, adjacent_rooms, x, y, number):
    self.vertices = {}
    self.rooms = {}
    self.coordinates = {}
  def add_room(self, adjacent_rooms, x, y, currentRoomNumber):
    for direction in adjacent_rooms:
      targetRoomNumber = adjacent_rooms[direction]
      if currentRoomNumber not in self.rooms:
        self.rooms[currentRoomNumber] = {}
      self.rooms[currentRoomNumber][direction] = targetRoomNumber
      if currentRoomNumber not in self.vertices:
        self.vertices[currentRoomNumber] = set()
      self.vertices[currentRoomNumber].add(targetRoomNumber)
      #if targetRoomNumber not in self.vertices:
      #  self.vertices[targetRoomNumber] = set()
      #self.vertices[targetRoomNumber].add(currentRoomNumber)
    self.coordinates[currentRoomNumber] = [x,y]

  '''
  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
      self.vertices[v2].add(v1)
    else:
      raise IndexError("one or both vertices don't exist")
  
  def add_directed_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      raise IndexError("one or both vertices don't exist")
  '''
  ## Part 2: Implement Breadth-First Traversal
  '''
  Write a function within your Graph class that takes takes a starting node as 
  an argument, then performs BFT. Your function should print the resulting nodes
  in the order they were visited.
  '''
  def bft(self, starting_vertex_id):
    queue = []
    queue.append(starting_vertex_id)
    visited = set()
    while len(queue) > 0:
      v = queue.pop(0)
      if v not in visited:
        visited.add(v)
        for next_vert in self.vertices[v]:
          queue.append(next_vert)
    return visited


  ## Part 3: Implement Depth-First Traversal with a Stack
  '''
  Write a function within your Graph class that takes takes a starting node as an 
  argument, then performs DFT. Your function should print the resulting nodes in 
  the order they were visited.
  '''

  # I don't know how to solve this without using recursion


  ## Part 3.5: Implement Depth-First Traversal using Recursion
  '''
  Write a function within your Graph class that takes takes a starting node 
  as an argument, then performs DFT using recursion. Your function should print 
  the resulting nodes in the order they were visited.
  '''
  def dft_recurse(self, curr_vert_id, visited=None):
    if visited is None:
      visited = set()
    for v in self.vertices[curr_vert_id]:
      if v not in visited:
        visited.add(v)
        self.dft_recurse(v, visited)

    return visited


  ## Part 4: Implement Breadth-First Search
  '''
  Write a function within your Graph class that takes takes a starting
  node and a destination node as an argument, then performs BFS. Your 
  function should return the shortest path from the start node to the 
  destination node.
  '''
  
  def bfs_path(self, start_vert, target_value):
    queue = []
    queue.append(str(start_vert))
    queue_dir = []
    visited = set()
    path = []
    while len(queue) > 0:
      if len(path) == 0:
        path = [queue.pop(0)]
      else:
        path = queue.pop(0)
      v = path[len(path)-1]
      if v not in visited:
        if v == str(target_value):
          return path
        visited.add(v)
        for next_vert in self.vertices[int(v)]:
          new_path = list(path)
          new_path.append(str(next_vert))
          queue.append(new_path)
    return None



  ## Part 5: Implement Depth-First Search
  '''
  Write a function within your Graph class that takes takes a 
  starting node and a destination node as an argument, then performs DFS. 
  Your function should return a valid path (not necessarily the shortest) 
  from the start node to the destination node.
  '''

  def path_check(self, start_vert, target_value):
    for direction in self.rooms[start_vert]:
      if self.rooms[start_vert][direction] == target_value:
        return [start_vert, target_value]
    return None

  def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
    
    if visited is None:
      visited = set()
    if path is None:
      path = []
    visited.add(start_vert)
    path = path + [start_vert]
    if start_vert == target_value:
      return path
    for child_vert in self.vertices[start_vert]:
      if child_vert not in visited:
        new_path = self.dfs_r_path(child_vert, target_value, visited, path)
        if new_path:
          return new_path
    return None

  def convert_path_to_dir_path(self, path):
    if isinstance(path[0], str):
      for i in range(0,len(path)):
        path[i] = int(path[i])
    new_path = []
    c = 0
    for room in path:
      if c < len(path)-1:
        for direction in self.rooms[room]:
          if self.rooms[room][direction] == path[c+1]:
            new_path.append(direction)
            break
      c+=1
    return new_path
 

#graph = Graph()
#graph.add_vertex('1')
#graph.add_directed_edge('5', '3')
#print(graph.vertices)
#print(graph.bft('1'))
#print(graph.dft_recurse('1'))
#print('*')
#print(graph.bfs_path('1','4'))
#print(graph.dfs_r_path('1','4'))
#print(graph.bfs_path('1','7'))
