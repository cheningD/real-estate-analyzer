from mock_listings import get_mock_listings
from analyzer import analyze_property
from discord_alert import send_alert

def main():
    print("🏠 Real Estate Deal Analyzer - Starting...")
    print("-" * 50)
    
    # Fetch listings (using mock data for demo)
    print("📋 Fetching listings...")
    response = get_mock_listings()
    listings = response.get('value', [])
    
    print(f"✅ Found {len(listings)} listings to analyze\n")
    
    # Analyze each listing
    for i, listing in enumerate(listings, 1):
        address = f"{listing.get('StreetNumber', '')} {listing.get('StreetName', '')} {listing.get('StreetSuffix', '')}, {listing.get('City', '')}"
        print(f"[{i}/{len(listings)}] Analyzing: {address}")
        
        # Run AI analysis
        analysis = analyze_property(listing)
        
        decision = analysis.get('decision', 'UNKNOWN')
        print(f"    Decision: {decision}")
        print(f"    Score: {analysis.get('score', 'N/A')}/10")
        
        # Send alert if property is worth it
        if decision == 'ALERT':
            print(f"    🚨 Sending Discord alert...")
            send_alert(listing, analysis)
        else:
            print(f"    ⏭️  Skipping (not a match)")
        
        print()
    
    print("-" * 50)
    print("✅ Analysis complete!")

if __name__ == "__main__":
    main()