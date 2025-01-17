## scripts for how to filter a df on a value and various methods to extract text or values from each row and col and print to screen

## create sub_df with filter 
sub_df = new_df[new_df['MMR_diversity'] >= 0.6]  # Filter the DataFrame

## 1. using enumerate and iterrows to print full text:
for index, row in sub_df.iterrows():
    print(f"Index: {index}")
    print(f"Dev Response: {row['dev_response']}")
    print(f"Preprod Response: {row['preprod_response']}")
    print("-" * 20)  # Separator for better readability

## 2. using enumerate and iloc to print full text
for index in range(len(sub_df)) :
  print(f"Index: {sub_df.index[index]}")
  print(f"Dev Response: {sub_df['dev_response'].iloc[index]}")
  print(f"Preprod Response: {sub_df['preprod_response'].iloc[index]}")
  print("-" * 20)

## 3. using zip to print full text:
for index,dev_resp,preprod_resp in zip(sub_df.index,sub_df['dev_response'],sub_df['preprod_response']):
  print(f"Index: {index}")
  print(f"Dev Response: {dev_resp}")
  print(f"Preprod Response: {preprod_resp}")
  print("-" * 20)

## 4. using apply to print full text:
def print_responses(row):
    print(f"Index: {row.name}")  # row.name gives the index
    print(f"Dev Response: {row['dev_response']}")
    print(f"Preprod Response: {row['preprod_response']}")
    print("-" * 20)

sub_df.apply(print_responses, axis=1)



## check null values in lst of df's
## check null again
df_lst= [df1, df2, df2, df3]

# Iterate through the list of DataFrames directly
for df in df_lst:
  # Check for null values within each DataFrame
  if df.isnull().values.any():
    print(f"Null values found in DataFrame: {df.isnull().sum().sum()}")  # Print total number of nulls
  else:
    print("No null values in this DataFrame")






## create venv
python3 -m venv <virtual_env_name>

## activate venv
source /path/to/venv/bin/activate
