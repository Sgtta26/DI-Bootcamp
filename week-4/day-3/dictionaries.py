sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict["class"]['student']['marks']['history'])


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

# del sample_dict['name']
# del sample_dict['salary']

for key_rmv in keys_to_remove:

    if key_rmv in sample_dict:
        del sample_dict[key_rmv]

print(sample_dict)