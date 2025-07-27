# Amazon-related Datasets for S3 Ingestion and Pipeline Practice

## 1. Amazon Review and Metadata (UCSD, 2018)

* **Description**: Reviews and product metadata from 1996 to 2018 across categories.

* **Formats**: JSON or CSV (after conversion)

* **Download Page**:
  [https://nijianmo.github.io/amazon/](https://nijianmo.github.io/amazon/)

* **Example Direct Links**:

  * Books reviews: [https://datarepo.eng.ucsd.edu/mcauley\_group/data/amazon\_v2/categoryFilesSmall/Books.json.gz](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Books.json.gz)
  * Electronics reviews: [https://datarepo.eng.ucsd.edu/mcauley\_group/data/amazon\_v2/categoryFilesSmall/Electronics.json.gz](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Electronics.json.gz)
  * Metadata (Books): [https://datarepo.eng.ucsd.edu/mcauley\_group/data/amazon\_v2/metaFiles2/meta\_Books.json.gz](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/metaFiles2/meta_Books.json.gz)

## 2. Stanford SNAP Amazon Review Dataset (1995–2013)

* **Description**: 34 million reviews categorized by product domain.

* **Format**: JSON

* **Download Page**:
  [https://snap.stanford.edu/data/web-Amazon.html](https://snap.stanford.edu/data/web-Amazon.html)

* **Example Direct Links**:

  * Electronics: [https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews\_Electronics\_5.json.gz](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Electronics_5.json.gz)
  * Books: [https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews\_Books\_5.json.gz](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Books_5.json.gz)

## 3. Amazon Reviews 2023 (McAuley Lab via HuggingFace)

* **Description**: Over 570 million reviews with rich metadata.

* **Format**: Parquet (requires conversion for CSV-based pipelines)

* **Download Page**:
  [https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)

* **HuggingFace CLI Required**:

  ```bash
  pip install datasets
  from datasets import load_dataset
  load_dataset("McAuley-Lab/Amazon-Reviews-2023", split="train[:1%]")
  ```

## 4. Amazon M2 Dataset (Shopping Sessions)

* **Description**: Real user interaction sessions, multilingual.

* **Download Page**:
  [https://github.com/awslabs/amazon-multilingual-data-release](https://github.com/awslabs/amazon-multilingual-data-release)

* **Direct CSV Link** (Session data):
  [https://raw.githubusercontent.com/awslabs/amazon-multilingual-data-release/main/datasets/amazon\_shopping\_sessions\_en.csv](https://raw.githubusercontent.com/awslabs/amazon-multilingual-data-release/main/datasets/amazon_shopping_sessions_en.csv)

## 5. Amazon MAVE Dataset (Attribute Extraction)

* **Description**: Annotated product titles and attributes.

* **Download Page**:
  [https://github.com/amazon-science/mave](https://github.com/amazon-science/mave)

* **Direct CSV Link**:
  [https://raw.githubusercontent.com/amazon-science/mave/main/data/annotations.csv](https://raw.githubusercontent.com/amazon-science/mave/main/data/annotations.csv)

---

## Suggested Initial Dataset to Ingest

Use this to start with Glue Crawlers, Athena, and S3:

* Dataset: `Books.json.gz`
* Link: [https://datarepo.eng.ucsd.edu/mcauley\_group/data/amazon\_v2/categoryFilesSmall/Books.json.gz](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Books.json.gz)
* File size: \~240 MB
* Contents: userID, itemID, rating, timestamp, reviewText, summary

You can convert JSON to CSV before upload or test Glue's automatic schema inference.
