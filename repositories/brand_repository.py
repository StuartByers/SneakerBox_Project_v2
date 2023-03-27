from db.run_sql import run_sql

from models.brand import Brand
from models.sneaker import Sneaker


def save(brand):
    sql = "INSERT INTO brands (first_name) VALUES (%s) RETURNING *"
    values = [brand.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    brand.id = id
    return brand


def select_all():
    brands = []

    sql = "SELECT * FROM brands"
    results = run_sql(sql)

    for row in results:
        brand = Brand(row['name'], row['id'])
        brands.append(brand)
    return brands


def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = Brand(result['name'], result['id'])
    return brand


def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(brand):
    sql = "UPDATE brands SET (name) = (%s) WHERE id = %s"
    values = [brand.name, brand.id]
    run_sql(sql, values)

def sneakers(brand):
    sneakers = []

    sql = "SELECT * FROM sneakers WHERE brand_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)

    for row in results:
        sneaker = sneaker(row['model'], row['brand_id'], row['price'], row['listed'], row['id'] )
        sneakers.append(sneaker)
    return sneakers