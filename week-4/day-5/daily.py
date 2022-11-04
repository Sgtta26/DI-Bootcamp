
items = input("Write many words separated by comma:")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))