from selenium import webdriver
from selenium.webdriver.common.by import By
import ui  # Import the Tkinter UI module

# Task 1: Form Field Detection using Selenium
def detect_form_fields(url):
    driver = webdriver.Chrome()
    driver.get(url)
    form_elements = driver.find_elements(By.TAG_NAME, 'input')
# Open the target webpage
driver.get('https://example.com/form-page')

# Detect all form elements
form_elements = driver.find_elements(By.TAG_NAME, 'input')

# Loop through elements to identify their types
for element in form_elements:
    field_type = element.get_attribute('type')
    if field_type == 'text':
        print(f'Text field detected: {element.get_attribute("name")}')
    elif field_type == 'password':
        print(f'Password field detected: {element.get_attribute("name")}')
    elif field_type == 'checkbox':
        print(f'Checkbox detected: {element.get_attribute("name")}')
    elif field_type == 'radio':
        print(f'Radio button detected: {element.get_attribute("name")}')
    else:
        print(f'Other field type: {field_type}, {element.get_attribute("name")}')
# Add more field types as needed
# Close the WebDriver
driver.quit()

# Main Program
if __name__ == '__main__':
    # Example of form detection (Task 1)
    detect_form_fields('https://example.com/form-page')

    # Launch the Tkinter UI (Task 2)
    ui.setup_ui()