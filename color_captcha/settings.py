# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from utils import check_colors


DEFAULT_COLORS = [
    (u'white', _('white')),
    (u'blue', _('blue')),
    (u'red', _('red')),
]

COLORS = getattr(settings, 'CAPTCHA_COLORS', DEFAULT_COLORS)

check_colors(COLORS)
