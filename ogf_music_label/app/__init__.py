from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'ogf-music-label-secret-key'
    
    # Routes
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/artists')
    def artists():
        artists_data = [
            {
                'name': 'MC Divine',
                'genre': 'Rap Conscient',
                'image': 'https://via.placeholder.com/300x300/1a1a1a/ffffff?text=MC+Divine',
                'bio': 'Artiste principal du label, prône les valeurs familiales et spirituelles.',
                'social': {'instagram': '#', 'spotify': '#', 'youtube': '#'}
            },
            {
                'name': 'Soul Sister',
                'genre': 'R&B Gospel',
                'image': 'https://via.placeholder.com/300x300/1a1a1a/ffffff?text=Soul+Sister',
                'bio': 'Voix puissante et messages inspirants, ambassadrice de la foi.',
                'social': {'instagram': '#', 'spotify': '#', 'youtube': '#'}
            },
            {
                'name': 'Young Prophet',
                'genre': 'Hip-Hop Spirituel',
                'image': 'https://via.placeholder.com/300x300/1a1a1a/ffffff?text=Young+Prophet',
                'bio': 'Jeune talent émergent, porte-parole de sa génération.',
                'social': {'instagram': '#', 'spotify': '#', 'youtube': '#'}
            }
        ]
        return render_template('artists.html', artists=artists_data)
    
    @app.route('/projects')
    def projects():
        projects_data = [
            {
                'title': 'Faith & Family',
                'artist': 'MC Divine',
                'type': 'Album',
                'cover': 'https://via.placeholder.com/300x300/8B5CF6/ffffff?text=Faith+%26+Family',
                'description': 'Premier album du label, mélange de rap conscient et de spiritualité.',
                'links': {'spotify': '#', 'apple': '#', 'youtube': '#'}
            },
            {
                'title': 'Blessed Vibes',
                'artist': 'Soul Sister',
                'type': 'EP',
                'cover': 'https://via.placeholder.com/300x300/F59E0B/ffffff?text=Blessed+Vibes',
                'description': 'EP de 6 titres R&B gospel, messages d\'espoir et de foi.',
                'links': {'spotify': '#', 'apple': '#', 'youtube': '#'}
            },
            {
                'title': 'New Generation',
                'artist': 'Young Prophet',
                'type': 'Single',
                'cover': 'https://via.placeholder.com/300x300/EF4444/ffffff?text=New+Generation',
                'description': 'Single percutant sur les défis de la jeunesse moderne.',
                'links': {'spotify': '#', 'apple': '#', 'youtube': '#'}
            }
        ]
        return render_template('projects.html', projects=projects_data)
    
    @app.route('/events')
    def events():
        events_data = [
            {
                'title': 'OGF Live Session',
                'date': '15 Mars 2024',
                'location': 'Studio OGF, Paris',
                'description': 'Session live exclusive avec tous les artistes du label.',
                'image': 'https://via.placeholder.com/400x200/8B5CF6/ffffff?text=OGF+Live'
            },
            {
                'title': 'Concert Spirituel',
                'date': '22 Avril 2024',
                'location': 'Église Saint-Martin, Lyon',
                'description': 'Concert caritatif avec Soul Sister et MC Divine.',
                'image': 'https://via.placeholder.com/400x200/F59E0B/ffffff?text=Concert+Spirituel'
            },
            {
                'title': 'Festival Hip-Hop Conscient',
                'date': '10 Juin 2024',
                'location': 'Parc de la Villette, Paris',
                'description': 'Participation au plus grand festival de hip-hop conscient.',
                'image': 'https://via.placeholder.com/400x200/EF4444/ffffff?text=Festival+Hip-Hop'
            }
        ]
        return render_template('events.html', events=events_data)
    
    @app.route('/shop')
    def shop():
        products_data = [
            {
                'name': 'T-Shirt OGF Classic',
                'price': '25€',
                'image': 'https://via.placeholder.com/300x300/1a1a1a/ffffff?text=T-Shirt+OGF',
                'description': 'T-shirt noir avec logo OGF brodé, 100% coton bio.'
            },
            {
                'name': 'Casquette Snapback',
                'price': '30€',
                'image': 'https://via.placeholder.com/300x300/8B5CF6/ffffff?text=Casquette+OGF',
                'description': 'Casquette snapback violette avec broderie "Only God & Family".'
            },
            {
                'name': 'Hoodie Premium',
                'price': '55€',
                'image': 'https://via.placeholder.com/300x300/F59E0B/ffffff?text=Hoodie+OGF',
                'description': 'Sweat à capuche premium, design exclusif du label.'
            },
            {
                'name': 'Vinyl Faith & Family',
                'price': '35€',
                'image': 'https://via.placeholder.com/300x300/EF4444/ffffff?text=Vinyl+Album',
                'description': 'Album "Faith & Family" en édition limitée vinyle.'
            }
        ]
        return render_template('shop.html', products=products_data)
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)