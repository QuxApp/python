import quxt as _
from quxt import true
from quxt import false

users = [
  {
    'name': 'foo',
    'age': 8,
    'deleted': false,
  },
  {
    'name': 'bar',
    'age': 18,
    'deleted': false,
  },
  {
    'name': 'baz',
    'age': 13,
    'deleted': true,
  },
  {
    'name': 'qux',
    'age': 13,
    'deleted': false,
  },
]

result = _.filter(users, _.matches({ 'name': 'foo' }))
print(result)

result = _.partition(users,  _.matches({ 'name': 'foo' }))
print(result)