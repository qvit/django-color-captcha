# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from utils import check_colors


DEFAULT_COLORS = [
    ('white', 'white'),
    ('blue', 'blue'),
    ('red', 'red'),
]

COLORS = getattr(settings, 'CAPTCHA_COLORS', DEFAULT_COLORS)

check_colors(COLORS)

DEFAULT_ERROR_MESSAGES = {
    'wrong': _('Wrong answer'),
    'required': _('This field is required'),
    'internal': _('Internal error'),
}

ERROR_MESSAGES = getattr(settings, 'CAPTCHA_ERROR_MESSAGES', DEFAULT_ERROR_MESSAGES)
