import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "bottoms"

# searching the name
search = ia.search_movie(name)


# loop for printing the name and id
for i in range(len(search)):

    # getting the id
    id = search[i].movieID

    # printing it
    print(search[i]['title'] + " : " + id)
