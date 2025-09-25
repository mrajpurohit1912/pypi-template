# PyPI Template 🚀

A **basic template repository** for creating and publishing Python packages to [PyPI](https://pypi.org/).  
This repo provides a minimal yet complete setup with support for:
- Packaging via `setup.py` and `pyproject.toml`
- Development dependencies
- Automated testing with `tox`
- GitHub Actions workflows
- Example project structure under `src/`

---

## 📦 Features
- Ready-to-use **Python package structure** (`src/` layout).
- `setup.py`, `setup.cfg`, and `pyproject.toml` included.
- Dependency management with `requirements.txt` and `requirements_dev.txt`.
- Unit testing support with `pytest`.
- CI/CD ready with GitHub Actions + `tox`.
- Example template file (`template.py`) and test folder.

---

## 🗂 Project Structure
```bash
├── src/example_demo/ # Package source code
├── tests/ # Unit tests
├── .github/workflows/ # CI workflows
├── requirements.txt # Runtime dependencies
├── requirements_dev.txt# Dev dependencies
├── setup.py # Setup script
├── setup.cfg # Configurations
├── pyproject.toml # Build system config
├── tox.ini # Test automation
└── README.md # Project documentation
```

## ⚙️ Setup

1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

3. 🧪 Running Tests
```bash
pytest tests/
or
tox
```


## 🚀 Publishing to PyPI
1. Build the package
```bash
python setup.py sdist bdist_wheel
```

2. Upload to TestPyPI
```bash
pip install twine
twine upload --repository testpypi dist/*
```

3. Upload to PyPI
```bash
twine upload dist/*
```
