from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class RechnungsverwaltungOverview:
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'

	def select_multiple_invoices(self, ids):
		selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
		driver = selenium2lib._current_browser()
		
		actions = ActionChains(driver)
		
		for id in ids:
			item = selenium2lib.get_webelement(id+'/$invoiceNumber') 
			driver.execute_script("arguments[0].scrollIntoView(false);", item);
			actions.move_to_element(item)
			actions.click(item)
			actions.key_down(Keys.CONTROL)
			#selenium2lib.set_focus_to_element(id+'/$invoiceNumber')		
			#selenium2lib.click_element(item)
		
		actions.key_up(Keys.CONTROL)
		actions.perform()
		
	def select_invoices_between(self, id1, id2):
		selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
		driver = selenium2lib._current_browser()
				
		item1 = selenium2lib.get_webelement(id1+'/$invoiceNumber') 
		item2 = selenium2lib.get_webelement(id2+'/$invoiceNumber')   

		driver.execute_script("arguments[0].scrollIntoView(false);", item1);
		
		actions = ActionChains(driver)
		actions.move_to_element(item1)
		actions.click(item1)
		actions.key_down(Keys.SHIFT)		
		driver.execute_script("arguments[0].scrollIntoView(false);", item2);
		actions.move_to_element(item2)
		actions.click(item2)
		actions.key_up(Keys.SHIFT)
		actions.perform()