import FileInfo

print("Привет! Это плохо написанная программа.")
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"
try:
    open(filename, 'r')
    File1 = FileInfo.F_Info(filename, FileInfo.CntWords(filename),
                            FileInfo.CntSentences(filename),
                            FileInfo.RepeatWords(filename),
                            FileInfo.Cnt_Vowels(filename),
                            FileInfo.Cnt_Consonants(filename))
    print(f"Имя файла: {File1.filename}")
    print(f"Количество слов в файле: {File1.words}")
    print(f"Количество предложений в файле: {File1.sentences}")
    print(f"Самые часто встречающиеся слова: {File1.repeatWords}")
    print(f"Кол-во гласных в файле: {File1.vowels}")
    print(f"Кол-во согласных в файле: {File1.consonants}")
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
