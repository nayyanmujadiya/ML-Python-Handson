import pandas as pd

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

'''
Suppose you wanted to add a column indicating the type of animal
that each food came from. Let’s write down a mapping of each distinct
meat type to the kind of animal :
'''

'''
The map method on a Series accepts a function or dict-like object containing a
mapping, but here we have a small problem in that some of the meats are
capitalized and others are not. Thus, we need

to convert each value to
lowercase using the str.lower Series method:
'''

lowercased = data['food'].str.lower()
lowercased

data['animal'] = lowercased.map(meat_to_animal)
data
