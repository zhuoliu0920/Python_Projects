#!/usr/bin/env python3

from functools import reduce
import re

def build_dict(filename):
    movie_by_actors = {}
    with open(filename, 'r') as m_file:
        for line in m_file.readlines():
            info = list(map(str.strip, line.strip().split(',')))
            for movie in set(info[1:]):
                if movie in movie_by_actors:
                    movie_by_actors[movie] = movie_by_actors[movie] | set([info[0]])
                else:
                    movie_by_actors[movie] = set([info[0]])
    return(movie_by_actors)

def find_coactors_by_movies(movie_by_actors, movies, operation):
    ops = {'&': (lambda x,y: x&y), '|': (lambda x,y: x|y), '^': (lambda x,y: x^y)}
    return( ops[operation](movie_by_actors[movies[0]], movie_by_actors[movies[1]]) )

def find_coactors_by_actor(movie_by_actors, actor_name):
    coactors_by_movies = [a-{actor_name} for a in movie_by_actors.values() if actor_name in a]
    return( reduce(lambda x,y: x|y, coactors_by_movies) )





def main():
    actor_dict = build_dict('movies.txt')
    option = input("You have 2 options:\n a. Give me two movies\n b. Give me name of an actor\n")
    if option == 'a':
        info = input("""Give me 2 movies separated by (&,|,^): """)
        movies = list( map(str.strip, re.split("\&|\^|\|", info)) )
        operation = info.replace(movies[0],"").replace(movies[1],"").strip()
        coactors = find_coactors_by_movies(actor_dict, movies, operation)
        print("Co-actors for {} {} {} are: {}".format(movies[0],operation,movies[1],coactors))
    elif option == 'b':
        actor_name = input("Give me name of an actor and find his/her co-actors: ")
        coactors = find_coactors_by_actor(actor_dict, actor_name)
        print("Co-actors for {} are: {}".format(actor_name, coactors))
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
        

