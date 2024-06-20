import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load your test dataset
test_dataset = load_dataset('your_dataset_name', split='test')

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained('your_model_path')

# Tokenize the test dataset
def tokenize(batch):
    return tokenizer(batch['text'], padding=True, truncation=True, max_length=512)

test_tokenized = test_dataset.map(tokenize, batched=True)
test_tokenized.set_format('torch', columns=['input_ids', 'attention_mask', 'label'])

# Initialize the Trainer
training_args = TrainingArguments(output_dir='./results', per_device_eval_batch_size=16)
trainer = Trainer(model=model, args=training_args)

# Make predictions on the test set
preds = trainer.predict(test_tokenized)

# Extract predicted and true labels
pred_labels = np.argmax(preds.predictions, axis=1)
true_labels = test_tokenized['label'].numpy()

# Decode the input_ids back to text for analysis
texts = [tokenizer.decode(ids, skip_special_tokens=True) for ids in test_tokenized['input_ids']]

# Create a DataFrame with texts, true labels, and predicted labels
df = pd.DataFrame({'text': texts, 'true_label': true_labels, 'predicted_label': pred_labels})

# Identify misclassified examples
misclassified = df[df['true_label'] != df['predicted_label']]

# Save or display misclassified examples
misclassified.to_csv('misclassified_examples.csv', index=False)
print(misclassified)

