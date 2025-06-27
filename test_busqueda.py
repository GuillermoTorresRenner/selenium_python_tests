from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar opciones del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")

# Inicializar el driver de Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navegar a DuckDuckGo
    driver.get("https://duckduckgo.com/")

    # Buscar campo de texto
    buscador = driver.find_element(By.NAME, "q")
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)

    # Esperar a que se carguen los resultados
    time.sleep(5)

    # Validar que exista algún resultado
    # Usar selectores CSS más específicos para DuckDuckGo
    resultados = driver.find_elements(
        By.CSS_SELECTOR, "[data-testid='result']")

    # Si no encuentra con el primer selector, probar con otros
    if len(resultados) == 0:
        resultados = driver.find_elements(By.CSS_SELECTOR, "article")
    if len(resultados) == 0:
        resultados = driver.find_elements(By.CSS_SELECTOR, ".result")
    if len(resultados) == 0:
        resultados = driver.find_elements(
            By.CSS_SELECTOR, "div[data-layout='organic']")

    assert len(resultados) > 0, "No se encontraron resultados."

    print("✅ Prueba funcional completada con éxito")
    print(f"Se encontraron {len(resultados)} resultados")

except (AssertionError, ValueError) as e:
    print(f"❌ Fallo en la validación: {e}")
except (ImportError, ModuleNotFoundError) as e:
    print(f"❌ Error de dependencias: {e}")
    print("Asegúrate de instalar selenium: pip install selenium")
except Exception as e:
    print(f"❌ Error inesperado: {e}")

finally:
    # Cerrar el navegador
    driver.quit()
