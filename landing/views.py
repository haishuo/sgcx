# landing/views.py
from django.shortcuts import render

def home(request):
    """Main landing page for SGCX"""
    context = {
        'page_title': 'SGCX - Statistical AI Research Organization',
        'meta_description': 'Pioneering human-AI collaboration to solve fundamental problems in statistics and data science',
    }
    return render(request, 'landing/home.html', context)

def about(request):
    """About page with detailed SGCX information"""
    context = {
        'page_title': 'About SGCX',
        'meta_description': 'Learn about SGCX\'s mission, approach, and team',
    }
    return render(request, 'landing/about.html', context)

def research(request):
    """Research publications and methodology"""
    context = {
        'page_title': 'Research - SGCX',
        'meta_description': 'SGCX research publications and statistical methodology',
    }
    return render(request, 'landing/research.html', context)

def contact(request):
    """Contact information and forms"""
    context = {
        'page_title': 'Contact - SGCX',
        'meta_description': 'Get in touch with the SGCX research team',
    }
    return render(request, 'landing/contact.html', context)