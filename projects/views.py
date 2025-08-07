# projects/views.py
from django.shortcuts import render

def project_list(request):
    """List all SGCX projects"""
    projects = [
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
        }
    ]
    
    context = {
        'page_title': 'Projects - SGCX',
        'meta_description': 'Explore SGCX research projects and statistical AI tools',
        'projects': projects,
    }
    return render(request, 'projects/project_list.html', context)

def lacuna(request):
    """Project Lacuna detail page"""
    context = {
        'page_title': 'Project Lacuna - SGCX',
        'meta_description': 'Neural Networks for Missing Data Mechanism Detection',
        'project': {
            'name': 'Project Lacuna',
            'tagline': 'Neural Networks for Missing Data Mechanism Detection',
            'description': '''Project Lacuna addresses a critical gap in statistical practice: 
                           the ability to distinguish between Missing at Random (MAR) and 
                           Missing Not at Random (MNAR) mechanisms.''',
            'technology': 'Transformer-based architecture with attention mechanisms',
            'impact': 'Revolutionary tool for pharmaceutical research, biostatistics, financial modeling',
            'status': 'Proof of concept completed, scaling phase planned'
        }
    }
    return render(request, 'projects/lacuna.html', context)

def blacklight(request):
    """Project Blacklight detail page"""
    context = {
        'page_title': 'Project Blacklight - SGCX',
        'meta_description': 'Revealing true optimizer performance against known global minima',
        'project': {
            'name': 'Project Blacklight',
            'tagline': 'Revealing true optimizer performance',
            'description': '''Generate toy neural networks small enough to find global minimum, 
                           then test various optimizers with statistical rigor.''',
            'methodology': 'Minimum 20-50 runs per optimizer with full statistical analysis',
            'impact': 'Quantify how close optimizers actually get to true optimum vs marketing claims',
            'status': 'Conceptual phase'
        }
    }
    return render(request, 'projects/blacklight.html', context)