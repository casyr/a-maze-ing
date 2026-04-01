import sys
import random


class MazeGenerator:

    def __init__(
        self,
        width: int,
        height: int,
        entry_x: int,
        entry_y: int,
        exit_x: int,
        exit_y: int,
        output_file: str,
        perfect: bool,
    ) -> None:
        self.width = width
        self.height = height
        self.entry_x = entry_x
        self.entry_y = entry_y
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.output_file = output_file
        self.perfect = perfect

    def create_full_maze(self, width, height) -> list[list[int]]:
        full_maze: list[list[int]] = []
        for _ in range(height):
            full_maze.append([])
        for i in range(height):
            for _ in range(width):
                full_maze[i].append(15)
        return full_maze

    def select_random_direction(
        self, x: int, y: int, maze: list[list[int]]
    ) -> int:
        direction = {"north": 1, "east": 2, "south": 4, "west": 8}
        if x == 0 or maze[y][x - 1] != 15:
            direction.pop("west")
        if x == self.width - 1 or maze[y][x + 1] != 15:
            direction.pop("east")
        if y == 0 or maze[y - 1][x] != 15:
            direction.pop("north")
        if y == self.height - 1 or maze[y + 1][x] != 15:
            direction.pop("south")
        if direction == {}:
            return 0
        return random.choice(list(direction.values()))

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
    
    # ##
    # @staticmethod
    # def print_maze(maze):
    #     for x in maze:
    #         for y in x:
    #             print(f"{y}{"":<4}", end="")
    #         print("")
    #     print("\n")
    # ##

    def dfs_maze_generator(self) -> list[list[int]]:
        pos_x = self.entry_x
        pos_y = self.entry_y
        actual_path: list[tuple] = [(self.entry_x, self.entry_y)]
        maze = self.create_full_maze(self.width, self.height)
        while actual_path != []:
            direction = self.select_random_direction(pos_x, pos_y, maze)
            maze[pos_y][pos_x] -= direction
            if direction == 1:
                pos_y -= 1
            elif direction == 2:
                pos_x += 1
            elif direction == 4:
                pos_y += 1
            elif direction == 8:
                pos_x -= 1
            elif actual_path != []:
                actual_path.pop()
                if actual_path != []:
                    pos_x, pos_y = actual_path[-1]
                continue
            maze[pos_y][pos_x] -= self.break_common_wall(direction)
            if self.break_common_wall(direction) != 0:
                actual_path.append((pos_x, pos_y))
        return maze

    def maze_nameofalgosolver_solver(self) -> None:
        pass

    def create_output_file(self, file_name) -> None:
        pass
