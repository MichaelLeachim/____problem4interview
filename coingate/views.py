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

from .apps import CoingateConfig

class MainView(TemplateView):
  template_name = "main.html"
  def load_transaction_data(self,page=1,sort="created_at_desc",per_page=100,app_token=CoingateConfig.api_key_v2):
    resp = requests.get("https://api.coingate.com/v2/orders",
                        headers={"Authorization":"Token "+app_token},
                        data={"per_page":per_page,"sort":sort,"page":page})
    if resp.ok:
      return resp.json(),resp.ok
    d = resp.json()
    d["reason"] = resp.reason
    d["status_code"] = resp.status_code
    return d,False
  
  def get_context_data(self, **kwargs):
    context = super(MainView, self).get_context_data(**kwargs)
    context["seo_description"] = _(u"This web site is a test task")
    context["seo_title"] =      _(u"Test task")
    context["host"] = _("example.com")
    context["appconf"] = CoingateConfig
