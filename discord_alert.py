import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_alert(listing, analysis):
    """Send property alert to Discord"""
    
    # Build address string
    address = f"{listing.get('StreetNumber', '')} {listing.get('StreetName', '')} {listing.get('StreetSuffix', '')}, {listing.get('City', '')}, {listing.get('StateOrProvince', '')} {listing.get('PostalCode', '')}"
    
    price = listing.get('ListPrice', 'N/A')
    price_str = f"${price:,}" if isinstance(price, (int, float)) else str(price)
    
    beds = listing.get('BedroomsTotal', 'N/A')
    baths = listing.get('BathroomsTotalInteger', 'N/A')
    sqft = listing.get('LivingArea', 'N/A')
    
    # Get listing URL if available
    url = "N/A"
    if listing.get('Media') and len(listing['Media']) > 0:
        url = listing['Media'][0].get('MediaURL', 'N/A')
    
    # Create Discord embed
    embed = {
        "title": f"🏠 {address}",
        "description": analysis.get('reasoning', 'No reasoning provided'),
        "color": 0x00ff00,  # Green
        "fields": [
            {
                "name": "Price",
                "value": price_str,
                "inline": True
            },
            {
                "name": "Score",
                "value": f"{analysis.get('score', 'N/A')}/10",
                "inline": True
            },
            {
                "name": "Beds/Baths",
                "value": f"{beds} bed, {baths} bath",
                "inline": True
            },
            {
                "name": "Square Feet",
                "value": str(sqft),
                "inline": True
            },
            {
                "name": "Listing",
                "value": url if url != "N/A" else "No URL available",
                "inline": False
            }
        ],
        "footer": {
            "text": f"Listing ID: {listing.get('ListingId', 'N/A')}"
        }
    }
    
    payload = {
        "embeds": [embed]
    }
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print(f"✅ Alert sent for {address}")
        return True
    except Exception as e:
        print(f"❌ Error sending Discord alert: {e}")
        return False