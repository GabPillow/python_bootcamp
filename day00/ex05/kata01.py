languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for i in languages:
    print(f'{languages[i]} was created by {languages.get(i)}')
