import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FirstNameValidator(validators.RegexValidator):
    regex = r"[a-zA-z]+$"
    message = _(
        "Enter your first name here."
    )
    flags = 0


@deconstructible
class LastNameValidator(validators.RegexValidator):
    regex = r"[a-zA-z]+$"
    message = _(
        "Enter your last name here."
    )
    flags = 0


@deconstructible
class EmailValidator(validators.RegexValidator):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    message = _(
        "Enter your email here. It should contain @ and in the end .com/.ro etc."
    )
    flags = 0
