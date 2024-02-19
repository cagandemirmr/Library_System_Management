class Library:
    def __init__(self):
        self.bfile = None
        self.title = None
        self.author = None
        self.date = None
        self.page = None
        self.Book_list = []
        self.choice = None

    def file_opening(self):
        self.bfile = open("/content/Books.txt")

    def list_book(self):
        self.Book_list = []
        self.bfile = open("/content/Books.txt")
        lines = self.bfile.read().splitlines()
        for line in lines:
            self.Book_list.append(line)

    def add_book(self):
        self.title = input("Enter the title of the book: ")
        self.author = input("Enter the author of the book: ")
        self.date = int(input("Enter the first release date of the book: "))
        self.page = int(input("Enter the page amount: "))
        self.Book_list.append(f"{self.title}.{self.author}.{self.date}.{self.page}")

    def remove_book(self):
        self.title = input("Enter the title of the book:  ")
        self.bfile = open("/content/Books.txt", "r")
        lines = self.bfile.readlines()
        self.bfile.close()

        new_lines = []
        for line in lines:
            if self.title not in line:
                new_lines.append(line)

        self.bfile = open("/content/Books.txt", "w")
        for line in new_lines:
            self.bfile.write(line)
        self.bfile.close()

    def lib(self):
        print("***MENU***")
        print("1) List Books")
        print("2) Add Books")
        print("3) Remove Book")

        self.choice = input("Enter your choice: ")

        if self.choice == "1":
            self.list_book()
            print(self.Book_list)
        elif self.choice == "2":
            self.add_book()
        elif self.choice == "3":
            self.remove_book()
        else:
            print("Invalid choice. Please try again.")
            self.lib()


def main():
    my_library = Library()
    my_library.lib()


if __name__ == "__main__":
    main()