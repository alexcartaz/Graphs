from graph import Graph
from random import randint
import math
import functools

'''
def genListOfRandNumsWithExpAvg(n, expected_avg):
    a = 0 #local min
    b = math.floor(n/2) #local max
    while True:
        l = [randint(a, b) for i in range(n)]
        avg = functools.reduce(lambda x, y: x + y, l) / len(l)
        if avg == expected_avg:
            return l

def genSpecificFriendships(numFriendsList, numUsers):
    friendshipList = []
    userId = 0
    for numFriends in numFriendsList:
        userId+=1
        friendIds = []
        while len(friendIds) < numFriends:
            ranFriendId = randint(1,numUsers)
            if ranFriendId not in friendIds and ranFriendId != userId:
                friendIds.append(ranFriendId)
        friendshipList.append(friendIds)
    return friendshipList
'''


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        self.graph = Graph()

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        elif friendID in self.users and userID in self.users:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            self.graph.add_edge(str(friendID),str(userID))
            return True
        else:
            print("Error: one or both users don't exist")
            return False

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()
        self.graph.add_vertex(str(self.lastID))

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.

        >>> sg = SocialGraph()
        >>> sg.populateGraph(10, 2)  # Creates 10 users with an average of 2 friends each
        >>> print(sg.friendships)
        {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        f = open('names.txt', 'r')
        names = f.read().split("\n")  # List containing 10000 names
        f.close()
        # Add users
        for userId in range(1,numUsers+1):
            self.addUser(names[userId])

        # Create friendships
        totalFriendships = numUsers * avgFriendships
        while(totalFriendships > 0):
            userId = randint(1,numUsers)
            friendId = randint(1,numUsers)
            if self.addFriendship(userId,friendId):
                totalFriendships-=2

        

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        u = str(userID)
        allConnections = self.graph.bft(u)
        for c in allConnections:
            if c != u and c not in self.graph.vertices[u]:
                visited[c] = self.graph.bfs_path(u,c)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print('*')
    print(connections)
