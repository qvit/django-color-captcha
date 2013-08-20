# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from hashlib import sha1
from settings import DEFAULT_ERROR_MESSAGES, ERROR_MESSAGES
from widgets import ColorCaptchaWidget

DEFAULT_ERROR_MESSAGES.update(ERROR_MESSAGES)

class ColorCaptchaField(forms.MultiValueField):

    default_error_messages = DEFAULT_ERROR_MESSAGES
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
