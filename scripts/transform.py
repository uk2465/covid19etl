# scripts/transform.py
import pandas as pd

def transform_covid_data(raw_data):
    # Convert to DataFrame
    df = pd.DataFrame(raw_data)
    
    # Flatten nested structures
    df['country'] = df['countryInfo'].apply(lambda x: x['country'])
    df['iso2'] = df['countryInfo'].apply(lambda x: x['iso2'])
    df['iso3'] = df['countryInfo'].apply(lambda x: x['iso3'])
    
    # Select relevant columns
    columns = [
        'updated', 'country', 'iso2', 'iso3',
        'cases', 'todayCases', 'deaths', 'todayDeaths',
        'recovered', 'todayRecovered', 'active', 'critical',
        'casesPerOneMillion', 'deathsPerOneMillion',
        'tests', 'testsPerOneMillion', 'population', 'continent'
    ]
    df = df[columns]
    
    # Convert timestamp to datetime
    df['updated'] = pd.to_datetime(df['updated'], unit='ms')
    
    # Add processing timestamp
    df['processed_at'] = pd.Timestamp.now()
    
    return df
