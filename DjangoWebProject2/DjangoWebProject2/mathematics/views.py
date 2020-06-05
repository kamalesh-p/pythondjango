"""
Definition of mathematics/views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import Mathematics as Ms

def mhome(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mhome.html',
        {
            'title':"Mathematics"
        }
    )

def mtopic(request):
    """Renders the topic page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mtopic.html',
        {
            'title':"Topics",
        }
    )

def mcomment(request):
    """Renders the comment page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mcomment.html',
        {
            'title':"Comment"
        }
    )

def mproblem(request):
    """Renders the problem page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mproblem.html',
        {
            'title':"Solution",
            'question':"",
            'answer':"",
            'formula':"",
            'base':"",
            'solution':"",
            'result':"",
        }
     )

def mdisplay(request):
    """Renders the display page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mdisplay.html',
        {
            'title':"Display"
        }
    )

def mprogramming(request):
    """Renders the programming page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mprogramming.html',
        {
            'title':"Programming"
        }
    )

def mgraphics(request):
    """Renders the graphics page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mgraphics.html',
        {
            'title':"Graphics"
        }
    )