from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count()==0:
        app.contact.add_new(Contact(lastname="test"))
    app.contact.delete_first_contact()
