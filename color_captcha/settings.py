# -*- coding: utf-8 -*-
from django.conf import settings
from utils import check_colors


DEFAULT_COLORS = [
    ('white', 'white'),
    ('blue', 'blue'),
    ('red', 'red'),
]

COLORS = getattr(settings, 'CAPTCHA_COLORS', DEFAULT_COLORS)

check_colors(COLORS)
