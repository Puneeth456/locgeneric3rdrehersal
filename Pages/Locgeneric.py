class LocGeneric():
    def __init__(self,driver):
        self.driver=driver


    def locator(self,loc_type,loc_val):
        try:
            if loc_type=='id':
                ele=self.driver.find_element_by_id(loc_val)
            elif loc_type=='name':
                ele=self.driver.find_element_by_name(loc_val)
            elif loc_type=='xpath':
                ele=self.driver.find_element_by_xpath(loc_val)
            elif loc_type=='tagname':
                ele=self.driver.find_element_by_tag_name(loc_val)
                return ele
        except AssertionError as e:
            self.report_fail
        except:
            self.report_fail()
