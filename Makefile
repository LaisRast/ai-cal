VENV_DIR = venv

run:
	@echo "Running app..."
	@source $(VENV_DIR)/bin/activate && $(VENV_DIR)/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

.PHONY: run