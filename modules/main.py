import pandas as pd
from modules.functions import add_ten

df = pd.DataFrame(data={
    'col1': [1, 2, 3],
    'col2': ['dog', 'cat', 'fish']
})

df['col1'] = df['col1'].apply(add_ten)

print(df)