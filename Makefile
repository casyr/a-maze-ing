
install: 
		pip install uv

run: 
		python3 a_maze_ing.py config.txt

debug:  
		python3 -m 
clean: 
		rm -rf __mypy_cache .mypy_cache

lint: 
		flake8 . mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
		flake8 . mypy . --strict