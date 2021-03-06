# Copyright (c) 2008 Pavol Rusnak, Michal Vyskocil
# see __init__.py for license details

import gettext

import scout

_ = gettext.gettext


class ScoutModule(scout.SimpleScoutModule):

    name = 'foo'
    desc = _('- template module -')
    sql = 'SELECT package, @@FOO@@, @@BAR@@ FROM @@BAR@@s ' \
        'LEFT JOIN @@FOO@@s ON @@BAR@@s.id_@@FOO@@=@@FOO@@s.id_@@FOO@@ ' \
        'LEFT JOIN packages ON @@FOO@@s.id_pkg=packages.id_pkg ' \
        'WHERE @@BAR@@ LIKE ?'
    sqli = 'SELECT package, @@FOO@@, @@BAR@@ FROM @@BAR@@s ' \
        'LEFT JOIN @@FOO@@s ON @@BAR@@s.id_@@FOO@@=@@FOO@@s.id_@@FOO@@ ' \
        'LEFT JOIN packages ON @@FOO@@s.id_pkg=packages.id_pkg ' \
        'WHERE package LIKE ?'
    scout.null_lang.install()
    result_list = ['repo', 'pkg', '@@FOO@@', '@@BAR@@']
    result_list2 = ['repository', 'package', '@@FOO@@ file', '@@BAR@@']
    scout.default_lang.install()
