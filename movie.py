#!/usr/bin/env python3
import csv
import sys

FILENAME = "movies.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()


def read_movies():
    movies = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()


def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except Exception as e:
        print(type(e), e)
        exit_program()


# Display the menu
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("find - Find a movie")   
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


# Add a new movie
def add_movie(movies):
    title = input("Name: ")
    while True:
        try:
            year = int(input("Year: "))
            movie = (title, year)
            movies.append(movie)
            write_movies(movies)
            print(f"{movie[0]} was added.\n")
            break
        except ValueError:
            print("Invalid entry for year, please try again.")


# Delete a movie from the list
def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
            if number < 1 or number > len(movies):
                print("There are no movies with that number. Please try again.")
            else:
                movie = movies.pop(number - 1)
                write_movies(movies)
                print(f"{movie[0]} was deleted.\n")
                break
        except ValueError:
            print("Invalid movie number. Please try again.")
            continue

def find(movie_list):
    title = input("Enter a movie title: ")
    found = False
    for movie in movie_list:
        if movie[0].lower() == title.lower():
            print(f"{movie[0]} was released in {movie[1]} and has an IMDB rating of {movie[2]}.\n")
            found = True
            break
    
    if not found:
        print(f"{title} was not found.\n")
        

# Display movies in the list
def list_movie(movie_list):
    # Test to see if there are movies in the list
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})")
        print()


def main():
    display_menu()
    # Create and initialize the movie list
    movie_list = read_movies()

    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movie(movie_list)
        elif command == "add":
            add_movie(movie_list)
        elif command == "del":
            delete_movie(movie_list)
        elif command.lower() == "find":
            find(movie_list)
        elif command.lower() == "exit":
            break
        else:            
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
    main()
