from datasets import load_dataset

# Load the Amazon Reviews 2023 dataset
dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023")

# Check a few samples
print(dataset["train"][0])

df = dataset.to_pandas()

# Save locally
df.to_csv("amazon_reviews_books.csv", index=False)
