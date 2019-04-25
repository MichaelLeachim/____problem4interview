# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .views import MainView

# Create your tests here.

class MainViewTests(TestCase):
  def test_getting_data_from_the_remote(self):
    # import pdb; pdb.set_trace()
    datum,isok = MainView().load_transaction_data()
    self.assertEqual(isok,True)
    
    datum,isok = MainView().load_transaction_data(app_token="whatever")
    self.assertEqual(isok,False)
    self.assertEqual(datum,{u'message': u'Auth Token is not valid', u'reason': u'BadAuthToken',
                            u'reason': 'Unauthorized',u'status_code': 401})
    




