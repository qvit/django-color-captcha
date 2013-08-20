# -*- coding: utf-8 -*-
from django import forms
from django.template import Context
from django.template.loader import get_template
from hashlib import sha1
from random import choice
from settings import COLORS


def get_color_option():
    try:
        return choice(COLORS)
    except IndexError:
        return None


class ColorCaptchaWidget(forms.MultiWidget):

    template = 'color_captcha/widget.html'

    def __init__(self, attrs={}):
        widgets = (
            forms.HiddenInput(attrs=attrs),
            forms.RadioSelect(attrs=attrs, choices=COLORS)
        )
        super(ColorCaptchaWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split()
        return []

    def render(self, name, value, attrs=None):
        color_option = get_color_option()
        color_hash = sha1(color_option[0]).hexdigest()
        return get_template(self.template).render(Context({
            'name': name,
            'colors': COLORS,
            'color_option': color_option,
            'hash': color_hash
        }))
