# -*- coding: utf-8 -*-

from django.db import models
from django import forms

class Subscription(models.Model):
    name = models.CharField('Nome',max_length=100)
    cpf = models.CharField('CPF',max_length=11, unique=True)
    email = models.EmailField('Email',unique=True)
    phone = models.CharField('Telefone',max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


