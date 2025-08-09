# Amazon Datasets for S3 Ingestion and Pipeline Practice

## 1. Amazon Review and Metadata (UCSD, 2018)

* **Description**: Product reviews and metadata from 1996 to 2018.
* **Format**: JSON (convertible to CSV)
* **Source**: [UCSD Amazon Dataset](https://nijianmo.github.io/amazon/)

### Direct Download Links:

* [Electronics reviews (Electronics.json.gz)](https://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Electronics.json.gz)
* [Books metadata (meta\_Books.json.gz)](https://deepyeti.ucsd.edu/jianmo/amazon/metaFiles2/meta_Books.json.gz)

---

## 2. Stanford SNAP Amazon Review Dataset (1995–2013)

* **Description**: 34 million reviews categorized by domain.
* **Format**: JSON
* **Source**: [Stanford SNAP Dataset](https://snap.stanford.edu/data/web-Amazon.html)

### Direct Download Links:

* [Electronics reviews (reviews\_Electronics\_5.json.gz)](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Electronics_5.json.gz)
* [Books reviews (reviews\_Books\_5.json.gz)](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Books_5.json.gz)

---

## 3. Amazon Reviews 2023 (UCSD on HuggingFace)

* **Description**: 570+ million reviews with metadata.
* **Format**: Parquet
* **Source**: [Amazon Reviews 2023 on HuggingFace](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)

### Sample Load Code:

```python
pip install datasets
from datasets import load_dataset
load_dataset("McAuley-Lab/Amazon-Reviews-2023", split="train[:1%]")
```

---

## 4. Amazon Shopping Session Data (Kaggle)

* **Description**: User sessions and product views.
* **Format**: CSV
* **Source**: [Amazon Shopping Session Dataset on Kaggle](https://www.kaggle.com/datasets/gfreschi/amazon-books-reviews)

---

## 5. Amazon Product Attribute Dataset (Kaggle)

* **Description**: Annotated product attributes for NLP/ML tasks.
* **Format**: CSV
* **Source**: [Amazon Product Attribute Dataset on Kaggle](https://www.kaggle.com/datasets/PromptCloudHQ/amazon-product-dataset)

---

## Recommended Starter Dataset

**Dataset**: Electronics reviews (Electronics.json.gz)
**Size**: \~120 MB
**Link**: [Electronics.json.gz](https://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Electronics.json.gz)
**Use Case**: Upload to S3, use Glue Crawler to infer schema, then query via Athena. Optionally, convert to CSV before ingestion.
