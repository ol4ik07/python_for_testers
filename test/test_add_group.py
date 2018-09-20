# -*- coding: utf-8 -*-


from model.group import Group


def test_add_group(app):

    app.group.create(Group(name="fgtyhtgfd", header="dfrtghy", footer="cdfgvbhnjyu"))


def test_empty_group(app):

    app.group.create(Group(name="", header="", footer=""))


