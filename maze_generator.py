
import sys
import random


class MazeGenerator:

    def __init__(self, width: int, height: int, entry_x: int, entry_y: int,
                 exit_x: int, exit_y: int, output_file: str, perfect: bool
                 ) -> None:
        self.width = width
        self.height = height
        self.entry_x = entry_x
        self.entry_y = entry_y
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.output_file = output_file
        self.perfect = perfect

    def select_random_direction(self, x: int, y: int) -> int:
        if y == 0:
            direction = {"east": 2, "south": 4, "west": 8}
        elif x == 0:
            direction = {"north": 1, "east": 2, "south": 4}
        elif y == self.height:
            direction = {"north": 1, "east": 2, "west": 8}
        elif x == self.width:
            direction = {"north": 1, "south": 4, "west": 8}
        else:
            direction = {"north": 1, "east": 2, "south": 4, "west": 8}
        return random.choice(list(direction.values()))

    def create_full_maze(self, width, height) -> list[list[str]]:
        full_maze: list[list[str]] = []
        for _ in range(height):
            full_maze.append([])
        for i in range(height):
            for _ in range(width):
                full_maze[i].append("15")
        return full_maze

    def dfs_maze_generator(self) -> list[list[str]]:
        pos_x = self.entry_x
        pos_y = self.entry_y
        visited_list: list[tuple] = []
        maze = self.create_full_maze(self.width, self.height)
        while (len(visited_list) < self.width*self.height):
            direction = self.select_random_direction(pos_x, pos_y)
            if ((pos_x, pos_y) not in visited_list or len(visited_list) == 1):
                new_value = int(maze[pos_x][pos_y]) - direction
                maze[pos_x][pos_y] = f"{new_value}"
            visited_list.append((pos_x, pos_y))
            if direction == 1 and pos_y != 0:
                pos_y -= 1
            if direction == 2 and pos_x != self.width:
                pos_x += 1
            if direction == 4 and pos_y != self.height:
                pos_y += 1
            if direction == 8 and pos_x != 0:
                pos_x -= 1

        return maze

    def maze_nameofalgosolver_solver(self) -> None:
        pass

    def create_output_file(self, file_name) -> None:
        pass


maze = MazeGenerator(3, 3, 0, 0, 2, 2, "salut", True)
print(maze.dfs_maze_generator())
