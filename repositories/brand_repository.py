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
        brand = brand(row['name'], row['id'] )
        brands.append(brand)
    return brands


def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        brand = brand(result['first_name'], result['last_name'], result['id'] )
    return brand


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values)

def tasks(user):
    tasks = []

    sql = "SELECT * FROM tasks WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        task = Task(row['description'], row['user_id'], row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks