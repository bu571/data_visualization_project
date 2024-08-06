import json

file_path = r'C:\Users\Godhane computer\Documents\data_visualization_project\jsondata.json'

sample_data = [
    {
        "intensity": "High",
        "likelihood": "Likely",
        "relevance": "High",
        "year": 2024,
        "country": "CountryX",
        "topics": "Topic1",
        "region": "RegionY",
        "city": "CityZ",
        "sector": "SectorA",
        "pest": "PestB",
        "source": "SourceC",
        "swot": "SWOTD"
    }
]

with open(file_path, 'w') as f:
    json.dump(sample_data, f, indent=4)

print(f'Sample file created at: {file_path}')
