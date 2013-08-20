Django Color Captcha
====================

Quick Start
^^^^^^^^^^^

Add ``color_captcha`` to INSTALLED_APPS ::

    INSTALLED_APPS = [
        ...
        'color_captcha',
        ...
    ]

Run ``collectstatic`` manage command ::

    > python manage.py collectstatic

Add ``color_captcha.css`` file to your template ::

    <link rel="stylesheet" href="{{ STATIC_URL }}color_captcha/css/color_captcha.css" type="text/css"/>

Add ``ColorCaptchaField`` into your form ::

    from django import forms
    from color_captcha.fields import ColorCaptchaField


    class MyForm(forms.Form)
        ...
        captcha = ColorCaptchaField(label='Choose a color')
        ...

Configuration
^^^^^^^^^^^^^

Feel free to configure your captcha with the following options.

**CAPTCHA_COLORS**

    Default: ::

        [
            ('white', 'white'),
            ('blue', 'blue'),
            ('red', 'red'),
        ]

    An iterable of two-string-value tuples. The first value in tuple is a HEX color code (e.g. ``#FFF``) or css color constant (e.g. ``white``). The second value is a color name for user who has to solve the captcha.

**CAPTCHA_ERROR_MESSAGES**

    Default: ::

        {
            'wrong': 'Wrong answer',
            'required': 'This field is required',
            'internal': 'Internal error',
        }

    A dictionary with error messages for captcha field. You can override any of them.
