#!/usr/bin/env python3

from .config_parser import GetConfig
from pydantic import BaseModel, Field, ValidationError, model_validator


def config_checker(config: dict[str, str]):
    ...


def main() -> None:
    ...


if __name__ == "__main__":
    get_config = GetConfig()
    config = get_config.dict_config_info()
    config_checker(get_config)
    main()
