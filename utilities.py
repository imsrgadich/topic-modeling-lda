import pandas as pd

def standardize_text(df, text_field):
    '''
    The definition standardizes the text by removing redundant text.
    Removes http.., twitter handles etc.  
    '''
    df[text_field] = df[text_field].str.replace(r"http\S+", "")
    df[text_field] = df[text_field].str.replace(r"http", "")
    df[text_field] = df[text_field].str.replace(r"@\S+", "")
    df[text_field] = df[text_field].str.replace(r"@", "at")
    df[text_field] = df[text_field].str.lower()
    return df