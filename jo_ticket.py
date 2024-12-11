import json
import locale
from datetime import datetime
import os
from pathlib import Path
from typing import Dict, List

import qrcode
from PIL import Image, ImageDraw, ImageFont

# Configuration globale
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

# Constantes
FONTS_DIR = Path("fonts")
OUTPUT_DIR = Path("tickets")
TICKET_TEMPLATE = Path("ticketJO.webp")

# Styles
TEAM_FONT = ImageFont.truetype(str(FONTS_DIR / "Paris2024.ttf"), 36)
TICKET_FONT = ImageFont.truetype(str(FONTS_DIR / "Paris2024.ttf"), 22)

TEAM_COLOR = (51, 19, 104)
TEXT_COLOR = (255, 255, 255)

# Positions des textes
POSITIONS = {
    "home_team": (37, 426),
    "away_team": (112, 503),
    "stadium": (60, 588),
    "datetime": (60, 656),
    "category": (20, 756),
    "seat": (200, 756),
    "price": (325, 756),
    "qr_code": (126, 835)
}

def load_json(filename: str):
    """Charge un fichier JSON avec gestion d'erreurs."""
    try:
        with open(filename, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erreur lors du chargement de {filename} : {e}")
        return []

def create_indexed_dict(data, key='id'):
    """Convertit la liste en dictionnaire pour une recherche plus rapide."""
    return {item[key]: item for item in data}

def format_price(price: float, currency: str) -> str:
    """Formate le prix avec le symbole monétaire lié à la devise."""
    if currency == 'USD':
        return f"${price}"
    elif currency == 'EUR':
        return f"{price} €"
    return f"{price} {currency}"

def generate_ticket(ticket, events, stadiums, index):
    """Génère un ticket individuel."""
    if not (ticket and 'event_id' in ticket):
        return None

    event = events.get(ticket['event_id'])
    stadium = stadiums.get(event.get('stadium_id')) if event else None
    
    if not event and stadium:
        print(f"Données manquantes pour le ticket {ticket['id']}")
        return None

    event_date = datetime.fromisoformat(event['start'])
    
    with Image.open(TICKET_TEMPLATE) as im:
        draw = ImageDraw.Draw(im)
        
        # Ajout des textes avec fonction de dessin factorisée
        def draw_text(key, text, font=TICKET_FONT, color=TEXT_COLOR):
            draw.text(POSITIONS[key], text, font=font, fill=color)
        
        draw_text("home_team", event['team_home'], font=TEAM_FONT, color=TEAM_COLOR)
        draw_text("away_team", event['team_away'], font=TEAM_FONT, color=TEAM_COLOR)
        draw_text("stadium", f"{stadium['name']} - {stadium['location']}")
        draw_text("datetime", f"{event_date.strftime('%d/%m/%Y')} à {event_date.strftime('%H:%M')}")
        draw_text("category", ticket['category'])
        draw_text("seat", "Libre" if ticket['seat'] == "free" else ticket['seat'])
        draw_text("price", format_price(ticket['price'], ticket['currency']))

        # Génération du QR Code
        qr = qrcode.QRCode(box_size=4)
        qr.add_data(ticket['id'])
        qr_im = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
        im.paste(qr_im, (126, 835), qr_im)

        # Sauvegarde du ticket
        OUTPUT_DIR.mkdir(exist_ok=True)
        ticket_filename = OUTPUT_DIR / f"ticket_{index}_{ticket['id']}.webp"
        im.save(ticket_filename)
        print(f"Billet généré : {ticket_filename}")

def main():
    """Fonction principale de génération des tickets."""
    events = {event['id']: event for event in load_json('events.json')}
    stadiums = {stadium['id']: stadium for stadium in load_json('stadiums.json')}
    tickets = load_json('tickets.json')

    if not (events and stadiums and tickets):
        print("Erreur : Impossible de charger les données nécessaires.")
        return

    for index, ticket in enumerate(tickets, 1):
        generate_ticket(ticket, events, stadiums, index)

    print("Génération des billets terminée. " + str(len(tickets)) + " billets ont été générés.")

if __name__ == "__main__":
    main()