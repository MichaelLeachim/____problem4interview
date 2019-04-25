# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase,tag
from .views import MainView

# Create your tests here.

class MainViewTests(TestCase):
  def test_typed_request_get(self):
    x = MainView()
    data = {"page":"12","blab":"hello","nose":"13zz"}
    
    self.assertEqual(x.typed_request_get("page",1,accessor=data),12)
    self.assertEqual(x.typed_request_get("blab","blab",accessor=data),"hello")
    self.assertEqual(x.typed_request_get("nose","blab",accessor=data),"13zz")    
    
    self.assertEqual(x.typed_request_get("nose",43,accessor=data),43)
    self.assertEqual(x.typed_request_get("page","blab",accessor=data),"12")
    self.assertEqual(x.typed_request_get("globus","blab",accessor=data),"blab")
    self.assertEqual(x.typed_request_get("whatever",123,accessor=data),123)
    
  def test_make_pagination(self):
    x = MainView()
    self.assertEqual(x.make_pagination(1,0),{u'next_page': 2, u'has_next_page': False, u'prev_page': 0, u'has_prev_page': False})
    self.assertEqual(x.make_pagination(0,0),{u'next_page': 1, u'has_next_page': True, u'prev_page': -1, u'has_prev_page': False})
    self.assertEqual(x.make_pagination(10,0), {u'next_page': 11, u'has_next_page': False, u'prev_page': 9, u'has_prev_page': True})
    self.assertEqual(x.make_pagination(10,9),{u'next_page': 11, u'has_next_page': False, u'prev_page': 9, u'has_prev_page': True})
    
  @tag("api_call")  
  def test_getting_data_from_the_remote(self):
    # import pdb; pdb.set_trace()
    dat,isok = MainView().load_transaction_data()
    self.assertEqual(isok,True)
    
    datum,isok = MainView().load_transaction_data(app_token="whatever")
    self.assertEqual(isok,False)
    self.assertEqual(datum,{u'message': u'Auth Token is not valid', u'reason': u'BadAuthToken',
                            u'reason': 'Unauthorized',u'status_code': 401})
    
    
    




