# encoding: utf-8

from datetime import datetime, timedelta
from functools import wraps
from itertools import groupby
from random import randint
import json
import sys
import re

from django import forms
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.http import urlencode
from django.utils.timezone import now
from django.template import RequestContext
from django.template.loader import render_to_string

from dateutil.tz import tzlocal

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Hidden




validate_slug = RegexValidator(
    regex=r'[a-z0-9-]+',
    message=u'Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.'
)


SLUG_FIELD_PARAMS = dict(
    max_length=63,
    unique=True,
    validators=[validate_slug],
    verbose_name=u'Tekninen nimi',
    help_text=u'Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja '
        u'merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi '
        u'muuttaa luomisen jälkeen.',
)
NONUNIQUE_SLUG_FIELD_PARAMS = dict(SLUG_FIELD_PARAMS, unique=False)