# SGCX Website

The official website for SGCX Research Organization - pioneering human-AI collaboration to solve fundamental problems in statistics and data science.

🌐 **Live Site**: [sgcx.org](https://sgcx.org)  
📧 **Contact**: contact@sgcx.org  
📚 **Research**: [sgcx.org/research](https://sgcx.org/research)

## About SGCX

SGCX is a statistical AI research organization that tackles long-standing problems in statistical methodology through transparent human-AI collaboration. Our name reflects our collaborative approach:

- **S** - Hai-Shuo **S**hu (Human researcher and visionary)
- **G** - Chat**G**PT (AI collaborator) 
- **C** - **C**laude (AI collaborator)
- **X** - E**X**cellerator (The breakthrough element)

### Research Areas

- **Missing Data Analysis**: Distinguishing between MAR and MNAR mechanisms using neural networks
- **Optimizer Performance**: Revealing true optimizer performance against known global minima
- **Computational Statistics**: GPU-native statistical libraries and modern implementations
- **Human-AI Collaboration**: Developing frameworks for transparent AI-assisted research

## Current Projects

### 🔬 Project Lacuna
**Neural Networks for Missing Data Mechanism Detection**
- Transformer-based architecture for missingness pattern recognition
- Addresses critical gap in pharmaceutical, financial, and insurance research
- Status: Active development, early access available

### 🔦 Project Blacklight  
**Revealing True Optimizer Performance**
- Systematic evaluation of ML optimizers against known global minima
- Statistical rigor with 20-50 runs per optimizer configuration
- Status: Research phase

## Technical Stack

- **Framework**: Django 5.2
- **Deployment**: Heroku (ertihan app)
- **Static Files**: WhiteNoise
- **Database**: SQLite (dev), PostgreSQL (production)
- **Domain**: sgcx.org via Namecheap → Heroku

## Development Setup

### Prerequisites
- Python 3.11+
- Conda (recommended) or pip

### Quick Start

```bash
# Clone the repository
git clone https://github.com/haishuo/sgcx.git
cd sgcx

# Create conda environment (recommended)
conda create -n sgcx python=3.11
conda activate sgcx

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the site locally.

### Project Structure

```
sgcx/
├── landing/              # Main landing page app
├── projects/             # Project showcase pages
├── sgcx_site/           # Django project settings
├── branding/            # Logo assets and brand materials
├── static/              # CSS, images, and static assets
└── requirements.txt     # Python dependencies
```

## Deployment

This site is deployed to Heroku and accessible at [sgcx.org](https://sgcx.org).

### Deployment Process
1. Push to `main` branch
2. Heroku automatically builds and deploys
3. Static files served via WhiteNoise
4. SSL handled automatically by Heroku

### Environment Variables
- `DJANGO_SETTINGS_MODULE`: Production settings
- `SECRET_KEY`: Django secret key (production)

## Related Repositories

- **[haishuo/lacuna](https://github.com/haishuo/lacuna)** - Project Lacuna implementation
- **[haishuo/sgcx-blacklight](https://github.com/haishuo/sgcx-blacklight)** - Project Blacklight research
- **PyMVNMLE** - Maximum likelihood estimation library (planned)
- **PyRegression** - GPU-accelerated regression library (planned)

## Subdomain Strategy

Each SGCX project gets its own subdomain:
- `lacuna.sgcx.org` - Project Lacuna
- `blacklight.sgcx.org` - Project Blacklight  
- `clinical.sgcx.org` - Clinical interface (planned)
- `pharma.sgcx.org` - Pharmaceutical interface (planned)
- `finance.sgcx.org` - Financial modeling interface (planned)

## Research Philosophy

We believe in:
- **Transparency**: Open about AI assistance in research
- **Rigor**: Maintaining statistical standards while embracing innovation  
- **Reproducibility**: All methods designed for validation and extension
- **Impact**: Focus on problems that matter to real research

## Contributing

SGCX is currently a research organization led by Hai-Shuo Shu with AI collaboration. For research collaboration opportunities, please contact us at research@sgcx.org.

## License

This website and its content represent proprietary work of SGCX Research Organization. While we believe in open research methodologies, the specific implementation of this website is not licensed for reuse.

---

**SGCX Research Organization**  
*Building the future of statistical AI through human-AI collaboration*