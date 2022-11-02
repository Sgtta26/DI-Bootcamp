sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key_rmv in keys_to_remove:

    if key_rmv in sample_dict:
        del sample_dict[key_rmv]

print(sample_dict)