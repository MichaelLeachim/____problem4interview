# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-04-25 09:56 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json
from django.conf import settings

from .apps import CoingateConfig

class MainView(TemplateView):
  template_name = "main.html"
  
  def typed_request_get(self,param,default,accessor=None):
    """
    will work only on int/string for now
    will request.Get.get results in type provided by default
    if cannot convert, will return default
    """
    if accessor == None:
      accessor = self.request.GET
      
    if type(default) == str or type(default) == unicode:
      return accessor.get(param, default)
    
    if type(default) == int:
      z = accessor.get(param, default)
      if z == str(default):
        return default
      try:
        return int(z,10)
      except:
        return default
      
    return default
  
  def load_transaction_data(self,page=1,sort="created_at_desc",per_page=100,app_token=CoingateConfig.api_key_v2):
    
    resp = requests.get("https://api.coingate.com/v2/orders",
                        headers = {"Authorization":"Token "+app_token},
                        data = {"per_page":per_page,"sort":sort,"page":page})
    
    if resp.ok:
      return resp.json(),resp.ok
    d = resp.json()
    d["reason"] = resp.reason
    d["status_code"] = resp.status_code
    return d,False
  
  def make_pagination(self,current_page,total_pages):
    prev_page,next_page = current_page - 1,current_page + 1
    has_prev_page,has_next_page = True,True
    if prev_page <= 0:
      has_prev_page = False
    if next_page - total_pages > 1:
      has_next_page = False
    return {
      "prev_page":prev_page,
      "next_page":next_page,
      "has_prev_page":has_prev_page,
      "has_next_page":has_next_page,
    }
    
  def get_context_data(self, **kwargs):
    # import pdb; pdb.set_trace()
    context = super(MainView, self).get_context_data(**kwargs)
    
    context["seo_description"] = _(u"This web site is a test task")
    context["seo_title"] =      _(u"Test task")
    context["host"] = _("example.com")
    
    context["payment_button_link"] = CoingateConfig.payment_button_link
    
    if CoingateConfig.use_fixtures:
      ok = True
      with open(settings.BASE_DIR+"/coingate/fixtures/sampledata.json","r") as f:
        trans_data = json.loads(f.read())
    else:
      trans_data,ok = self.load_transaction_data(page = self.typed_request_get('page',1,accessor=self.request.GET,),
                                                 sort = self.typed_request_get('sort','created_at_desc',accessor=self.request.GET,),
                                                 per_page = self.typed_request_get('per_page',2,accessor=self.request.GET,))
      
    if ok:
      context["pagination"] = self.make_pagination(trans_data["current_page"],trans_data["total_pages"])
      context["transdata"] = trans_data
      
    if not ok:
      context["transdata_error"] = trans_data
    return context  
