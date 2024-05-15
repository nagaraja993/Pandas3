import pandas as pdimport pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def clean(x):
        return x[0].upper() + x[1:].lower()
    users['name'] = users['name'].apply(clean)
    return users.sort_values(by = ['user_id'])
    