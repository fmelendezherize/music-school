# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Department, Instrument

# Register your models here.
admin.site.register(Department)
admin.site.register(Instrument)