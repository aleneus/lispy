# Release checklist

* code: no TODO (`$ make todo`)
* test: all passed (`$ make check`)
* test: coverage == 100% (`htmlcov`)
* style: no flakes (`$ make flake`)
* pylint: result >= 9.1 (`$ make lint`)
* pylint: no errors (`$ make lint-e`)
* deploy: actual version (`__init__.py`)
