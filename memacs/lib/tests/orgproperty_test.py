# -*- coding: utf-8 -*-
# Time-stamp: <2011-12-20 15:13:31 awieser>

import unittest
import time
from memacs.lib.orgformat import OrgFormat
from memacs.lib.orgproperty import OrgProperties


class TestOrgProperties(unittest.TestCase):

    def test_properties_default_ctor(self):
        p = OrgProperties("hashing data 1235")
        properties = unicode(p).splitlines()
        self.assertEqual(properties[0], u"   :PROPERTIES:")
        self.assertEqual(properties[1],
            u"   :ID:         063fad7f77461ed6a818b6b79306d641e9c90a83")
        self.assertEqual(properties[2], u"   :END:")

    def test_properties_with_own_created(self):
        p = OrgProperties()
        p.add(u"CREATED",
              OrgFormat.datetime(time.gmtime(0)))
        properties = unicode(p).splitlines()

        self.assertEqual(properties[0], u"   :PROPERTIES:")
        self.assertEqual(properties[1], u"   :CREATED:    <1970-01-0" + \
                         "1 Thu 00:00>")
        self.assertEqual(properties[2], u"   :ID:         fede47e9" + \
                         "f49e1b7f5c6599a6d607e9719ca98625")
        self.assertEqual(properties[3], u"   :END:")
