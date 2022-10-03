import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# for see interaction
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# chrome_options = Options()
options.add_experimental_option("detach", True)                         
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)



# obtener el contenido de la web
url_to_grab = "https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc/"
driver.get(url_to_grab)

text_imput = driver.find_element(By.ID, "busquedaRucId")
text_imput.send_keys("2390060680001")


consultar_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row'][2]//button" )))
consultar_button.click()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.recaptcha-checkbox-checkmark"))).click()

# time.sleep(11)

# establecimientos_button = driver.find_element(By.XPATH, "//div[@class='col-sm-12'][2]//button")
# establecimientos_button.click()

# time.sleep(5)

# doc = BeautifulSoup(driver.page_source, "html.parser")
# text = doc.text
# print(text)