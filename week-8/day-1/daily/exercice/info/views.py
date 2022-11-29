from django.shortcuts import render

# Create your views here.


def get_people(request):
    people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
    context = {'people':people}
    return render(request,'people.html',context)

# people.sort(key= lambda person: person:['age'])


def get_person(request, id):
    people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
context = {}

for person in people:
    if person['id']== id:
        context['person']= person
return render(request,'people.html',context)


