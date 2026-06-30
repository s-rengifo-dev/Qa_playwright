Markdown
# Playwright E2E Automation Framework

Framework de automatización de pruebas E2E diseñado para garantizar estabilidad, observabilidad y trazabilidad en la suite de pruebas de `the-internet.herokuapp.com`.

## Stack Tecnológico
- **Lenguaje:** Python 3.14+
- **Core:** Playwright
- **Test Runner:** Pytest
- **Reporting:** Allure Framework (con `allure-pytest`)
- **Gestor de Entorno:** venv (Python virtual environments)

## Prerrequisitos
1. **Python 3.x:** Instalado y accesible en el PATH.
2. **Java (JDK 17+):** Requerido exclusivamente para ejecutar el servidor de reportes de Allure (`allure serve`).
   - *Nota:* Asegúrate de tener la variable de entorno `JAVA_HOME` apuntando al directorio raíz de tu instalación JDK.
3. **Navegadores:** Playwright gestionará la instalación de los binarios (Chromium, Firefox, Webkit).

## Configuración Inicial
1. **Clonar/Acceder al repositorio.**
2. **Crear entorno virtual:**
   ```powershell
   python -m venv venv
Activar entorno:

PowerShell
.\venv\Scripts\activate
Instalar dependencias:

PowerShell
pip install -r requirements.txt
 Ejecución
Toda la configuración de ejecución (navegador, base URL, trazas) está centralizada en pytest.ini.

Ejecutar todos los tests:

PowerShell
pytest

 Reportes (Allure)
El framework genera automáticamente datos de reporte en la carpeta allure-results.

Generar y visualizar el reporte:

PowerShell
allure serve allure-results

 Estructura del Proyecto
Plaintext
├── .pytest_cache/        # Caché de pytest
├── allure-results/       # Metadata generada tras cada ejecución
├── pages/                # Page Object Model (POM)
├── tests/                # Casos de prueba (*_test.py)
├── venv/                 # Entorno virtual
├── conftest.py           # Fixtures globales (configuración de contexto)
├── pytest.ini            # Configuración de ejecución (addopts)
└── requirements.txt      # Dependencias del proyecto
 Notas Técnicas y Troubleshooting
Error JAVA_HOME: Si allure serve falla, verifica en las Variables de Entorno del Sistema que JAVA_HOME contenga la ruta absoluta del JDK y que Path incluya %JAVA_HOME%\bin.

Trazas y Videos: La configuración tracing=retain-on-failure y la grabación de video están habilitadas en pytest.ini. Los archivos se guardarán automáticamente en caso de fallo dentro de test-results/.