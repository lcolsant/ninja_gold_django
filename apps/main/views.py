# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        print "Gold count: ",request.session['total_gold']
    if 'new_gold' not in request.session:
        request.session['new_gold'] = 0
    if 'building' not in request.session:
        request.session['building'] = ""
    if 'history' not in request.session:
        request.session['history'] = []
    if 'length' not in request.session:
        request.session['length'] = 0
    return render(request,'main/index.html')

def process_money(request):
    print 'got here'
    if request.POST['building'] == 'farm':
        request.session['new_gold'] = random.randrange(10, 21)
        print "Found new farm gold: ",request.session['new_gold']
        request.session['total_gold']+=request.session['new_gold']
    elif request.POST['building'] == 'cave':
        request.session['new_gold'] = random.randrange(5, 11)
        print "Found new cave gold: ",request.session['new_gold']
        request.session['total_gold']+=request.session['new_gold']
    elif request.POST['building'] == 'house':
        request.session['new_gold'] = random.randrange(2, 6)
        print "Found new house gold: ",request.session['new_gold']
        request.session['total_gold']+=request.session['new_gold']
    elif request.POST['building'] == 'casino':
        request.session['new_gold'] = random.randrange(-50, 51)
        print "Found new casino gold: ",request.session['new_gold']
        request.session['total_gold']+= request.session['new_gold']
        if request.session['total_gold'] < 0:
            request.session['total_gold'] = 0

    print "Session total_gold is now:", request.session['total_gold']
    
    turn = {
        'new_gold':request.session['new_gold'],
        'building':request.session['building'],
        'time':datetime.datetime.now().strftime("%m/%d/%Y %H:%M"), 
    }
    
    
    request.session['history'].append(turn)
    request.session.modified = True
    print request.session['history']
    request.session['length'] = len(request.session['history'])

    return redirect('/')

def reset(request):
    del request.session['total_gold']
    del request.session['new_gold']
    del request.session['history']
    return redirect('/')

