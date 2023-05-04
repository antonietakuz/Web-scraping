from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Buscar un botón, seleccione un elemento dentro del menú desplegable y extraiga datos de una tabla

# definir el sitio web para scrapear y la ruta donde se encuentra el chromediver

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/Users/frank/Downloads/chromedriver' # write the path here


#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# define 'driver' variable
driver = webdriver.Chrome(path)
# open Google Chrome with chromedriver
driver.get(website)

# ubica el boton 
all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')

# click en el boton
all_matches_button.click()

# usamos un box  como referencia para ayudarnos a ubicar un elemento dentro
box = driver.find_element(By.CLASS_NAME,'panel-body')
# seleccionamos el dropdown y seleccionamos el elemnto dentro a trav{es del texto visible
dropdown = Select(box.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')
# implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
#time.sleep(5)
# seleccionamos el elemento en la tabla
matches = driver.find_elements(By.CSS_SELECTOR,'tr')

# almaceno en una lista

partidos = []

for match in matches:
	partidos.append(match.text)
#quit drive we opened in the beginning

driver.quit()


df= pd.DataFrame({'partidos':partidos})
print(df)

# Bonus: Create Dataframe in Pandas and export to CSV (Excel)

df.to_csv('tutorial.csv', index=False)


