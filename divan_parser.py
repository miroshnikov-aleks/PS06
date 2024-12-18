from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Укажите путь к вашему WebDriver
driver = webdriver.Chrome()
driver.get('https://www.divan.ru/bryansk/category/svet')

# Дайте странице время загрузиться
time.sleep(5)

products = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k.U4KZV')

with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Image URL'])

    for product in products:
        try:
            name = product.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe').text
            price_elements = product.find_elements(By.CSS_SELECTOR, 'div.pY3d2')
            if price_elements:
                # Предполагается, что первый элемент содержит актуальную цену
                price_text = price_elements[0].text.split()[0]  # Получаем только первое значение, если их несколько
                if price_text.isdigit() and len(price_text) == 2:
                    price = f"{price_text}990 руб."
                else:
                    price = price_text
            else:
                price = "Цена не найдена"

            image_url = product.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

            writer.writerow([name, price, image_url])
        except Exception as e:
            print(f"Ошибка при обработке продукта: {e}")

driver.quit()