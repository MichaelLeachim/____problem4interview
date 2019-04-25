# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-04-25 18:32 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals

from django.apps import AppConfig

class CoingateConfig(AppConfig):
  name = 'coingate'
  payment_button_link = 'https://coingate.com/pay/name_id_of_test_button'
  api_key_v2 = '**********************'
  api_key_v1 = '**********************'
  api_secret_v1 = '********************'
