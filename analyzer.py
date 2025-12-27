import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_property(listing):
    """Analyze a property listing using Claude"""
    
    # Extract key data
    address = f"{listing.get('StreetNumber', '')} {listing.get('StreetName', '')} {listing.get('StreetSuffix', '')}, {listing.get('City', '')}, {listing.get('StateOrProvince', '')} {listing.get('PostalCode', '')}"
    price = listing.get('ListPrice', 'N/A')
    beds = listing.get('BedroomsTotal', 'N/A')
    baths = listing.get('BathroomsTotalInteger', 'N/A')
    sqft = listing.get('LivingArea', 'N/A')
    description = listing.get('PublicRemarks', 'N/A')
    
    prompt = f"""You are a real estate investment analyzer. Analyze this property and determine if it's worth alerting the team.

PROPERTY DATA:
Address: {address}
Price: ${price:,} if isinstance(price, (int, float)) else {price}
Bedrooms: {beds}
Bathrooms: {baths}
Square Feet: {sqft}
Description: {description}

CRITERIA (example criteria - will be customized per client):
- Price under $500k preferred for value-add opportunities
- At least 2 bed, 1 bath minimum
- Look for keywords indicating potential: "fixer", "needs work", "investor special", "below market", "motivated seller"
- Good locations (established neighborhoods)

RESPOND IN THIS EXACT FORMAT:
DECISION: [ALERT or SKIP]
REASONING: [2-3 sentences explaining why]
SCORE: [1-10 investment potential]

Be concise and specific."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = message.content[0].text
        
        # Parse response
        lines = response_text.strip().split('\n')
        decision = None
        reasoning = None
        score = None
        
        for line in lines:
            if line.startswith('DECISION:'):
                decision = line.split(':', 1)[1].strip()
            elif line.startswith('REASONING:'):
                reasoning = line.split(':', 1)[1].strip()
            elif line.startswith('SCORE:'):
                score_text = line.split(':', 1)[1].strip()
                # Extract just the first number
                score = score_text.split('/')[0] if '/' in score_text else score_text
        
        return {
            'decision': decision,
            'reasoning': reasoning,
            'score': score,
            'full_response': response_text
        }
        
    except Exception as e:
        print(f"Error analyzing property: {e}")
        return {
            'decision': 'ERROR',
            'reasoning': str(e),
            'score': '0'
        }