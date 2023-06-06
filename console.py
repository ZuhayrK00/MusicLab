import pdb

from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()


artist1 = Artist("Godspeed You! Black Emperor")
artist_repository.save(artist1)

artist2 = Artist('Nervana')
artist_repository.save(artist2)


# title, genre, artist, id=None
album1 = Album("G_d's Pee AT STATE'S END!", "Post-rock", artist1)
album_repository.save(album1)

album2 = Album("Nevermand", "Grunge Rock", artist2)
album_repository.save(album2)

artists = artist_repository.select_all()
albums = album_repository.select_all()

artists[1].name = "Nirvana"
artist_repository.update(artists[1])
# pdb.set_trace()

albums[1].title = "Nevermind"
album_repository.update(albums[1])


album = album_repository.select(albums[0].id)

artist = artist_repository.select(artists[0].id)

albums_by_artist = album_repository.find_albums_by_artist(artist2)

album_repository.delete(albums[0].id)
artist_repository.delete(artists[0].id)

result = album_repository.select_all()

for item in result:
    print(item.__dict__)

result = artist_repository.select_all()
for item in result:
    print(item.__dict__)

# pdb.set_trace()
