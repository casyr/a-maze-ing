#!/usr/bin/env python3

import sys
from .config_parser import GetConfig
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Annotated


class config_data(BaseModel):

    width: Annotated[int, Field(ge=100, le=1980)]
    




def config_checker(config: dict[str, str]):
    ...


def main() -> None:

    if not len(sys.argv) == 2:
        raise Exception("You must run the programm like"
                        " <python3 a_maza_ing.py config.txt>")

    config = GetConfig(sys.argv[2])
    try:
        config_checker(config.get_data_config())
    except Exception as e:
        print(e)


if __name__ == "__main__":

    main()
