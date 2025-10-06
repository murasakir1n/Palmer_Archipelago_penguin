import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("penguins_lter.csv")

# Clearing data
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')

df = df.drop(columns = ['comments'])
df = df.drop(columns = ['studyname'])
df = df.drop(columns = ['sample_number'])
df = df.drop(columns = ['individual_id'])

print(df.columns.tolist())


columns_round = ['culmen_length_(mm)', 'culmen_depth_(mm)','flipper_length_(mm)', 'body_mass_(g)']
columns_delta = [ 'delta_15_n_(o/oo)', 'delta_13_c_(o/oo)']

for column_r in columns_round:
    df[column_r] = df[column_r].fillna(df[column_r].median()).round(1)

for column_d in columns_delta:
    df[column_d] = df[column_d].fillna(df[column_d].median())


sex_mode = df['sex'].mode()
print(sex_mode)

# Тут видно, что больше всего самцов, заменим пропуски на Male

df['sex'] = df['sex'].fillna(df['sex'].mode()[0])
df['sex'] = df['sex'].replace('.', 'MALE')

sex_count = df['sex'].value_counts()
print(sex_count)

engine = create_engine('postgresql://postgres:eaajcqt1337eaajcqt@localhost:5432/Palmer_Archipelago_penguin')

df.to_sql('palmer_penguins', engine, if_exists='replace', index= False)


