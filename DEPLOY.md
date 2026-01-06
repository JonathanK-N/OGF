# Déploiement Railway - OGF Music Label

## 🚀 Instructions de déploiement

### 1. Préparer le repository Git
```bash
cd ogf_music_label
git init
git add .
git commit -m "Initial commit - OGF Music Label"
```

### 2. Pousser sur GitHub (optionnel mais recommandé)
```bash
# Créer un repo sur GitHub puis :
git remote add origin https://github.com/votre-username/ogf-music-label.git
git branch -M main
git push -u origin main
```

### 3. Déployer sur Railway

#### Option A : Via GitHub
1. Aller sur [railway.app](https://railway.app)
2. Se connecter avec GitHub
3. Cliquer "New Project" → "Deploy from GitHub repo"
4. Sélectionner votre repository
5. Railway détectera automatiquement Flask

#### Option B : Via Railway CLI
```bash
# Installer Railway CLI
npm install -g @railway/cli

# Se connecter
railway login

# Déployer
railway deploy
```

### 4. Variables d'environnement (optionnel)
Dans Railway Dashboard → Variables :
- `SECRET_KEY` : votre-clé-secrète-forte
- `FLASK_DEBUG` : false

## 📁 Fichiers de déploiement créés

- ✅ `Procfile` - Commande de démarrage
- ✅ `requirements.txt` - Dépendances Python (avec Gunicorn)
- ✅ `runtime.txt` - Version Python
- ✅ `.gitignore` - Fichiers à ignorer
- ✅ `main.py` - Modifié pour Railway (PORT dynamique)

## 🌐 Après déploiement

Votre site sera accessible à : `https://votre-app.railway.app`

Railway fournira automatiquement :
- HTTPS
- Domaine personnalisé
- Déploiement automatique sur push Git
- Logs en temps réel

## 🔧 Configuration automatique

Railway détecte automatiquement :
- Python/Flask app
- Port dynamique via `$PORT`
- Build et start commands
- Dépendances via requirements.txt