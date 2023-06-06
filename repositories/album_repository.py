import pdb
from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
    albums = []

    sql = "SELECT * FROM album"
    result = run_sql(sql)

    for row in result:
        artist = artist_repository.select(row[artist.id])
        album = Album(
            row['title'],
            artist,
            row['genre'],
            row['id'],
        )
        albums.append(album)
    return albums

def select_by_id(id):
    album = None
    sql = "SELECT * FROM album WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        artist = artist_repository.select(result[artist.id])
        album = Album(
            result['title'],
            artist,
            result['genre'],
            result['id'],
        )
    return album

def save(album):
    sql = "INSERT INTO album (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    result = run_sql(sql, values)
    id = result[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM album"
    run_sql(sql)

def delete(album):
    sql = "DELETE FROM album WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE album SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)
    

