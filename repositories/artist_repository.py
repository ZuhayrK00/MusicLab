import pdb
from db.run_sql import run_sql
from models.artist import Artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    result = run_sql(sql)

    for row in result:
        artist = Artist(
            row['artist_name']
        )
        artists.append(artist)
    return artists

def select_by_id(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        artist = Artist(
            result['artist_name'],
            result['id']
            )
    return artist

def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]

    result = run_sql(sql, values)
    id = result[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [artist.artist_name, artist.id]
    run_sql(sql, values)