class Node:
    def __init__(self, word):
        self.word = word
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, word):
        new_node = Node(word)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        words = []
        current = self.head
        while current:
            words.append(current.word)
            current = current.next
        return words

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def longest_word(self):
        current = self.head
        longest = ""
        while current:
            if len(current.word) > len(longest):
                longest = current.word
            current = current.next
        return longest



dictionary = [LinkedList() for _ in range(26)]


def add_word_in_dictionary(word):
    index = ord(word[0].lower()) - ord('a')
    if 0 <= index < 26:
        dictionary[index].add(word)


def load_words_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  
                for word in words:
                    add_word_in_dictionary(word.lower())  
        print("Words have been successfully loaded from the file.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def display_words(letter):
    index = ord(letter.lower()) - ord('a')
    if 0 <= index < 26:
        words = dictionary[index].traverse()
        if words:
            print(" -> ".join(words) + " -> None")
            print(f"This list has {len(words)} words")
        else:
            print(f"No words found for letter '{letter}'.")
    else:
        print("Invalid letter.")


def letter_with_the_least_words():
    min_count = float('inf')
    letter = None
    for i, ll in enumerate(dictionary):
        count = ll.count()
        if count < min_count and count > 0:  
            min_count = count
            letter = chr(i + ord('a'))
    if letter:
        print(f"The letter with the least words is: {letter} ({min_count})")
    else:
        print("No words found in the dictionary.")


def letter_with_the_longest_word():
    max_length = 0
    longest_word = ""
    letter = None
    for i, ll in enumerate(dictionary):
        word = ll.longest_word()
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
            letter = chr(i + ord('a'))
    if letter:
        print(f"The letter with the longest word is: {letter} ({longest_word})")
    else:
        print("No words found in the dictionary.")


def menu():
    while True:
        print("\n1- Display the list of a single letter")
        print("2- Display the letter with the least words")
        print("3- Display the letter of the longest word")
        print("4- Exit")
        choice = input("> Please enter your choice: ")

        if choice == "1":
            letter = input("Which letter do you want to see? = ")
            display_words(letter)
        elif choice == "2":
            letter_with_the_least_words()
        elif choice == "3":
            letter_with_the_longest_word()
        elif choice == "4":
            print("Bye.")
            break
        else:
            print("Wrong, Invalid choice. Try again")



load_words_from_file("words.txt")
menu()
