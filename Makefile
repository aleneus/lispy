PACKAGE_FOLDER = lispy

help:
	@echo "todo"
	@echo "check"
	@echo "flake"
	@echo "lint"
	@echo "lint-e"

todo:
	@rgrep "TODO" --include="*py" --include="*md" --exclude="release-checklist.md"

check:
	@nose2 --with-coverage --coverage-report=html

flake:
	flake8 $(PACKAGE_FOLDER)

lint:
	pylint $(PACKAGE_FOLDER)

lint-e:
	pylint --disable=R,C,W $(PACKAGE_FOLDER)
