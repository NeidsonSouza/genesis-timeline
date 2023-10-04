import plotly.express as px
import pandas as pd

GENESIS_CHARACTERS = [
    {
        'name':         'adam',
        'parenting_age': 130,
        'lifetime':      930,
    },
    {
        'name':          'seth',
        'parenting_age': 105,
        'lifetime':      912,
    },
    {
        'name':          'enosh',
        'parenting_age': 90,
        'lifetime':      905,
    },
    {
        'name':          'Kenan',
        'parenting_age': 70,
        'lifetime':      910,
    },
    {
        'name':          'mahalalel',
        'parenting_age': 65,
        'lifetime':      895,
    },
    {
        'name':          'jared',
        'parenting_age': 162,
        'lifetime':      962,
    },
    {
        'name':          'enoch',
        'parenting_age': 65,
        'lifetime':      365,
    },
    {
        'name':          'mathuselah',
        'parenting_age': 187,
        'lifetime':      969,
    },
    {
        'name':          'lamech',
        'parenting_age': 182,
        'lifetime':      777,
    },
    {
        'name':          'noah',
        'parenting_age': 600 + 2 - 100,
        'lifetime':      950,
    },
    {
        'name':          'shem',
        'parenting_age': 100,
        'lifetime':      100 + 500,
    },
    {
        'name':          'Arphaxad',
        'parenting_age': 35,
        'lifetime':      35 + 403,
    },
    {
        'name':          'shelah',
        'parenting_age': 30,
        'lifetime':      30 + 403,
    },
    {
        'name':          'eber',
        'parenting_age': 34,
        'lifetime':      34 + 430,
    },
    {
        'name':          'peleg',
        'parenting_age': 30,
        'lifetime':      30 + 209,
    },
    {
        'name':          'reu',
        'parenting_age': 32,
        'lifetime':      32 + 207,
    },
    {
        'name':          'serug',
        'parenting_age': 30,
        'lifetime':      30 + 200,
    },
    {
        'name':          'nahor',
        'parenting_age': 29,
        'lifetime':      29 + 119,
    },
    {
        'name':          'terah',
        'parenting_age': 70,
        'lifetime':      70 + 135,
    },
    {
        'name':          'abraham',
        'parenting_age': 100,
        'lifetime':      100 + 75,
    },
    {
        'name':          'isac',
        'parenting_age': 60,
        'lifetime':      60 + 120,
    },
]

data = {
    'person': [person['name'] for person in GENESIS_CHARACTERS]
}

print(data)
