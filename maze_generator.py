
import sys


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

    def create_full_maze(self, width, height) -> list[list[str]]:
        full_maze: list[list[str]] = []
        for _ in range(height):
            full_maze.append([])
        for i in range(height):
            for _ in range(width):
                full_maze[i].append("F")
        return full_maze

    def dfs_maze_generator(self) -> list[list[str]]:
        maze = self.create_full_maze(self.width, self.height)
        return maze

    def maze_nameofalgosolver_solver(self) -> None:
        pass

    def create_output_file(self, file_name) -> None:
        pass


maze = MazeGenerator(5, 2, 1, 2, 2, 2, "salut", True)
print(maze.dfs_maze_generator())
