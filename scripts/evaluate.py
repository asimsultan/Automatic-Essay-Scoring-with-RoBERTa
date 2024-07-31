
import torch
import argparse
from transformers import RobertaForSequenceClassification, RobertaTokenizer
from utils import get_device, preprocess_data, EssayScoringDataset
from datasets import load_dataset
from sklearn.metrics import mean_squared_error

def main(model_path, data_path):
    # Load Model and Tokenizer
    model = RobertaForSequenceClassification.from_pretrained(model_path)
    tokenizer = RobertaTokenizer.from_pretrained(model_path)

    # Device
    device = get_device()
    model.to(device)

    # Load Dataset
    dataset = load_dataset('csv', data_files={'validation': data_path})
    tokenized_datasets = dataset.map(lambda x: preprocess_data(tokenizer, x, max_length=512), batched=True)

    # DataLoader
    eval_dataset = EssayScoringDataset(tokenized_datasets['validation'])
    eval_loader = torch.utils.data.DataLoader(eval_dataset, batch_size=16, shuffle=False)

    # Evaluation Function
    def evaluate(model, data_loader, device):
        model.eval()
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for batch in data_loader:
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['labels'].to(device)

                outputs = model(input_ids=input_ids, attention_mask=attention_mask)
                preds = torch.argmax(outputs.logits, dim=-1)
                all_preds.extend(preds.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())

        mse = mean_squared_error(all_labels, all_preds)
        return mse

    # Evaluate
    mse = evaluate(model, eval_loader, device)
    print(f'Mean Squared Error: {mse}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True, help='Path to the fine-tuned model')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the CSV file containing validation data')
    args = parser.parse_args()
    main(args.model_path, args.data_path)
