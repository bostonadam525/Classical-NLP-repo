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
