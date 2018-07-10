#!/bin/python3


MCQs = [{'question': 'What is the capital of Nepal?', 'options': ('Kathmandu', 'New Delhi', 'Beijing', 'Thimphu'),
         'answer': 'Kathmandu'},
        {'question': 'Who is the 45th president of the USA?',
         'options': ('Ronald Reagan', 'Richard Nixon', 'Donald Trump', 'George W Bush'), 'answer': 'Donald Trump'},
        {'question': 'Which is the capital of the USA?',
         'options': ('New York', 'Washington D.C.', 'Texas', 'California'), 'answer': 'Washington D.C.'}]

"""
for num, mcq in enumerate(MCQs, start=1):
    print('{}. {}'.format(num, mcq))
    print(mcq)
"""

print('Check your general knowledge !!!', '\n')
for index in range(len(MCQs)):
    print('{}. {}'.format(index + 1, MCQs[index]['question']))
    for num, opt in enumerate(MCQs[index]['options'], start=2):
        print('{}. {}'.format(chr(95 + num), opt), end=' ')
    print('\n')
