from Pages.Locgeneric import LocGeneric

class Webgeneric(LocGeneric):
    def __init__(self,driver):
        LocGeneric.__init__(self,driver)
        lc=LocGeneric(driver)


    def enter(self,loc_type,loc_val,input_val):
        e=self.locator(loc_type,loc_val)
        e.send_keys(input_val)


    def submit(self,loc_type,loc_val):
        e=self.locator(loc_type,loc_val)
        e.click()

    def report(self):
        pass

    def report_fail(self):
        pass