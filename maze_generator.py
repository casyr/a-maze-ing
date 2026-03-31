
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
        direction = {"north": 1, "east": 2, "south": 4, "west": 8}
        if x == 0:
            direction.pop("west")
        if x == self.width - 1:
            direction.pop("east")
        if y == 0:
            direction.pop("north")
        if y == self.height - 1:
            direction.pop("south")
        return random.choice(list(direction.values()))

    def create_full_maze(self, width, height) -> list[list[str]]:
        full_maze: list[list[str]] = []
        for _ in range(height):
            full_maze.append([])
        for i in range(height):
            for _ in range(width):
                full_maze[i].append("15")
        return full_maze

    @staticmethod
    def break_common_wall(direction: int) -> int:
        if direction == 1:
            return 4
        if direction == 2:
            return 8
        if direction == 4:
            return 1
        if direction == 8:
            return 2
        return 0

    def dfs_maze_generator(self) -> list[list[str]]:
        pos_x = self.entry_x
        pos_y = self.entry_y
        visited_list: list[tuple] = []
        maze = self.create_full_maze(self.width, self.height)
        visited_list.append((pos_x, pos_y))

        return maze

    def maze_nameofalgosolver_solver(self) -> None:
        pass

    def create_output_file(self, file_name) -> None:
        pass


maze = MazeGenerator(3, 3, 0, 0, 2, 2, "salut", True)
print(maze.dfs_maze_generator())
