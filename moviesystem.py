class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - Rating: {self.rating}/10"


class MovieSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, year, rating):
        movie = Movie(title, genre, year, rating)
        self.movies.append(movie)
        print(f"Movie '{title}' added successfully!")

    def list_movies(self):
        if not self.movies:
            print("No movies in the system.")
        else:
            for movie in self.movies:
                print(movie)

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def remove_movie(self, title):
        movie = self.find_movie(title)
        if movie:
            self.movies.remove(movie)
            print(f"Movie '{title}' removed successfully!")
        else:
            print(f"Movie '{title}' not found.")

    def update_movie(self, title, genre=None, year=None, rating=None):
        movie = self.find_movie(title)
        if movie:
            if genre:
                movie.genre = genre
            if year:
                movie.year = year
            if rating:
                movie.rating = rating
            print(f"Movie '{title}' updated successfully!")
        else:
            print(f"Movie '{title}' not found.")


if __name__ == "__main__":
    system = MovieSystem()

    while True:
        print("\nMovie System Menu:")
        print("1. Add Movie")
        print("2. List Movies")
        print("3. Find Movie")
        print("4. Remove Movie")
        print("5. Update Movie")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            year = input("Enter release year: ")
            rating = input("Enter movie rating (out of 10): ")
            system.add_movie(title, genre, year, rating)
        elif choice == "2":
            system.list_movies()
        elif choice == "3":
            title = input("Enter movie title to find: ")
            movie = system.find_movie(title)
            if movie:
                print(movie)
            else:
                print(f"Movie '{title}' not found.")
        elif choice == "4":
            title = input("Enter movie title to remove: ")
            system.remove_movie(title)
        elif choice == "5":
            title = input("Enter movie title to update: ")
            genre = input("Enter new genre (leave blank to keep current): ")
            year = input("Enter new release year (leave blank to keep current): ")
            rating = input("Enter new rating (leave blank to keep current): ")
            system.update_movie(title, genre or None, year or None, rating or None)
        elif choice == "6":
            print("Exiting Movie System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")