import FileInfo

print("Привет! Это плохо написанная программа.")
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")
content = ""
filename = "sample.txt"
try:
    with open(filename, 'r') as file:
        content = file.read()

except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
File1 = FileInfo.F_Info(filename, FileInfo.Cnt_words(content),
                        FileInfo.Cnt_sentences(content),
                        FileInfo.Repeat_words(content),
                        FileInfo.Cnt_vowels(content),
                        FileInfo.Cnt_consonants(content))
print(f"Имя файла: {File1.filename}")
print(f"Количество слов в файле: {File1.words}")
print(f"Количество предложений в файле: {File1.sentences}")
print(f"Самые часто встречающиеся слова: {File1.repeatWords}")
print(f"Кол-во гласных в файле: {File1.vowels}")
print(f"Кол-во согласных в файле: {File1.consonants}")
