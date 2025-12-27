def get_mock_listings():
    """Mock data matching Bridge MLS API exact response format"""
    return {
        "@odata.context": "https://api.bridgedataoutput.com/api/v2/OData/test/$metadata#Property",
        "@odata.nextLink": "https://api.bridgedataoutput.com/api/v2/OData/test/Property?$skip=3",
        "value": [
            {
                "@odata.id": "https://api.bridgedataoutput.com/api/v2/OData/test/Property('P_5af601c3fc76173b348291e9')",
                "ListingKey": "P_5af601c3fc76173b348291e9",
                "ListingId": "12345",
                "StandardStatus": "Active",
                "ListPrice": 425000,
                "StreetNumber": "123",
                "StreetName": "Main",
                "StreetSuffix": "St",
                "City": "Los Angeles",
                "StateOrProvince": "CA",
                "PostalCode": "90210",
                "BedroomsTotal": 3,
                "BathroomsTotalInteger": 2,
                "LivingArea": 1650,
                "PropertyType": "Residential",
                "PropertySubType": "Single Family Residence",
                "PublicRemarks": "Fixer-upper opportunity! Property needs cosmetic updates but has great bones. Large lot in desirable neighborhood. Priced below market for quick sale.",
                "ListingContractDate": "2024-12-26T08:00:00Z",
                "ModificationTimestamp": "2024-12-26T08:05:00Z",
                "Media": [
                    {
                        "MediaURL": "https://www.zillow.com/homedetails/123-Main-St/12345_zpid/",
                        "MediaType": "Image"
                    }
                ]
            },
            {
                "@odata.id": "https://api.bridgedataoutput.com/api/v2/OData/test/Property('P_5af601c3fc76173b348291e10')",
                "ListingKey": "P_5af601c3fc76173b348291e10",
                "ListingId": "12346",
                "StandardStatus": "Active",
                "ListPrice": 1250000,
                "StreetNumber": "456",
                "StreetName": "Oak",
                "StreetSuffix": "Ave",
                "City": "Beverly Hills",
                "StateOrProvince": "CA",
                "PostalCode": "90212",
                "BedroomsTotal": 5,
                "BathroomsTotalInteger": 4,
                "LivingArea": 3200,
                "PropertyType": "Residential",
                "PropertySubType": "Single Family Residence",
                "PublicRemarks": "Luxury turnkey property in pristine condition. Recently renovated with high-end finishes throughout.",
                "ListingContractDate": "2024-12-26T07:30:00Z",
                "ModificationTimestamp": "2024-12-26T07:35:00Z",
                "Media": [
                    {
                        "MediaURL": "https://www.zillow.com/homedetails/456-Oak-Ave/12346_zpid/",
                        "MediaType": "Image"
                    }
                ]
            },
            {
                "@odata.id": "https://api.bridgedataoutput.com/api/v2/OData/test/Property('P_5af601c3fc76173b348291e11')",
                "ListingKey": "P_5af601c3fc76173b348291e11",
                "ListingId": "12347",
                "StandardStatus": "Active",
                "ListPrice": 380000,
                "StreetNumber": "789",
                "StreetName": "Pine",
                "StreetSuffix": "Rd",
                "City": "Pasadena",
                "StateOrProvince": "CA",
                "PostalCode": "91101",
                "BedroomsTotal": 2,
                "BathroomsTotalInteger": 1,
                "LivingArea": 1100,
                "PropertyType": "Residential",
                "PropertySubType": "Single Family Residence",
                "PublicRemarks": "Investor special - needs full renovation. Sold as-is. Cash buyers only.",
                "ListingContractDate": "2024-12-26T09:15:00Z",
                "ModificationTimestamp": "2024-12-26T09:20:00Z",
                "Media": [
                    {
                        "MediaURL": "https://www.zillow.com/homedetails/789-Pine-Rd/12347_zpid/",
                        "MediaType": "Image"
                    }
                ]
            }
        ]
    }