# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-04-25 10:11 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from django.conf.urls import url
from .views import MainView

urlpatterns = [
   url("^$",MainView.as_view(),name="main"),
]


    
     
     



