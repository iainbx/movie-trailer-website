import fresh_tomatoes
import media


# create movie list and add movie objects
movies = []
movies.append(media.Movie("Casablanca",
                          "https://upload.wikimedia.org/wikipedia/"
                          "commons/b/b3/CasablancaPoster-Gold.jpg",
                          "https://www.youtube.com/watch?v=BkL9l7qovsE",
                          "Of all the gin joints, in all the towns,"
                          " in all the world, she walks into mine."))
movies.append(media.Movie("Jaws",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/e/eb/JAWS_Movie_poster.jpg",
                          "https://www.youtube.com/watch?v=U1fu_sA7XhE",
                          "You're gonna need a bigger boat."))
movies.append(media.Movie("The Shining",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/2/25/The_Shining_poster.jpg",
                          "https://www.youtube.com/watch?v=3b726feAhdU",
                          "Heeere's Johnny!"))
movies.append(media.Movie("Alien",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/c/c3/Alien_movie_poster.jpg",
                          "https://www.youtube.com/watch?v=bEVY_lonKf4",
                          "I can't lie to you about your chances, but..."
                          " you have my sympathies."))
movies.append(media.Movie("The Imitation Game",
                          "http://ia.media-imdb.com/images/M/"
                          "MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@."
                          "_V1_SY317_CR0,0,214,317_AL_.jpg",
                          "https://www.youtube.com/watch?v=S5CjKEFb-sM",
                          "Think of it. A digital computer."
                          " Electrical brain."))
movies.append(media.Movie("The Good, The Bad, And The Ugly",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                          "https://www.youtube.com/watch?v=WCN5JJY_wiA",
                          "You see, in this world there's two kinds of people,"
                          " my friend: Those with loaded guns and those who"
                          " dig. You dig."))
movies.append(media.Movie("The Matrix",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/c/c1/The_Matrix_Poster.jpg",
                          "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                          "Never send a human to do a machine's job."))
movies.append(media.Movie("Fargo",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/a/ac/Fargo.jpg",
                          "https://www.youtube.com/watch?v=h2tY82z3xXU",
                          "You're darn tootin'!"))
movies.append(media.Movie("Pulp Fiction",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/8/82/Pulp_Fiction_cover.jpg",
                          "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                          "They call it a 'Royale with cheese'."))
movies.append(media.Movie("The Commitments",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/8/88/Commitments_poster.jpg",
                          "https://www.youtube.com/watch?v=3paf2TLrgsg",
                          "Do you not get it, lads? The Irish are the blacks "
                          "of Europe. And Dubliners are the blacks of Ireland."
                          " And the Northside Dubliners are the blacks of"
                          " Dublin. So say it once, say it loud: I'm black and"
                          " I'm proud."))
movies.append(media.Movie("The Terminator",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/7/70/Terminator1984movieposter.jpg",
                          "https://www.youtube.com/watch?v=lHz95RYUbik",
                          "I'll be back!"))
movies.append(media.Movie("A Fish Called Wanda",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/4/4f/A_Fish_Called_Wanda_DVD.jpg",
                          "https://www.youtube.com/watch?v=dqAJUlSRCwo",
                          "Don't call me stupid."))

# generate HTML file and open in browser
fresh_tomatoes.open_movies_page(movies)
