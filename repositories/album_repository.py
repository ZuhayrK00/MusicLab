from db.run_sql import run_sql
import pdb
from models.album import Album
import repositories.artist_repository as artist_repository

# title, genre, artist, id=None
def save(album):
    # pdb.set_trace()
    sql = 'INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *'
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id 
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row["title"], row["genre"], artist, row['id'])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result["title"], result["genre"], artist)
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def find_albums_by_artist(artist):
    artist_albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]

    results = run_sql(sql, values)
    if results:
        for row in results:
            album = Album(row["title"], row["genre"], row["artist_id"], row["id"])
            artist_albums.append(album)
    return artist_albums

def update(album):
    sql = 'UPDATE albums SET (title, genre, artist_id) = ROW(%s, %s, %s) WHERE id = %s'
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

def delete(id):
    # pdb.set_trace()
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)