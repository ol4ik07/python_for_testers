# -*- coding: utf-8 -*-

from model.contact import Contact

    
def test_add_contact(app):


    app.contact.add_new(Contact(first_name="bdwhjw", midname="bxsgv", lastname="hjbu", nick="ghvjb", title="cdfgc", company="rdfgh", address="dfghj", home="rftyguhgjb", mobile="hgvb",
                                work="ghjnk", fax="fghbjnk", email="fgvhbjn", homepage="fghjkjiuhgy", year="1111", ayear="2222", phone="87yt6rdxgcvhbn", notes="dfghvbjn"))


def test_add_empty_contact(app):


    app.contact.add_new(Contact(first_name="", midname="", lastname="", nick="", title="", company="", address="", home="", mobile="",
                                work="", fax="", email="", homepage="", year="", ayear="", phone="", notes=""))
