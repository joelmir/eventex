# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from subscription.models import Subscription
from subscription.forms import SubscriptionForm


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)
    subscription = form.save()
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)


