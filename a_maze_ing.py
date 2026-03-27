#!/usr/bin/env python3

from .config_parser import GetConfig
from pydantic import BaseModel, Field, ValidationError, model_validator


def config_checker(config: dict[str, str]):
    ...


def main() -> None:
    ...


if __name__ == "__main__":
    main()
