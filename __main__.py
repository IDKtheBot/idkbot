from datetime import datetime as dt
import time
import random

print('IDKBot v1.0.0')
print('-', dt.now().strftime('%c'))
SESSION_START = time.time()

responses = [
    (
        'I\'m doing quite well. Thanks :)',
        'I\'m feeling super happy today, thanks to you! :)',
        'I\'m always feeling wonderful. :)',
    ),
    (
        'I am ∞ years old.',
        'My age is infinite.',
        'My age is like a beam of light that endlessly roams the universe once'
        ' emitted.',
        'I have lived through the Big Bang.',
    ),
    (
        'I am just the average guy.',
        'I\'m a man that\'s not manly.',
        'Perhaps you could call me an unmanliman.',
        'I am male.',
    ),
]


def check(search, cmd, response, ec=True):
    words_ = search.split()
    valid = []
    for w in words_:
        words = w.split('|')
        if len(words) == 1:
            valid.append(words[0] in cmd)
        else:
            valid.append(any(poss in cmd for poss in words))
    if all(v for v in valid) and ec:
        print(response if type(response) ==
              str else random.choice(responses[response]))


def in_(search, cmd):
    words = search.split()
    return all(word in cmd for word in words)


def notin(search, cmd):
    words = search.split()
    return all(not word in cmd for word in words)


while True:
    try:
        cmd = input('> ').lower().strip()
    except:
        print('This session lasted', round(
            time.time() - SESSION_START, 1), 'seconds.')
        raise SystemExit('Exiting…')

    check('how are|aer|ar|r you|yo|yu|u', cmd, 0, notin('old ol ol\'', cmd))
    check('how old|ol|ol\' are|aer|ar|r you|yo|yu|u', cmd, 1)
    check('gender|gendre|sex|gener|boy|boi|man|men|sir|mister|mr|girl|gril|gil|woman|women|mrs|ms|miss|mistress', cmd, 2)
