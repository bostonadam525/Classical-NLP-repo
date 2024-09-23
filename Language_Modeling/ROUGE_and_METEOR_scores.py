## ROUGE Score function
!pip install rouge_score

from rouge_score import rouge_scorer

## function to calculate ROUGE score
def calculate_rouge(df, reference_col, response_col):
  """
  Calculates the ROUGE score between two columns of text in a DataFrame.

  Args:
    df: DataFrame containing the text data.
    reference_col: Name of the column containing the reference summaries.
    response_col: Name of the column containing the generated summaries.

  Returns:
    A list of ROUGE scores for each row in the DataFrame.
  """
  scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
  scores = []
  for idx in df.index:
    ref = df.loc[idx, reference_col]
    response = df.loc[idx, response_col]
    score = scorer.score(ref, response)
    scores.append(score)
  return scores


## models and responses
models = ['T5_', 'BART_'] 
responses = ['response_1', 'response_2']

## loop through data and calculate ROUGE
for model in models:
  for response in responses:
    summary_col = f'{model}{response}_summary'
    response_col = f'{response}'
    rouge_col = f'{response}_{model}ROUGE'
    df2[rouge_col] = calculate_rouge(df2, summary_col, response_col)

    # Accessing individual ROUGE scores (e.g., ROUGE-1)
    df2[f'{response}_{model}ROUGE1'] = df2[rouge_col].apply(lambda x: x['rouge1'].fmeasure)
    df2[f'{response}_{model}ROUGEL'] = df2[rouge_col].apply(lambda x: x['rougeL'].fmeasure)

    avg_rouge1 = df2[f'{response}_{model}ROUGE1'].mean()
    avg_rougeL = df2[f'{response}_{model}ROUGEL'].mean()
    print(f"Average ROUGE-1 for {response} ({model.replace('_', '')}): {avg_rouge1}")
    print(f"Average ROUGE-L for {response} ({model.replace('_', '')}): {avg_rougeL}")

# Calculate average ROUGE for each model across responses (using ROUGE-1 for example)
for model in models:
  rouge_cols = [f'{response}_{model}ROUGE1' for response in responses]
  df2[f'{model.replace("_", "")}Average_ROUGE1'] = df2[rouge_cols].mean(axis=1)

  avg_model_rouge1 = df2[f'{model.replace("_", "")}Average_ROUGE1'].mean()
  print(f"Average ROUGE-1 for {model.replace('_', '')}: {avg_model_rouge1}")





## METEOR Score function
!pip install evaluate
import evaluate


## load meteor score
meteor = evaluate.load('meteor')

## calculate meteor scores
df2['T5_meteor_1'] = df2.apply(lambda row: meteor.compute(predictions=[row['T5_response_1_summary']], references=[row['response_1']])['meteor'], axis=1)
df2['BART_meteor_1'] = df2.apply(lambda row: meteor.compute(predictions=[row['BART_response_1_summary']], references=[row['response_1']])['meteor'], axis=1)
df2['T5_meteor_2'] = df2.apply(lambda row: meteor.compute(predictions=[row['T5_response_2_summary']], references=[row['response_2']])['meteor'], axis=1)
df2['BART_meteor_2'] = df2.apply(lambda row: meteor.compute(predictions=[row['BART_response_2_summary']], references=[row['response_2']])['meteor'], axis=1)
