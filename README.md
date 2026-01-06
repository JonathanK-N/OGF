# OGF - Only God & Family 🎵

Site web officiel du label musical indépendant OGF, construit avec Flask, Tailwind CSS et GSAP.

## 🚀 Fonctionnalités

- **Design moderne et responsive** : Interface adaptée à tous les écrans
- **Animations fluides** : Utilisation de GSAP pour des transitions élégantes
- **Navigation intuitive** : Menu responsive avec animations
- **Pages complètes** :
  - Accueil avec hero section et carrousel
  - À propos avec timeline animée
  - Artistes avec effets hover
  - Projets musicaux avec filtres
  - Événements avec calendrier
  - Boutique e-commerce
  - Contact avec formulaire

## 🛠️ Technologies utilisées

- **Backend** : Python Flask 2.3.3
- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Styling** : Tailwind CSS (via CDN)
- **Animations** : GSAP 3.12.2 avec ScrollTrigger
- **Icons** : Font Awesome 6.4.0
- **Fonts** : Google Fonts (Oswald, Inter)

## 📁 Structure du projet

```
ogf_music_label/
├── app/
│   ├── templates/
│   │   ├── base.html          # Template de base
│   │   ├── index.html         # Page d'accueil
│   │   ├── about.html         # À propos
│   │   ├── artists.html       # Nos artistes
│   │   ├── projects.html      # Projets musicaux
│   │   ├── events.html        # Événements
│   │   ├── shop.html          # Boutique
│   │   └── contact.html       # Contact
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Styles personnalisés
│   │   ├── js/
│   │   │   └── main.js        # JavaScript principal
│   │   └── images/            # Images (placeholder)
│   └── __init__.py            # Application Flask
├── main.py                    # Point d'entrée
├── requirements.txt           # Dépendances Python
└── README.md                  # Documentation
```

## 🔧 Installation et lancement

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd ogf_music_label
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   
   # Sur Windows
   venv\Scripts\activate
   
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application**
   ```bash
   python main.py
   ```

5. **Accéder au site**
   Ouvrez votre navigateur et allez à : `http://localhost:5000`

## 🎨 Personnalisation

### Couleurs du thème
Les couleurs principales sont définies dans Tailwind CSS :
- `ogf-purple` : #8B5CF6 (Violet principal)
- `ogf-gold` : #F59E0B (Or/Jaune)
- `ogf-dark` : #1a1a1a (Noir principal)

### Modification du contenu
- **Données des artistes** : Modifiez le dictionnaire `artists_data` dans `app/__init__.py`
- **Projets musicaux** : Modifiez `projects_data` dans la même fonction
- **Événements** : Modifiez `events_data`
- **Produits boutique** : Modifiez `products_data`

### Images
Remplacez les images placeholder par vos propres images :
- Placez vos images dans `app/static/images/`
- Mettez à jour les URLs dans les templates HTML

## 🌟 Fonctionnalités avancées

### Animations GSAP
- Animations d'entrée au scroll
- Effets de parallaxe
- Transitions de page fluides
- Hover effects interactifs

### Responsive Design
- Mobile-first approach
- Breakpoints Tailwind CSS
- Menu mobile avec animations

### Performance
- Lazy loading des images
- Optimisation des animations
- Code JavaScript modulaire

## 🚀 Déploiement

### Déploiement local
Le site est prêt pour le développement local avec Flask en mode debug.

### Déploiement en production
Pour un déploiement en production, considérez :

1. **Serveur WSGI** (Gunicorn, uWSGI)
2. **Serveur web** (Nginx, Apache)
3. **Variables d'environnement** pour la configuration
4. **Base de données** (PostgreSQL, MySQL) si nécessaire

Exemple avec Gunicorn :
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

## 📝 Développement

### Ajouter une nouvelle page
1. Créer le template HTML dans `app/templates/`
2. Ajouter la route dans `app/__init__.py`
3. Mettre à jour la navigation dans `base.html`

### Ajouter des animations
Utilisez GSAP dans vos templates :
```javascript
gsap.from(".mon-element", {
    y: 50,
    opacity: 0,
    duration: 1,
    ease: "power2.out"
});
```

## 🎵 Contenu par défaut

Le site inclut du contenu de démonstration :
- **3 artistes** : MC Divine, Soul Sister, Young Prophet
- **3 projets** : Faith & Family, Blessed Vibes, New Generation
- **3 événements** : OGF Live Session, Concert Spirituel, Festival Hip-Hop
- **4 produits** : T-shirts, casquettes, hoodies, vinyles

## 🤝 Contribution

Pour contribuer au projet :
1. Fork le repository
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 📞 Support

Pour toute question ou support :
- Email : contact@ogf-music.com
- Site web : [OGF Music Label](http://localhost:5000)

---

**OGF - Only God & Family** 🙏
*Label musical indépendant prônant les valeurs spirituelles et familiales*