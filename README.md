## Selenium Python Automation with Allure & GitHub Actions

This project demonstrates UI automation using Selenium WebDriver with Python. Test results are published with Allure and executed automatically via GitHub Actions.

---

### ✅ Tools Used
- Selenium WebDriver
- Pytest
- Allure for reporting
- GitHub Actions for CI

---

### 🚀 How to Run Locally

```bash
pip install -r requirements.txt
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

### 🧪 Test Scenario
- Visit login page
- Enter username and password
- Click login and validate redirection

---

### 🔁 Continuous Integration
Test cases run on every push using GitHub Actions. Reports will be generated and published.

---

# 📦 requirements.txt
selenium
pytest
allure-pytest
