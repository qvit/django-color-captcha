# -*- coding: utf-8 -*-
from django import forms
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _
from hashlib import sha1
from random import choice
from settings import COLORS


__version__ = '0.1.0'


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


class ColorCaptchaField(forms.MultiValueField):

    default_error_messages = {
        'wrong': _('Wrong answer'),
        'required': _('This field is required'),
        'internal': _('Internal error'),
    }
    widget = ColorCaptchaWidget()

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.ChoiceField()
        )
        super(ColorCaptchaField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if len(data_list) < 2:
            return None
        else:
            return reduce(lambda x, y: x == sha1(y).hexdigest(), data_list)

    def clean(self, value):
        color, chosen = value
        if chosen is None:
            raise forms.ValidationError, self.error_messages['required']
        chosen = sha1(chosen).hexdigest()
        if not color == chosen:
            raise forms.ValidationError, self.error_messages['wrong']
