# -*- coding: utf-8 -*-
class IncorrectCaptchaColorsFormatError(Exception):

    message = "Incorrect 'CAPTCHA_COLORS' setting format (must be iterable of two-string-value tuples)"

    def __str__(self):
        return self.message


class TooFewCaptchaColorsError(Exception):

    message = "Please specify al least two colors in 'CAPTCHA_COLORS' setting"

    def __str__(self):
        return self.message


def check_colors(COLORS):

    def check_color_option(color_option):
        try:
            if not (len(color_option) == 2 and
                    isinstance(color_option[0], basestring) and
                    isinstance(color_option[1], basestring)):
                raise IncorrectCaptchaColorsFormatError()
        except IndexError:
            raise IncorrectCaptchaColorsFormatError()

    try:
        iter(COLORS)
    except TypeError:
        raise IncorrectCaptchaColorsFormatError()
    else:
        if len(COLORS) < 2:
            raise TooFewCaptchaColorsError()
        else:
            for color_option in COLORS:
                check_color_option(color_option)
