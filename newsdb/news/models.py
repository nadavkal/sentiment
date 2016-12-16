from __future__ import unicode_literals

from django.db import models

from AppConfigs import CURRENCY
from utils import kmb_converter


# Create your models here.

class Stocks(models.Model):
    symbol = models.CharField(max_length=8, null=False, blank=False)
    name = models.CharField(max_length=80, null=True, blank=True)
    lastsale = models.CharField(max_length=20, null=True, blank=True)
    marketcap = models.CharField(max_length=20, null=True, blank=True)
    ipoyear = models.CharField(max_length=10, null=True, blank=True)
    sector = models.CharField(max_length=30, null=True, blank=True)
    industry = models.CharField(max_length=40, null=True, blank=True)
    summary_quate = models.URLField()


class Ticker(models.Model):
    symbol = models.CharField(max_length=8, null=False,blank=False)
    begin = models.DateField(auto_now=False, null=True)
    end = models.DateField(auto_now=False, null=False)
    last_updated = models.DateField(auto_now=False, null=False)
    company_name = models.CharField(max_length=200)


class NewsSummary(models.Model):
    ticker = models.ForeignKey('Ticker')
    date = models.DateField(auto_now=True, null=False)
    time = models.TimeField(auto_now=True, null=True)
    text = models.TextField(null=False, blank=False)
    source = models.CharField(max_length=80, null=True, blank=True)
    link = models.URLField()


class News(models.Model):
    ticker = models.ForeignKey('Ticker')
    date = models.DateField(auto_now=True, null=False)
    time = models.TimeField(auto_now=True, null=True)
    text = models.TextField(null=False, blank=False)
    source = models.CharField(max_length=80, null=True, blank=True)
    summary = models.ForeignKey('NewsSummary', null=True, blank=True)


class Feature(models.Model):
    ticker = models.ForeignKey('Ticker')
    last_updated = models.DateField(auto_now=True, null=False)
    feature_name = models.CharField(max_length=80, null=False, blank=False)
    value = models.CharField(max_length=80, null=False, blank=False)
    cur = [(c, c) for c in CURRENCY]
    currency = models.CharField(choices=cur, max_length=20, null=True, blank=True)

    def numeric_value(self):
        return kmb_converter(self.value)

    def text_value(self):
        return unicode(self.value).encode('utf-8')
