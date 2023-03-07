
default:
	poetry install
	poetry run python repro_type_error_whylogs/main.py
