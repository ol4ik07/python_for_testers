def test_delete_contact(app):


    app.session.login( username="admin", password="secret")
    app.contact.del_all_contacts()
    app.session.logout()