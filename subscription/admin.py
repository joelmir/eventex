#-*- coding: utf-8 -*-

#import datetime
from django.contrib import admin
#from django.utils.translation import ugettext as _
#from django.utils.translation import ungettext

#from django.conf.urls.defaults import patterns, url
#from django.http import HttpResponse

from subscription.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'email', 'phone', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    
    

admin.site.register(Subscription, SubscriptionAdmin)

