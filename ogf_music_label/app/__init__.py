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
                'image': 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=300&h=300&fit=crop&crop=face',
                'bio': 'Artiste principal du label, prône les valeurs familiales et spirituelles.',
                'social': {'instagram': '#', 'spotify': '#', 'youtube': '#'}
            },
            {
                'name': 'Soul Sister',
                'genre': 'R&B Gospel',
                'image': 'https://images.unsplash.com/photo-1494790108755-2616c9c0e8e3?w=300&h=300&fit=crop&crop=face',
                'bio': 'Voix puissante et messages inspirants, ambassadrice de la foi.',
                'social': {'instagram': '#', 'spotify': '#', 'youtube': '#'}
            },
            {
                'name': 'Young Prophet',
                'genre': 'Hip-Hop Spirituel',
                'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face',
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
                'cover': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=300&h=300&fit=crop&auto=format',
                'description': 'Premier album du label, mélange de rap conscient et de spiritualité.',
                'links': {'spotify': '#', 'apple': '#', 'youtube': '#'}
            },
            {
                'title': 'Blessed Vibes',
                'artist': 'Soul Sister',
                'type': 'EP',
                'cover': 'https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?w=300&h=300&fit=crop&auto=format',
                'description': 'EP de 6 titres R&B gospel, messages d\'espoir et de foi.',
                'links': {'spotify': '#', 'apple': '#', 'youtube': '#'}
            },
            {
                'title': 'New Generation',
                'artist': 'Young Prophet',
                'type': 'Single',
                'cover': 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=300&h=300&fit=crop&auto=format',
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
                'image': 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=400&h=200&fit=crop&auto=format'
            },
            {
                'title': 'Concert Spirituel',
                'date': '22 Avril 2024',
                'location': 'Église Saint-Martin, Lyon',
                'description': 'Concert caritatif avec Soul Sister et MC Divine.',
                'image': 'https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?w=400&h=200&fit=crop&auto=format'
            },
            {
                'title': 'Festival Hip-Hop Conscient',
                'date': '10 Juin 2024',
                'location': 'Parc de la Villette, Paris',
                'description': 'Participation au plus grand festival de hip-hop conscient.',
                'image': 'https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?w=400&h=200&fit=crop&auto=format'
            }
        ]
        return render_template('events.html', events=events_data)
    
    @app.route('/shop')
    def shop():
        products_data = [
            {
                'name': 'T-Shirt OGF Classic',
                'price': '25€',
                'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=300&h=300&fit=crop&auto=format',
                'description': 'T-shirt noir avec logo OGF brodé, 100% coton bio.'
            },
            {
                'name': 'Casquette Snapback',
                'price': '30€',
                'image': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=300&h=300&fit=crop&auto=format',
                'description': 'Casquette snapback violette avec broderie "Only God & Family".'
            },
            {
                'name': 'Hoodie Premium',
                'price': '55€',
                'image': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=300&h=300&fit=crop&auto=format',
                'description': 'Sweat à capuche premium, design exclusif du label.'
            },
            {
                'name': 'Vinyl Faith & Family',
                'price': '35€',
                'image': 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=300&h=300&fit=crop&auto=format',
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