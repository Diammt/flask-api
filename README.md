# API

## Installation of dependencies
All dependencies are in **requirements.txt** file.

```python
pip install -r requirements.txt
```
We recommande you to work in [virtual environment](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4463278-travaillez-dans-un-environnement-virtuel)

## Usage
* For SQLite3
  * Set `sqlite`variable to `True` in `config.py` file 
  * Create a `database.db` file(you have to install sqlite3 in your system)
  
* For mariadb(mysql) 
  * Set `sqlite` variable to `False` in `config.py` file 
  * Custom `credentials`  in `config.py` file 
  
* Initialize all table by typing:
```python
FLASK_APP=run.py flask init-db
```
* If you are in developement launch:
```python
FLASK_APP=run.py flask dev-migration
```
* If you are in production launch:
```python
FLASK_APP=run.py flask prod-migration
```
* Launch `python run.py`
* Finally run
  ```python
  FLASK_APP=run.py flask api-generate
  ```
  and go to `{{base_url}}/swagger` to see the documantation of the API

## Note
* A collection for SWAGGER is available at endpoint `/spec`

* If you want to generate a collection for POSTMAN you can type
  ```python
  flask2postman run.app --name "API Collection" --folders > collection.json -i
  ```
  You can probably need to [convert](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#converting-postman-collections-from-v1-to-v2) the `collection.json` file into `2.0.0 version` before use it