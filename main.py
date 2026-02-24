import re

print("1 задание")

with open("task1_ru.txt", "r", encoding="utf-8") as file:
    text = file.read()

hyphen_words = re.findall(r"\b\w+-\w+\b", text)

print("\nСлова с дефисом:")
for word in hyphen_words:
    print(word)

brackets = re.findall(r"\(.*?\)", text)

print("\nИнформация в круглых скобках:")
for b in brackets:
    print(b)


print("\n 2 задание")

with open("task2.html", "r", encoding="utf-8") as file:
    html = file.read()

links = re.findall(r"https?://[^\s\"']+\.com[^\s\"']*", html)

print("\nСсылки .com:")
for link in links:
    print(link)


print("\n3 задание")

with open("task3.txt", "r", encoding="utf-8") as file:
    data = file.read()

ids = re.findall(r"\b\d+\b", data)
emails = re.findall(r"\S+@\S+", data)
dates = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", data)
sites = re.findall(r"https?://\S+", data)
names = re.findall(r"\b[A-ZА-Я][a-zа-я]+\b", data)

print("\nID:")
print(ids)

print("\nEmails:")
print(emails)

print("\nDates:")
print(dates)

print("\nSites:")
print(sites)

print("\nNames:")
print(names)