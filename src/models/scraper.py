from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def lanzar_cxt(driver, centros, especialidade, ente, vernaculo, linguas, itinerancias, limite):
    for i, centro in enumerate(centros):
        if limite > 0 and i >= limite:
            linguas_uso = [linguas[0]]
            itinerancias_uso = [itinerancias[0]]
        else:
            linguas_uso = linguas
            itinerancias_uso = itinerancias

        for itinerancia in itinerancias_uso:
            textbox = driver.find_element(By.NAME, "datPets.codigo")
            textbox.clear()
            textbox.send_keys(centro)
            Select(driver.find_element(By.NAME, "datPets.codEspecialidade")).select_by_visible_text(especialidade)
            Select(driver.find_element(By.NAME, "datPets.codEnteVernaculo")).select_by_visible_text(ente)
            Select(driver.find_element(By.NAME, "datPets.codVernaculo")).select_by_visible_text(vernaculo)
            Select(driver.find_element(By.NAME, "datPets.itinerancia")).select_by_visible_text(itinerancia)
            for lingua in linguas_uso:
                Select(driver.find_element(By.NAME, "datPets.codBilinguismo")).select_by_visible_text(lingua)
                driver.find_element(By.NAME, "DIALOG-EVENT-operacionAlta").click()
                WebDriverWait(driver, 15).until(
                    EC.invisibility_of_element_located((By.ID, "page-loader"))
                )


def lanzar_cadp(driver, centros, corpo, especialidade, linguas, afin, itinerancias, limite):
    for i, centro in enumerate(centros):
        if limite > 0 and i >= limite:
            linguas_uso = [linguas[0]]
            itinerancias_uso = [itinerancias[0]]
        else:
            linguas_uso = linguas
            itinerancias_uso = itinerancias

        for itinerancia in itinerancias_uso:
            textbox = driver.find_element(By.NAME, "cenloc")
            textbox.clear()
            textbox.send_keys(centro)
            Select(driver.find_element(By.NAME, "codCorpo")).select_by_visible_text(corpo)
            Select(driver.find_element(By.NAME, "codEspecialidade")).select_by_visible_text(especialidade)
            checkbox_itinerante = driver.find_element(By.NAME, "aceptaItinerante")
            if (itinerancia == "Si" and not checkbox_itinerante.is_selected()) or (itinerancia == "Non" and checkbox_itinerante.is_selected()):
                checkbox_itinerante.click()

            for lingua in linguas_uso:
                Select(driver.find_element(By.NAME, "comboLinguas")).select_by_visible_text(lingua)
                checkbox = driver.find_element(By.NAME, "aceptaAfin")
                if afin and not checkbox.is_selected():
                    checkbox.click()
                driver.find_element(By.ID, "operacion1").click()
                driver.find_element(By.NAME, "DIALOG-EVENT-aplicarCambio").click()
