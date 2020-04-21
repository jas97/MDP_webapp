import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Game() :

    def __init__(self, dim, start, goal, action_cost):
        self.dim = dim # TODO: add check if start and goal values make sense wrt to dim
        self.start = self.convert_index_to_coordinates(start)
        self.goal = self.convert_index_to_coordinates(goal)
        self.action_cost = action_cost
        self.goal_reward = self.get_manhattan_dist(self.start, self.goal)

    def calculate_value_function(self):
        val_func = np.zeros(self.dim*self.dim)
        visited = np.zeros(self.dim*self.dim)
        priority_queue = []

        # put goal into the queue
        goal_ind = self.convert_coordinates_to_index(self.goal)
        priority_queue.append(goal_ind)
        visited[goal_ind] = 1
        val_func[goal_ind] = self.goal_reward

        while len(priority_queue) > 0:
            current = priority_queue.pop(0)
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if visited[neighbor] == 0:
                    val_func[neighbor] = val_func[current] + self.action_cost
                    visited[neighbor] = 1
                    priority_queue.append(neighbor)
        return val_func

    def convert_index_to_coordinates(self, index):
        x = index % self.dim
        y = int(np.floor(index / self.dim))

        return x, y

    def convert_coordinates_to_index(self, coordinates):
        i = coordinates[0]
        j = coordinates[1]
        return j * self.dim + i

    def get_neighbors(self, field):
        possible_neighbors = [field - self.dim, field + self.dim]
        left = field - 1
        right = field + 1
        if right % self.dim != 0:
            possible_neighbors.append(right)
        if field % self.dim != 0:
            possible_neighbors.append(left)

        neighbors = filter(lambda f: self.is_valid_field(f), possible_neighbors)
        return neighbors

    def is_valid_field(self, field):
        if field >= 0 and field < self.dim * self.dim:
            return True
        else:
            return False

    def get_manhattan_dist(self, start, goal):
        x_dist = np.abs(start[0] - goal[0])
        y_dist = np.abs(start[1] - goal[1])
        manh_dist = x_dist + y_dist
        return manh_dist

    def visualize_val_function(self):
        val_func = self.calculate_value_function()

        fig, ax = plt.subplots()
        # Using matshow here just because it sets the ticks up nicely. imshow is faster.
        ax.matshow(val_func, cmap='seismic')

        for (i, j), val in np.ndenumerate(val_func):
            ax.text(j, i, '{:0.1f}'.format(val), ha='center', va='center')
        # TODO: pass data as param
        # TODO: modify colours to be lighter
        plt.show()



