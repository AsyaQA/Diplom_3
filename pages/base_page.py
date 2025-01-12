from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_the_element(self, locator):
        self.find_element_with_wait(locator).click()

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def add_text_in_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def wait_for_disappears_element_for_firefox(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element(element)
        )

    def find_element_without_wait(self, locator):
        return self.driver.find_element(*locator)

    def find_element_change_text(self, locator, text):
        self.driver.find_element(*locator)
        WebDriverWait(self.driver, 5).until_not(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )

    def move_the_element(self, locator, locator_target):
        element = self.find_element_with_wait(locator)
        target = self.find_element_with_wait(locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    def move_the_element_for_firefox(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true, 
                    cancelable: true, 
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);
                var dropEvent = new DragEvent('drop', {
                    bubbles: true, 
                    cancelable: true, 
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true, 
                    cancelable: true, 
                    dataTransfer: dataTransfer
                }); 
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        self.driver.execute_script(script, source_element, target_element)

    def format_locator(self, locator, text):
        method, f_locator = locator
        f_locator = f_locator.format(text)
        return method, f_locator
