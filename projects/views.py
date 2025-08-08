# projects/views.py
from django.shortcuts import render

def project_list(request):
    """List all SGCX projects"""
    # Research projects
    research_projects = [
        {
            'name': 'Project Lacuna',
            'tagline': 'Neural Networks for Missing Data Mechanism Detection',
            'description': 'Revolutionary tool for distinguishing between MAR and MNAR mechanisms',
            'status': 'Active Development',
            'url_name': 'projects:lacuna'
        },
        {
            'name': 'Project Blacklight',
            'tagline': 'Revealing true optimizer performance',
            'description': 'Quantify how close optimizers actually get to global minima',
            'status': 'Research Phase',
            'url_name': 'projects:blacklight'
        },
        {
            'name': 'GradFlow',
            'tagline': 'GPU-Accelerated WENO Implementation',
            'description': 'Modern PyTorch implementation of WENO schemes using convolution operations',
            'status': 'Early Development',
            'url_name': 'projects:gradflow'
        },
        {
            'name': 'AFL Research',
            'tagline': 'Approximate Forgiveness Level in Neural Networks',
            'description': 'Discovery that random pruning improves performance up to 70-80% sparsity',
            'status': 'Significant Results',
            'url_name': 'projects:afl'
        },
        {
            'name': 'Project Bonsai',
            'tagline': 'Statistics-Informed Neural Network Pruning',
            'description': 'FANIM-based pruning with Wilcoxon statistical testing',
            'status': 'On Hold',
            'url_name': 'projects:bonsai'
        }
    ]
    
    # Interface projects (future subdomains)
    interface_projects = [
        {
            'name': 'SGC-Clinical',
            'tagline': 'Statistical tools for clinical research',
            'description': 'Drag-and-drop clinical trial analysis with no coding required - upload data, configure analysis, download FDA-ready results',
            'status': 'Planned',
            'url_name': 'projects:clinical'
        },
        {
            'name': 'SGC-Pharma',
            'tagline': 'Pharmaceutical statistical analysis',
            'description': 'No-code pharmaceutical statistical analysis with built-in regulatory compliance and automated FDA submission reports',
            'status': 'Planned', 
            'url_name': 'projects:pharma'
        },
        {
            'name': 'SGC-Finance',
            'tagline': 'Financial modeling and risk analysis',
            'description': 'Point-and-click financial risk modeling and portfolio analysis - no programming, just upload data and get professional reports',
            'status': 'Planned',
            'url_name': 'projects:finance'
        },
        {
            'name': 'SGC-Insurance',
            'tagline': 'Insurance analytics and risk modeling',
            'description': 'Intuitive actuarial analysis interface - drag-and-drop claims data for reserving, pricing, and regulatory reporting',
            'status': 'Planned',
            'url_name': 'projects:insurance'
        }
    ]
    
    context = {
        'page_title': 'Projects - SGCX',
        'meta_description': 'Explore SGCX research projects and statistical AI tools',
        'research_projects': research_projects,
        'interface_projects': interface_projects,
    }
    return render(request, 'projects/project_list.html', context)

def lacuna(request):
    """Project Lacuna detail page"""
    context = {
        'page_title': 'Project Lacuna - SGCX',
        'meta_description': 'Neural Networks for Missing Data Mechanism Detection',
    }
    return render(request, 'projects/lacuna.html', context)

def blacklight(request):
    """Project Blacklight detail page"""
    context = {
        'page_title': 'Project Blacklight - SGCX',
        'meta_description': 'Revealing true optimizer performance against known global minima',
    }
    return render(request, 'projects/blacklight.html', context)

def gradflow(request):
    """GradFlow detail page"""
    context = {
        'page_title': 'GradFlow - SGCX',
        'meta_description': 'GPU-Accelerated WENO Implementation using PyTorch',
    }
    return render(request, 'projects/gradflow.html', context)

def afl(request):
    """AFL Research detail page"""
    context = {
        'page_title': 'AFL Research - SGCX',
        'meta_description': 'Approximate Forgiveness Level in Neural Networks',
    }
    return render(request, 'projects/afl.html', context)

def bonsai(request):
    """Project Bonsai detail page"""
    context = {
        'page_title': 'Project Bonsai - SGCX',
        'meta_description': 'Statistics-Informed Neural Network Pruning',
    }
    return render(request, 'projects/bonsai.html', context)

def clinical(request):
    """Clinical Interface detail page"""
    context = {
        'page_title': 'Clinical Interface - SGCX',
        'meta_description': 'Statistical tools for clinical research and biostatistics',
    }
    return render(request, 'projects/clinical.html', context)

def pharma(request):
    """Pharma Interface detail page"""
    context = {
        'page_title': 'Pharma Interface - SGCX',
        'meta_description': 'Pharmaceutical statistical analysis and regulatory compliance',
    }
    return render(request, 'projects/pharma.html', context)

def finance(request):
    """Finance Interface detail page"""
    context = {
        'page_title': 'Finance Interface - SGCX',
        'meta_description': 'Financial modeling and risk analysis tools',
    }
    return render(request, 'projects/finance.html', context)

def insurance(request):
    """Insurance Interface detail page"""
    context = {
        'page_title': 'Insurance Interface - SGCX',
        'meta_description': 'Insurance analytics and actuarial modeling tools',
    }
    return render(request, 'projects/insurance.html', context)