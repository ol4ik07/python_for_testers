class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_the_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_new(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()

        wd.find_element_by_name("submit").click()
        self.return_to_the_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.first_name)
        self.change_contact_value("middlename", contact.midname)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nick)
        self.change_contact_value("title", contact.title)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("home", contact.home)
        self.change_contact_value("mobile", contact.mobile)
        self.change_contact_value("work", contact.work)
        self.change_contact_value("fax", contact.fax)
        self.change_contact_value("email", contact.email)
        self.change_contact_value("homepage", contact.homepage)
        self.change_contact_value("byear", contact.year)
        self.change_contact_value("ayear", contact.ayear)
        self.change_contact_value("phone2", contact.phone)
        self.change_contact_value("notes", contact.notes)


    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # def del_all_contacts(self):
    #     wd = self.app.wd
    #     self.return_to_the_home_page()
    #     # if not wd.find_element_by_id("19").is_selected():
    #     #   wd.find_element_by_id("19").click()
    #     if not wd.find_element_by_id("MassCB").is_selected():
    #         wd.find_element_by_id("MassCB").click()
    #     # self.select_first_contact()
    #     # wd.find_element_by_name("delete").click()
    #     # wd.find_element_by_name("selected[]").click()
    #     wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
    #
    #     wd.switch_to_alert().accept()
    #     self.return_to_the_home_page()
    #
    # def select_first_contact(self):
    #     wd = self.app.wd
    #     # if not wd.find_element_by_name("selected[]").is_selected():
    #     # wd.find_element_by_name("selected[]").click()
    #     # wd.find_element_by_name("selected[]").click()
    #     wd.find_element_by_name("selected[]").click()
    def delete_first_contact(self):
        wd = self.app.wd

        self.return_to_the_home_page()

        self.select_first_contact()

        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

        self.return_to_the_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_the_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry'][1]/td[8]/a").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_the_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_the_home_page()
        return len(wd.find_elements_by_name("selected[]"))