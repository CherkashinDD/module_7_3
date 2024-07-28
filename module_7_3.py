class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    new_text = text.replace(punct, '')
                all_words[file_name] = new_text.split()
        return all_words

    def find(self, word):
        position_word = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                position_word[file_name] = words.index(word) + 1  # Добавляю позицию слова (начиная с 1)
        return position_word

    def count(self, word):
        count_words = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            count_words[file_name] = words.count(word)
        return count_words


# import string
# class WordsFinder:
#
#     def __init__(self, *file_names):
#         self.file_names = file_names
#
#     def get_all_words(self):
#         all_words = {}
#         for file_name in self.file_names:
#             with open(file_name, encoding='utf-8') as file:
#                 text = file.read().lower()
#                 not_punctuation = str.maketrans('', '', string.punctuation + '–')
#                 new_text = text.translate(not_punctuation)
#                 all_words[file_name] = new_text.split()
#         return all_words
#
#     def find(self, word):
#         position_word = {}
#         word = word.lower()
#         for file_name, words in self.get_all_words().items():
#             if word in words:
#                 position_word[file_name] = words.index(word) + 1  # Добавляю позицию слова (начиная с 1)
#         return position_word
#
#     def count(self, word):
#         count_words = {}
#         word = word.lower()
#         for file_name, words in self.get_all_words().items():
#             count_words[file_name] = words.count(word)
#         return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
