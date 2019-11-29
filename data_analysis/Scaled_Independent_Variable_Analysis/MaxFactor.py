import pandas as pd

df = pd.read_csv('Mortality Outcome GTWR Model SCALED Outputs 2006-2012 White.csv', header=0)

df2010 = df[df.year == 2010]

result = df2010[['fips', 'name.x', 'state.x', 'county', 'state.y']].copy()

result['max_factor'] = df2010[['coef_opioids_perperson', 'coef_hhincome_clean', 'coef_age_clean', 'coef_percent_white' ]].idxmax(axis=1)

result.to_csv('Mortality Outcome GTWR Model SCALED Outputs 2010 Max Factors.csv')

print("Written to Mortality Outcome GTWR Model SCALED Outputs 2010 Max Factors.csv")

print(result['max_factor'].value_counts())