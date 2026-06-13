.PHONY: help install install-system clean

help:
	@echo "Claude Code SAT Tutor - Available targets:"
	@echo ""
	@echo "  install           Install Python dependencies with uv"
	@echo "  install-system    Install system dependencies (pandoc)"
	@echo "  clean             Remove virtual environment and cache files"
	@echo "  help              Show this help message"

install:
	uv sync

install-system:
	@if ! command -v pandoc &> /dev/null; then \
		echo "Installing pandoc..."; \
		if command -v brew &> /dev/null; then \
			brew install pandoc; \
		else \
			echo "Error: pandoc not found and brew is not available."; \
			echo "Install pandoc manually from: https://pandoc.org/installing.html"; \
			exit 1; \
		fi \
	else \
		echo "pandoc is already installed"; \
	fi

clean:
	rm -rf .venv
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "Cleaned up virtual environment and cache files"
