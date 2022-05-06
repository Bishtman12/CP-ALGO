#RECURSIVE DFS##
def dfs_helper(self, v, color, parent, time, ans):
    color[v] = 'G'  # when it is visited once then grey
    time[v][0] = self.Time
    ans.append(v)
    for node in self.list[v]:
        if color[node] == 'W':
            parent[node] = v
            self.dfs_helper(node, color, parent, time, ans)
    color[v] = "B"
    time[v][1] = self.Time
    self.Time += 1


def DFS(self, start):
    ans = []
    color = {}
    parent = {}
    time = {}
    for nodes in self.list:
        color[nodes] = 'W'
        parent[nodes] = None
        time[nodes] = [1, -1]
    self.dfs_helper(start, color, parent, time, ans)
    return ans

##ITERATIVE DFS##
def dfs_stacks(self, start):
    ans = []
    visited = {}
    for nodes in self.list:
        visited[nodes] = False
    temp = [start]
    visited[start] = True
    while len(temp) > 0:
        u = temp.pop()  # popping the top most element of the stack
        ans.append(u)  # getting it in the ans
        for j in self.list[u]:  # for neighbours of the popped element
            if visited[j] == False:  # if not visited then append them in j
                temp.append(j)
                visited[j] = True
            else:
                continue
    return ans
