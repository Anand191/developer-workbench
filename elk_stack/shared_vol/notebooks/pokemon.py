import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

def get_legendary_pokemon(df: pd.DataFrame) -> pd.DataFrame:
    """
    (1)
    Select legendary Pokemon only, drop the 
    `Legendary` column and reset the index.
    """
    df = df[df.Legendary]
    df.drop(columns=['Legendary'], inplace=True)
    return df.reset_index(drop=True)
    

def name_starts_with(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    """ 
    (2)
    Select all rows containing Pokemon names that start 
    with `prefix`. Only return `#`, `Name` and `Total` 
    columns and reset indices. 
    """
    return df[df['Name'].str.startswith(prefix)][['#', 'Name', 'Total']].reset_index(drop=True)
  
def fix_camel_cased_names(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    (3)
    Some of the `Name` column data in the dataframe 
    is badly formatted.

    Names in the form `LandorusIncarnate Forme` (that is, 
    with a word containing a lowercase letter immediately
    followed by an uppercase letter) should be fixed by 
    inserting a space between the letters as follows: 
    `Landorus Incarnate Forme`.

    An edge case is `Zygarde50% Forme` which should be 
    corrected to `Zygarde 50% Forme`. In other words, digits 
    immediately following a lowercase letter should be 
    considered as well as uppercase in splitting.

    The last edge case is the Pokemon named "Porygon2". 
    This is the correct name and should be maintained, so the 
    final requirement for inserting whitespace is that the rest 
    of the string must contain a non-digit character. Therefore,
    "Porygon12345" would be ignored but "Porygon12345abc"
    would become "Porygon 12345abc" since it has a non-digit 
    character after the "n12345" substring.

    Return only Pokemon with fixed names using the 
    columns `#` and `Name`.

    Finally, reset the index before returning the df.

    ====================
    A few more examples:
    ====================
    "AA"  => "AA"   (do nothing, this is normal)
    "aB"  => "a B"
    "a2"  => "a2"   (no further characters after the "2")
    "a23" => "a23"  (no further characters after the "23")
    "a2b" => "a 2b" (additional character "b" following "a2")
    """
    pass

def get_most_common_type_combos(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    (4)
    Find the Type 1 and Type 2 combo(s) that is/are
    most common for all Pokemon, ignoring nan. Order
    matters so `Psychic, Water` != `Water, Psychic`.
    
    Returned df should have columns `Type 1` and 
    `Type 2` and rows should be the most common. 
    """
    df['t1t2'] = df['Type 1'] + '-' + df['Type 2']
    max_count = df.t1t2.value_counts().max()
    max_combos = df.t1t2.value_counts().index[np.where(df.t1t2.value_counts().values==max_count)[0]]
    t1t2_max = [s.split('-') for s in max_combos]
    t1_max = [s[0] for s in t1t2_max]
    t2_max = [s[1] for s in t1t2_max]
    return df[(df['Type 1'].isin(t1_max)) & (df['Type 2'].isin(t2_max))][['Type 1', 'Type 2']].drop_duplicates().reset_index(drop=True)
    

def get_most_common_legendary_pokemon_types(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    (5)
    Of legendary Pokemon, return a DataFrame of the counts 
    of each type that appears in either `Type 1` or `Type 2` 
    columns ordered descending on the `Count` column and 
    ascending on the `Type` columns.
    """
    df = df[df.Legendary]
    df1 = df.groupby('Type 1').agg({'#': 'count'}).reset_index().rename(columns={'Type 1': 'Type'})
    df2 = df.groupby('Type 2').agg({'#': 'count'}).reset_index().rename(columns={'Type 2': 'Type'})
    fdf = df1.merge(df2, on='Type', how='outer')
    fdf.fillna(0, inplace=True)
    fdf['Count'] = fdf['#_x'] + fdf['#_y']
    fdf.drop(columns=['#_x', '#_y'], inplace=True)
    fdf = fdf.sort_values(['Count', 'Type'], ascending=[False, True])
    fdf = fdf.astype({"Count": int})
    return fdf.reset_index(drop=True)
    

def group_by_generation_avg_strength(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    (6)
    Rank the `Generation`s by average strength using 
    the `Total` column and sort descending. Counts
    are raw row counts; ignore duplicate Pokemon ids.
    
    Return the df with columns `Generation`, 
    `Mean Total` and `Count`.
    
    The final row of the returned df should be a summary
    of all generations shown in the df. The format is
    `All` (string), mean of `Mean Total` and sum of `Count`.
    """
    fdf = df.groupby('Generation').agg({'Total': 'mean', '#': 'count'}).reset_index().rename(columns={'Total': 'Mean Total', '#': 'Count'})
    fdf = fdf.sort_values(['Mean Total'], ascending=False)
    totals = pd.DataFrame(np.asarray(['All', np.mean(fdf['Mean Total']), np.sum(fdf['Count'])]).reshape(1,3), 
columns=['Generation', 'Mean Total', 'Count'])
    fdf = pd.concat([fdf, totals])
    fdf = fdf.astype({"Mean Total": float})
    fdf = fdf.astype({"Count": int})
    return fdf.set_index('Generation')

def get_pokemon_with_unique_type1_type2_combos(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    (7)
    Get combinations of `Type 1` and `Type 2` columns 
    which are unique in the entire df, respecting order 
    between the pair (in other words, a, b != b, a) and 
    ignoring all nan rows. Sort by `Name`.
    """
    df.dropna(inplace=True)
    df['t1t2'] = df['Type 1'] + '-' + df['Type 2']
    unk = df.t1t2.unique()
    unk = [s.split('-') for s in unk]
    t1_max = [s[0] for s in unk]
    t2_max = [s[1] for s in unk]
    return df[(df['Type 1'].isin(t1_max)) & (df['Type 2'].isin(t2_max))][['Name','Type 1', 'Type 2']].reset_index(drop=True)
