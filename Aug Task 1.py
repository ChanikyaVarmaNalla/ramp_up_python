class StatementProcessor:
    def __init__(self, statement):
        self.statement = statement

    def count_characters(self):
        return len([char for char in self.statement if char.isalnum()])

    def count_duplicate_characters(self):
        return len([char for char in set(self.statement) if self.statement.count(char) > 1 and char.isalnum()])

    def count_words(self):
        words = self.statement.split()
        return len(words)

    def count_duplicate_words(self):
        words = self.statement.split()
        return len([word for word in set(words) if words.count(word) > 1])

    def reverse_characters(self):
        return ''.join(reversed(self.statement))

    def reverse_words(self):
        words = self.statement.split()
        return ' '.join(word[::-1] for word in words)

    def remove_duplicate_characters(self):
        unique_chars = []
        char_set = set()
        for char in self.reverse_words():
            if char not in char_set:
                unique_chars.append(char)
                char_set.add(char)
        return ''.join(unique_chars)


dynamic_input = input("Enter a statement: ")
processor = StatementProcessor(dynamic_input)

total_characters = processor.count_characters()
print(f"Total characters in the statement: {total_characters}")

total_duplicate_characters = processor.count_duplicate_characters()
print(f"Total duplicate characters in the statement: {total_duplicate_characters}")

total_words = processor.count_words()
print(f"Total words present in the statement: {total_words}")

total_duplicate_words = processor.count_duplicate_words()
print(f"Total duplicate words in the statement: {total_duplicate_words}")

reversed_characters = processor.reverse_characters()
print(f"Reversed characters: {reversed_characters}")

reversed_words = processor.reverse_words()
print(f"Reversed words: {reversed_words}")

new_statement = processor.reverse_words()
print(f"New statement from reversed words: {new_statement}")

unique_statement = processor.remove_duplicate_characters()
print(f"New statement without duplicate characters: {unique_statement}")
