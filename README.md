# Playwright E2E Automation Framework

[![Playwright Tests](https://github.com/s-rengifo-dev/Qa_playwright/actions/workflows/playwright_tests.yml/badge.svg)](https://github.com/s-rengifo-dev/Qa_playwright/actions/workflows/ci.yml)

Framework de automatización de pruebas E2E diseñado para garantizar estabilidad, observabilidad y trazabilidad en la suite de pruebas. Implementado con un enfoque de integración continua para asegurar la calidad en cada iteración.

---

### 🚀 CI/CD Pipeline (GitHub Actions)
Este proyecto integra una pipeline automatizada para validación de calidad:
* **Disparadores:** Ejecución automática en cada `push` o `pull_request` sobre la rama `develop`.
* **Entorno:** Ejecución en contenedores Ubuntu (Linux).
* **Observabilidad:** Generación automática de reportes con Allure, almacenados como artefactos descargables por 7 días.
* **Configuración:** Utiliza *GitHub Secrets* para la gestión segura de credenciales (`QA_USER`, `QA_PASSWORD`).

### 🛠 Tech Stack
* **Lenguaje:** Python 3.12+
* **Core:** Playwright
* **Test Runner:** Pytest
* **Reporting:** Allure Framework
* **CI/CD:** GitHub Actions

### ⚙️ Configuración Inicial
1. **Clonar el repositorio.**
2. **Entorno virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
Instalar dependencias:

PowerShell
pip install -r requirements.txt
🚀 Ejecución Local
La configuración está centralizada en pytest.ini.
Nota: Para ejecuciones locales, asegúrate de configurar tus variables de entorno (puedes usar un archivo .env).

Ejecutar tests:

PowerShell
pytest
Generar y visualizar reportes (Allure):

PowerShell
allure serve allure-results
📂 Estructura
Plaintext
├── .github/workflows/    # CI/CD Pipelines (GitHub Actions)
├── allure-results/       # Metadata generada tras ejecución
├── pages/                # Page Object Model (POM)
├── tests/                # Casos de prueba (*_test.py)
├── conftest.py           # Fixtures globales
├── pytest.ini            # Configuración de ejecución
└── requirements.txt      # Dependencias
🔒 Configuración de Seguridad (CI/CD)
Para que el pipeline funcione correctamente, debes configurar los secretos en tu repositorio de GitHub:

Ve a Settings > Secrets and variables > Actions.

Crea los siguientes Repository secrets:

QA_USER

QA_PASSWORD

Framework mantenido con buenas prácticas de automatización.
