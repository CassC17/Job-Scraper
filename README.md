# Job-Scraper
Web scraper pour les offres d'emplois du site [LesJeudis.com](https://www.lesjeudis.com/).

## Fonctionnalités
- Scrape les 5 premières pages d'offres d'emploi.
- Récupère : titre, lieu, type de contrat, date de publication et le lien.
( manque: l'entreprise, description courte et précise)
- Stocke les données dans :
  - Un fichier JSON (`jobs.json`)

## Technologies utilisées

- [Python 3.13.2](https://www.python.org/)
- [Scrapy](https://scrapy.org/)

## Installation
# Cloner le projet
git clone https://github.com/votre-utilisateur/job_scraper.git
```cd job_scraper```

# Créer l'environnement conda
```conda create -n job_scraper python=3.11```
```conda activate job_scraper```

# Installer les dépendances
```pip install -r requirements.txt```

# Lancer le scraping et exporter en JSON (automatiquement voir settings.py)
```scrapy crawl jobs```

# Structure du projet
job_scraper/
├── scrapy.cfg
├── job_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       └── jobs.py
├── jobs.json
├── requirements.txt
└── README.md
