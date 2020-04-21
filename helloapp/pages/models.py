from django.db import models

# Create your models here.
import numpy as np
import matplotlib.pyplot as plt


class Game() :

    def __init__(self, dim, start, goal, action_cost):
        self.dim = dim # TODO: add check if start and goal values make sense wrt to dim
        self.start = start
        self.goal = goal
        self.action_cost = action_cost
        self.goal_reward = self.get_manhattan_dist(self.start, self.goal)

    def calculate_value_function(self):
        val_func = np.zeros((self.dim, self.dim))
        visited = np.zeros((self.dim, self.dim))
        priority_queue = []

        # put goal into the queue
        priority_queue.append(self.goal)
        goal_x, goal_y = self.goal
        visited[goal_x][goal_y] = 1
        val_func[goal_x][goal_y] = self.goal_reward

        while len(priority_queue) > 0:
            current_x, current_y = priority_queue.pop(0)
            neighbors = self.get_neighbors(current_x, current_y)
            for neighbor in neighbors:
                neighbor_x, neighbor_y = neighbor
                if visited[neighbor_x][neighbor_y] == 0:
                    val_func[neighbor_x][neighbor_y] = val_func[current_x][current_y] + self.action_cost
                    visited[neighbor_x][neighbor_y] = 1
                    priority_queue.append(neighbor)
                    for i in range(self.dim):
                        print(val_func[i])
                    print(priority_queue)
        return val_func

    def get_neighbors(self, x, y):
        possible_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        neighbors = filter(lambda f: self.is_valid_field(f), possible_neighbors)
        return neighbors

    def is_valid_field(self, location):
        x, y = location
        if x < 0 or y < 0:
            return False
        if x >= self.dim or y >= self.dim:
            return False
        return True

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