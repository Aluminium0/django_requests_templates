# Django Phone Catalog Homework

Standalone homework for importing a phone catalog from CSV into a Django database.

## Run

```bash
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py import_phones
python3 manage.py runserver
```

## Pages

- `/catalog` - phone catalog
- `/catalog?sort=name` - sort by name
- `/catalog?sort=min_price` - cheapest first
- `/catalog?sort=max_price` - most expensive first
- `/catalog/iphone-x` - phone detail page by slug
