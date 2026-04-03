#!/usr/bin/env python3

import sys
from config_parser import GetConfig
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Annotated
from typing_extensions import Self
from maze_generator import MazeGenerator


class ConfigData(BaseModel):

    WIDTH: Annotated[int, Field(ge=2, le=1000)]
    HEIGHT: Annotated[int, Field(ge=2, le=1000)]
    ENTRY_X: Annotated[int, Field(ge=0, le=1500)]
    ENTRY_Y: Annotated[int, Field(ge=0, le=900)]
    EXIT_X: Annotated[int, Field(ge=0, le=1500)]
    EXIT_Y: Annotated[int, Field(ge=0, le=900)]
    OUTPUT_FILE: Annotated[str, Field(min_length=5, max_length=50)]
    PERFECT: bool

    @model_validator(mode='after')
    def validation(self) -> Self:
        # add condition where start and end are in the "42"
        if self.ENTRY_X == self.EXIT_X and self.ENTRY_Y == self.EXIT_Y:
            raise ValueError("Entry and exit exist and are different, "
                             "inside the maze bounds")
        if self.ENTRY_X > self.WIDTH - 1 or self.EXIT_X > self.WIDTH - 1:
            raise ValueError("ENTRY_X and EXIT_X must be < WIDTH - 1")
        if self.ENTRY_Y > self.HEIGHT - 1 or self.EXIT_Y > self.HEIGHT - 1:
            raise ValueError("ENTRY_Y and EXIT_Y must be < WIDTH - 1")
        return self


def main() -> None:

    if not len(sys.argv) == 2:
        raise Exception("You must run the programm like"
                        " <python3 a_maza_ing.py config.txt>")
    config_parser = GetConfig(sys.argv[1])
    data_dict = config_parser.get_data_config()
    data_dict["ENTRY_X"] = data_dict["ENTRY"].split(",")[0]
    data_dict["ENTRY_Y"] = data_dict["ENTRY"].split(",")[1]
    data_dict["EXIT_X"] = data_dict["EXIT"].split(",")[0]
    data_dict["EXIT_Y"] = data_dict["EXIT"].split(",")[1]
    try:
        ConfigData.model_validate(data_dict)
    except ValidationError as e:
        print(f"Pydantic Error:\n{e.errors()[0]['msg']}")
        return

    maze_generator = MazeGenerator(
        int(data_dict["WIDTH"]),
        int(data_dict["HEIGHT"]),
        int(data_dict["ENTRY_X"]),
        int(data_dict["ENTRY_X"]),
        int(data_dict["EXIT_X"]),
        int(data_dict["EXIT_Y"]),
        data_dict["OUTPUT_FILE"],
        bool(data_dict["PERFECT"]))

    print(maze_generator.maze_floodfill_solver())
    maze_generator.create_output_file()


if __name__ == "__main__":

    main()
