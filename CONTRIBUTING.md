# Contributing to TRIANGLE

Thanks for your interest in contributing! Here's how you can help.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/triangle.git`
3. Create a feature branch: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Commit: `git commit -m "Add amazing feature"`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## Code Style

- Follow PEP 8
- Use Black for formatting: `black .`
- Use Flake8 for linting: `flake8 .`
- Use MyPy for type checking: `mypy app/`

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=app tests/

# Run specific test
pytest tests/unit/test_models.py -v
```

## Pull Request Process

1. Update README.md with any new features
2. Ensure tests pass
3. Update CHANGELOG.md
4. Request review from maintainers

## Reporting Issues

Please include:
- Python version
- Operating system
- Error message and traceback
- Steps to reproduce

Thank you for contributing! ⭐
