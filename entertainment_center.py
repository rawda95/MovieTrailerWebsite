import media
import fresh_tomatoes


#  A single movie object InseideOut
InseideOut = media.Moive('Inseide Out',
                         'https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg',
                         'https://www.youtube.com/watch?v=seMwpP0yeu4')

#  A single movie object zootopia
zootopia = media.Moive('zootopia',
                       'https://s3.amazonaws.com/oscars-img-abc/wp-content/uploads/2017/01/10125617/6523d73b04407f9f9a490cf03db41e5b25908690117a1759a4e5dba24708acfd.jpg',
                       'https://www.youtube.com/watch?v=yCOPJi0Urq4'
)

#  A single movie object up
up = media.Moive('UP',
                  'https://vignette.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816',
                  'https://www.youtube.com/watch?v=pkqzFUhGPJg')


#  A single movie object DespicableMe
DespicableMe = media.Moive('Despicable Me',
                            'https://images-na.ssl-images-amazon.com/images/I/81JKBIZxUVL._SL1500_.jpg',
                            'https://www.youtube.com/watch?v=euz-KBBfAAo')

#  A single movie object BossBaby
shrek = media.Moive('shrek',
                     'https://i.ytimg.com/vi/xNAXY5ukn-E/movieposter.jpg',
                     'https://www.youtube.com/watch?v=ooJJX3R42WM')

#  A single movie object BossBaby
BossBaby = media.Moive('Boss Baby',
                       'https://images-na.ssl-images-amazon.com/images/M/MV5BMTg5MzUxNzgxNV5BMl5BanBnXkFtZTgwMTM2NzQ3MjI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'https://www.youtube.com/watch?v=4a2KkiB9op0&pbjreload=10')


# list of all feverite moive
moiveList = [InseideOut, up, zootopia, DespicableMe, shrek, BossBaby]
# make site for moive
fresh_tomatoes.open_movies_page(moiveList)
