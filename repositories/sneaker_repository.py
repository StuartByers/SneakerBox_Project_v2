from db.run_sql import run_sql

from models.sneaker import Sneaker
from models.brand import Brand
import repositories.brand_repository as brand_repository


def save(sneaker):
    sql = "INSERT INTO sneakers (model, brand_id, price, listed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [sneaker.model, sneaker.brand.id, sneaker.price, sneaker.listed]
    results = run_sql(sql, values)
    id = results[0]['id']
    sneaker.id = id
    return sneaker


def select_all():
    sneakers = []

    sql = "SELECT * FROM sneakers"
    results = run_sql(sql)

    for row in results:
        brand = brand_repository.select(row['brand_id'])
        sneaker = Sneaker(row['model'], brand, row['price'], row['listed'], row['id'])
        sneakers.append(sneaker)
    return sneakers



def select(id):
    sneaker = None
    sql = "SELECT * FROM sneakers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = brand_repository.select(result['brand_id'])
        sneaker = Sneaker(result['model'], brand, result['price'], result['listed'], result['id'])
    return sneaker


def delete_all():
    sql = "DELETE FROM sneakers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sneakers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(sneaker):
    sql = "UPDATE sneakers SET (model, brand_id, price, listed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [sneaker.model, sneaker.brand.id, sneaker.price, sneaker.listed, sneaker.id]
    run_sql(sql, values)