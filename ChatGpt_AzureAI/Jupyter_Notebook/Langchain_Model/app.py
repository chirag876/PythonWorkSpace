import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, AdamW
import torch
from torch.utils.data import DataLoader, Dataset
import os

# Load your CSV dataset
df = pd.read_csv(r'C:\Workspaces\CodeSpaces\Python_Work\Langchain_Model\benchmark.csv')

# Flatten the CSV into a list of data points
data_points = []
for col in df.columns:
    for value in df[col]:
        data_points.append(f"{col}: {value}")

# Create labels based on column names
labels = [col for col in df.columns for _ in range(len(df))]

# Encode labels using LabelEncoder
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data_points, y_encoded, test_size=0.2, random_state=42)

# Tokenize the data with padding token
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
X_train_tokens = tokenizer(X_train, padding=True, truncation=True, return_tensors='pt', max_length=50)
X_test_tokens = tokenizer(X_test, padding=True, truncation=True, return_tensors='pt', max_length=50)

# Create a custom dataset
class CustomDataset(Dataset):
    def __init__(self, tokens, labels):
        self.tokens = tokens
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            'input_ids': self.tokens['input_ids'][idx],
            'attention_mask': self.tokens['attention_mask'][idx],
            'labels': torch.tensor(self.labels[idx])
        }

train_dataset = CustomDataset(X_train_tokens, y_train)
test_dataset = CustomDataset(X_test_tokens, y_test)

# Set up DataLoader
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=4, shuffle=False)

# Load pre-trained DistilBERT model for sequence classification
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=len(label_encoder.classes_))

# Set up optimizer and loss function using AdamW
optimizer = AdamW(model.parameters(), lr=5e-5)

# Training loop
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
num_epochs = 3

for epoch in range(num_epochs):
    model.train()
    total_loss = 0

    for batch in train_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()

        loss.backward()
        optimizer.step()

    average_loss = total_loss / len(train_loader)
    print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {average_loss}')

# Save the trained model
model_save_path = r'C:/Workspaces/CodeSpaces/Python_Work/Langchain_Model/saved_model'
os.makedirs(model_save_path, exist_ok=True)
model.save_pretrained(model_save_path)

# Evaluation
model.eval()
all_preds = []
all_labels = []

with torch.no_grad():
    for batch in test_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        preds = torch.argmax(logits, dim=1)

        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

# Decode predictions
decoded_preds = label_encoder.inverse_transform(all_preds)

# Evaluate the model
accuracy = accuracy_score(y_test, all_preds)
classification_rep = classification_report(y_test, all_preds)

# Display the results
print(classification_rep)
print(accuracy)
