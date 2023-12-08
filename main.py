file_text = "text.txt"
word = input("Введіть слово для пошуку: ")

try:
    with open(file_text, "r") as file:
        content = file.read()
        paragraphs = content.split('\n\n')
        found_paragraphs = []

        for i, paragraph in enumerate(paragraphs, 1):
            if word.lower() in paragraph.lower():
                found_paragraphs.append((i, paragraph))

        if found_paragraphs:
            print(f"\nЗнайдені абзаци, які містять слово '{word}':\n")
            for i, paragraph in found_paragraphs:
                print(f"Абзац {i}:\n{paragraph}\n")
        else:
            print(f"Слово '{word}' не знайдено в жодному абзаці.")
except FileNotFoundError:
    print(f"Файл '{file_text}' не знайдено.")
except Exception :
    print("Виникла помилка")

