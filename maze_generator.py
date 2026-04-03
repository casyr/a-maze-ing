
import random
from typing import Any


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
        mid_width = self.width // 2
        mid_height = self.height // 2
        self.forty_two_list: list[tuple] = [
            (mid_width - 3, mid_height - 2),
            (mid_width - 3, mid_height - 1),
            (mid_width - 3, mid_height),
            (mid_width - 2, mid_height),
            (mid_width - 1, mid_height),
            (mid_width - 1, mid_height + 1),
            (mid_width - 1, mid_height + 2),

            (mid_width + 1, mid_height - 2),
            (mid_width + 2, mid_height - 2),
            (mid_width + 3, mid_height - 2),
            (mid_width + 3, mid_height - 1),
            (mid_width + 3, mid_height),
            (mid_width + 2, mid_height),
            (mid_width + 1, mid_height),
            (mid_width + 1, mid_height + 1),
            (mid_width + 1, mid_height + 2),
            (mid_width + 2, mid_height + 2),
            (mid_width + 3, mid_height + 2),
        ]

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
        if (x == 0 or maze[y][x - 1] != 15
                or (x - 1, y) in self.forty_two_list):
            direction.pop("west")
        if (x == self.width - 1 or maze[y][x + 1] != 15
                or (x + 1, y) in self.forty_two_list):
            direction.pop("east")
        if (y == 0 or maze[y - 1][x] != 15
                or (x, y - 1) in self.forty_two_list):
            direction.pop("north")
        if (y == self.height - 1 or maze[y + 1][x] != 15
                or (x, y + 1) in self.forty_two_list):
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

    ##
    @staticmethod
    def print_maze(maze):
        for x in maze:
            for y in x:
                print(f"{y}{"":<4}", end="")
            print("")
        print("\n")
    ##

    def break_dead_end(self, x: int, y: int, maze: list[list[int]]) -> int:
        direction = {"north": 1, "east": 2, "south": 4, "west": 8}
        if (x == 0 or maze[y][x] & 8 == 0
                or (x - 1, y) in self.forty_two_list):
            direction.pop("west")
        if (x == self.width - 1 or maze[y][x] & 2 == 0
                or (x + 1, y) in self.forty_two_list):
            direction.pop("east")
        if (y == 0 or maze[y][x] & 1 == 0
                or (x, y - 1) in self.forty_two_list):
            direction.pop("north")
        if (y == self.height - 1 or maze[y][x] & 4 == 0
                or (x, y + 1) in self.forty_two_list):
            direction.pop("south")
        if direction == {}:
            return 0
        return random.choice(list(direction.values()))

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
                if not self.perfect:
                    self.break_dead_end(pos_x, pos_y, maze)
                actual_path.pop()
                if actual_path != []:
                    pos_x, pos_y = actual_path[-1]
                continue
            maze[pos_y][pos_x] -= self.break_common_wall(direction)
            if self.break_common_wall(direction) != 0:
                actual_path.append((pos_x, pos_y))
        return maze

    def select_avaible_position(
        self, maze: list[list[int]], pos_x, pos_y, visited_list: set[tuple]
    ) -> tuple:
        if (
            pos_x != 0
            and maze[pos_y][pos_x - 1] & 2 == 0
            and (pos_x - 1, pos_y) not in visited_list
        ):
            return (pos_x - 1, pos_y)
        if (
            pos_x != self.width - 1
            and maze[pos_y][pos_x + 1] & 8 == 0
            and (pos_x + 1, pos_y) not in visited_list
        ):
            return (pos_x + 1, pos_y)
        if (
            pos_y != 0
            and maze[pos_y - 1][pos_x] & 4 == 0
            and (pos_x, pos_y - 1) not in visited_list
        ):
            return (pos_x, pos_y - 1)
        if (
            pos_y != self.height - 1
            and maze[pos_y + 1][pos_x] & 1 == 0
            and (pos_x, pos_y + 1) not in visited_list
        ):
            return (pos_x, pos_y + 1)
        return (-1, -1)

    def create_depth_maze(self, maze: list[list[int]]) -> list[list[int]]:
        depth_maze: list[list[int]] = self.create_full_maze(
            self.width, self.height
        )
        pos_x = self.exit_x
        pos_y = self.exit_y
        depth = 0
        actual_path: list[tuple] = [(pos_x, pos_y)]
        visited_list: set[tuple] = {(pos_x, pos_y)}
        depth_maze[pos_y][pos_x] = depth
        while actual_path != []:
            avaible_pos = self.select_avaible_position(
                maze, pos_x, pos_y, visited_list
            )
            if avaible_pos == (-1, -1):
                actual_path.pop()
                if actual_path != []:
                    pos_x, pos_y = actual_path[-1]
                depth = depth_maze[pos_y][pos_x]
                continue
            pos_x, pos_y = avaible_pos
            depth += 1
            depth_maze[pos_y][pos_x] = depth
            visited_list.add((pos_x, pos_y))
            actual_path.append((pos_x, pos_y))
        return depth_maze

    def select_min_avaible_position(
        self,
        maze: list[list[int]],
        pos_x,
        pos_y,
        depth_maze: list[list[int]],
        visited_list: set[tuple],
    ) -> dict[str, Any]:
        avaible_list: list[dict[str, Any]] = []
        if (
            pos_x != 0
            and maze[pos_y][pos_x - 1] & 2 == 0
            and not (pos_x - 1, pos_y) in visited_list
        ):
            avaible_list.append(
                {
                    "direction": "W",
                    "pos": (pos_x - 1, pos_y),
                    "depth": depth_maze[pos_y][pos_x - 1],
                }
            )
        if (
            pos_x != self.width - 1
            and maze[pos_y][pos_x + 1] & 8 == 0
            and not (pos_x + 1, pos_y) in visited_list
        ):
            avaible_list.append(
                {
                    "direction": "E",
                    "pos": (pos_x + 1, pos_y),
                    "depth": depth_maze[pos_y][pos_x + 1],
                }
            )
        if (
            pos_y != 0
            and maze[pos_y - 1][pos_x] & 4 == 0
            and not (pos_x, pos_y - 1) in visited_list
        ):
            avaible_list.append(
                {
                    "direction": "S",
                    "pos": (pos_x, pos_y - 1),
                    "depth": depth_maze[pos_y - 1][pos_x],
                }
            )
        if (
            pos_y != self.height - 1
            and maze[pos_y + 1][pos_x] & 1 == 0
            and not (pos_x, pos_y + 1) in visited_list
        ):
            avaible_list.append(
                {
                    "direction": "N",
                    "pos": (pos_x, pos_y + 1),
                    "depth": depth_maze[pos_y + 1][pos_x],
                }
            )
        if avaible_list == []:
            return {}
        return min(avaible_list, key=lambda min_depth: min_depth["depth"])


    def maze_floodfill_solver(self) -> list[dict]:
        maze = self.dfs_maze_generator()
        depth_maze = self.create_depth_maze(maze)
        pos_x = self.entry_x
        pos_y = self.entry_y
        solve_path: list[dict] = []
        visited_list: set[tuple] = set([])
        while (pos_x, pos_y) != (self.exit_x, self.exit_y):
            min_avaible_pos = self.select_min_avaible_position(
                maze, pos_x, pos_y, depth_maze, visited_list
            )
            if min_avaible_pos == {}:
                if solve_path != []:
                    solve_path.pop()
                    pos_x, pos_y = solve_path[-1]
                continue
            pos_x, pos_y = min_avaible_pos["pos"]
            visited_list.add((pos_x, pos_y))
            solve_path.append(min_avaible_pos)
        return solve_path

    def maze_convertor(self) -> str:
        maze = self.dfs_maze_generator()
        convert_str = ""
        for x in maze:
            for y in x:
                convert_str += format(y, 'x')
            convert_str += "\n"
        return convert_str

    def create_output_file(self) -> None:
        maze_convert = self.maze_convertor()
        solve_path = self.maze_floodfill_solver()
        with open(self.output_file, "w") as output_f:
            output_f.write(f"{maze_convert}\n")
            output_f.write(f"{self.entry_x}.{self.entry_y}\n")
            output_f.write(f"{self.exit_x}.{self.exit_y}\n")
            for x in solve_path:
                output_f.write(x["direction"])
            output_f.write("\n")
