# 📚 Alphabetical Dictionary with Linked Lists in Python

This project is a simple command-line dictionary application written in Python. It uses **linked lists** to store and manage words alphabetically by their starting letter (A-Z).

Each letter has its own linked list, and words are added to the appropriate list based on their first character. The program supports loading words from a file, displaying specific letter lists, and finding the letter with the **least number of words** or the **longest word**.

## 🔧 Features

- ✅ Load words from a text file (`words.txt`)
- ✅ Organize words into 26 linked lists (A-Z)
- ✅ Display words of a specific letter
- ✅ Find the letter with the **least words**
- ✅ Find the letter with the **longest word**
- ✅ Simple text-based menu for interaction

## 📁 File Structure

```bash
project-folder/
│
├── words.txt         # Your input file with words
├── main.py           # Main Python file (your code)
└── README.md         # This file
```

## 🧠 How It Works

1. **Initialization**: A list of 26 `LinkedList` objects is created for each letter.
2. **File Loading**: Reads words from `words.txt`, splits by whitespace, and adds them to the corresponding list.
3. **Linked List Operations**: Each list supports:
   - `add(word)`: Add a word to the end
   - `traverse()`: Return all words in the list
   - `count()`: Return the number of words
   - `longest_word()`: Find the longest word in the list

4. **Menu Options**:
   - Display list for a letter (e.g., `a`)
   - Find the letter with the **least words**
   - Find the letter with the **longest word**
   - Exit

## 📂 Example Input (`words.txt`)

```
apple armadillo ant
banana boat bottle
car cat crane
zebra zoom
```

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Place your `words.txt` file in the same directory.
3. Run the program:

```bash
python main.py
```

## 💡 Educational Use

This project is ideal for students learning:

- Linked List data structures
- File input/output in Python
- String manipulation
- Basic menu-based CLI applications

## 📜 License

This project is for educational purposes and is provided under the [MIT License](LICENSE).
