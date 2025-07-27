# Amazon-related Datasets for S3 Ingestion and Pipeline Practice

This document lists high-quality, public Amazon datasets suitable for building AWS S3-based data ingestion pipelines.

---

## 1. Amazon Review and Metadata (UCSD, 2018)

* **Description**: Amazon product reviews and metadata from 1996 to 2018.
* **Format**: JSON (.gz compressed)
* **Homepage**: [https://nijianmo.github.io/amazon](https://nijianmo.github.io/amazon)

**Sample Direct Links**:

* [Books Reviews (\~240MB)](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Books.json.gz)
* [Electronics Reviews](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Electronics.json.gz)
* [Books Metadata](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/metaFiles2/meta_Books.json.gz)

---

## 2. Stanford SNAP Amazon Review Dataset (1995–2013)

* **Description**: 34 million reviews with ratings, categories, and timestamps.
* **Format**: JSON
* **Homepage**: [https://snap.stanford.edu/data/web-Amazon.html](https://snap.stanford.edu/data/web-Amazon.html)

**Sample Direct Links**:

* [Electronics Reviews](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Electronics_5.json.gz)
* [Books Reviews](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Books_5.json.gz)

---

## 3. Amazon Reviews 2023 (McAuley Lab via HuggingFace)

* **Description**: 570M+ reviews across all product categories with metadata.
* **Format**: Parquet (requires conversion if needed)
* **Homepage**: [https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)

**Access Example**:

```bash
pip install datasets
from datasets import load_dataset
load_dataset("McAuley-Lab/Amazon-Reviews-2023", split="train[:1%]")
```

---

## 4. Amazon M2 Dataset (Shopping Sessions)

* **Description**: User sessions in multilingual shopping.
* **Format**: CSV
* **Homepage**: [https://github.com/awslabs/amazon-multilingual-data-release](https://github.com/awslabs/amazon-multilingual-data-release)
* **Direct Link**: [amazon\_shopping\_sessions\_en.csv](https://raw.githubusercontent.com/awslabs/amazon-multilingual-data-release/main/datasets/amazon_shopping_sessions_en.csv)

---

## 5. Amazon MAVE Dataset (Attribute Extraction)

* **Description**: Annotated product attributes from Amazon product titles.
* **Format**: CSV
* **Homepage**: [https://github.com/amazon-science/mave](https://github.com/amazon-science/mave)
* **Direct Link**: [annotations.csv](https://raw.githubusercontent.com/amazon-science/mave/main/data/annotations.csv)

---

## Recommended Starting Dataset

Use the following dataset for initial pipeline testing with Glue Crawlers, Athena, and S3:

* **Dataset**: `Books.json.gz`
* **Source**: UCSD Amazon Dataset
* **Direct Link**: [Download Here](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Books.json.gz)
* **File Size**: \~240 MB
* **Fields**: reviewerID, asin, rating, timestamp, reviewText, summary

Convert JSON to CSV locally or test AWS Glue's automatic schema inference on JSON format directly.
