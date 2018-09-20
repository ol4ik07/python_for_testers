from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count()==0:
        app.contact.add_new(Contact(lastname="add_new_bacause_no_contacts_for_modify"))
    app.contact.modify_first_contact(Contact(first_name="Modified contacts name"))


def test_modify_contact_mobile(app):
    if app.contact.count()==0:
        app.contact.add_new(Contact(lastname="add_new_bacause_no_contacts_for_modify"))
    app.contact.modify_first_contact(Contact(mobile="Modified contacts mobile"))
