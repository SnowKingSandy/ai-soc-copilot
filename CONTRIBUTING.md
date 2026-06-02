# Contributing to AI SOC Copilot

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/yourusername/ai-soc-copilot.git
cd ai-soc-copilot
```

### 2. Create a Virtual Environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8  # Dev dependencies
```

## Development Workflow

### Creating a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### Coding Standards

- **Python**: Follow PEP 8
- **Type Hints**: Use type annotations where possible
- **Documentation**: Add docstrings to functions and classes
- **Testing**: Write tests for new features

### Format Code
```bash
black app/ tests/
flake8 app/ tests/
```

### Run Tests
```bash
pytest tests/ -v --cov=app
```

## Commit Messages

Use clear, descriptive commit messages:

```
✨ Add new threat detection model
🐛 Fix incident parsing bug
📚 Update API documentation
🔧 Refactor severity service
```

Commit message format:
```
<type>: <subject>

<body>

<footer>
```

Types:
- `✨ feat` - New feature
- `🐛 fix` - Bug fix
- `📚 docs` - Documentation
- `♻️ refactor` - Code refactoring
- `🧪 test` - Add tests
- `🔧 chore` - Build/tooling

## Pull Request Process

1. **Create PR with descriptive title**
   - Reference any related issues: "Closes #123"

2. **Provide detailed description**
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update

   ## Testing
   How to test these changes

   ## Screenshots
   If applicable, add screenshots
   ```

3. **Ensure tests pass**
   ```bash
   pytest tests/ -v
   ```

4. **Code review**
   - Address feedback
   - Update code as needed
   - Mark conversations as resolved

5. **Merge**
   - Squash commits if necessary
   - Delete feature branch

## Adding New Features

### Example: Adding a New Service

1. Create `backend/app/services/my_service.py`
2. Add tests in `backend/tests/test_my_service.py`
3. Update documentation in `docs/`
4. Create PR with examples

### Example: Adding an API Endpoint

1. Add route in `backend/app/api/`
2. Create schema in `backend/app/schemas/`
3. Add to main.py router
4. Document in `docs/api_design.md`
5. Add tests

## Testing Guidelines

### Unit Tests
```python
def test_threat_detection():
    result = detect_threat("malicious log")
    assert result.severity == "high"
```

### Integration Tests
```python
def test_api_analyze_endpoint(client):
    response = client.post("/analyze", json={"log_text": "..."})
    assert response.status_code == 200
```

Run with coverage:
```bash
pytest tests/ --cov=app --cov-report=html
```

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Document new features in docs/
- Include examples where helpful

## Reporting Issues

### Bug Reports
- Describe the bug clearly
- Steps to reproduce
- Expected vs actual behavior
- Environment (OS, Python version)
- Logs/screenshots if applicable

### Feature Requests
- Clearly describe the feature
- Explain the use case
- Provide examples if possible
- Discuss implementation approach

## Project Structure

Keep the structure organized:
- API endpoints → `app/api/`
- Business logic → `app/services/`
- Data models → `app/schemas/` and `app/models/`
- Agents → `app/agents/`
- Configuration → `app/core/`
- Tests → `tests/`

## Areas for Contribution

- **Frontend**: React/Next.js dashboard
- **Backend**: New agents, services, API endpoints
- **Infrastructure**: Docker, Kubernetes configs
- **Documentation**: Guides, API docs, architecture diagrams
- **Testing**: Expand test coverage
- **Performance**: Optimization, caching
- **Security**: Auth, rate limiting, validation

## Need Help?

- Check existing issues and discussions
- Review documentation in `docs/`
- Look at existing code for patterns
- Ask in pull request comments

## Recognition

Contributors will be:
- Listed in README.md
- Credited in commit messages
- Acknowledged in releases

---

Thank you for contributing to AI SOC Copilot! 🎉
