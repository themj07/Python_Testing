import json
from flask import Flask,render_template,request,redirect,flash,url_for

def loadClubs(filename='clubs.json'):
    with open(filename) as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

def loadCompetitions(file='competitions.json'):
    with open(file) as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html', clubs = clubs, competitions = competitions)

@app.route('/showSummary', methods=['POST'])
def showSummary():
    entered_email = request.form['email']
    club = next((c for c in clubs if c['email'] == entered_email), None)
    
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash("L'adresse e-mail n'est pas associée à un club. Veuillez réessayer.")
        return render_template('index.html', clubs=clubs, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    # Extract data from the form
    competition_name = request.form['competition']
    club_name = request.form['club']
    places_required = int(request.form['places'])

    # Search for the competition and club in the existing data
    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)

    # Check if the competition and club exist
    if competition is None or club is None:
        flash('Error - Competition or club not found!')
        return render_template('welcome.html', club=club, competitions=competitions)

    # Check the number of available places
    current_places = int(competition['numberOfPlaces'])
    purchased_places = club.get('purchasedPlaces', 0)

    if places_required <= 0 or places_required > current_places:
        flash('Error - Invalid number of places requested!')
        return render_template('welcome.html', club=club, competitions=competitions)
    
    if places_required + purchased_places > 12:
        flash('Error - You have already purchased 12 places!')
        return render_template('welcome.html', club=club, competitions=competitions)

    # Update the number of places after the purchase
    competition['numberOfPlaces'] = current_places - places_required
    club['purchasedPlaces'] = purchased_places + places_required

    flash('Great - Booking complete!')

    # Prevent the club from buying more places if they've already purchased 12
    if purchased_places + places_required >= 12:
        club['canBuyMorePlaces'] = False

    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))