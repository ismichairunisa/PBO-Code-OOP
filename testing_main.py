class Buku:
    def __init__(self):
        self.judul = ""
        self.pengarang = ""

def main():
    obj = Buku()
    obj.judul = "Python for Beginners"
    obj.pengarang = "John Smith"
    print(f"Buku '{obj.judul}' oleh {obj.pengarang}")

if __name__ == '__main__':
    main()
