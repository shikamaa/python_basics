import time
import random
import analyzer

config_path = '/home/john/python_homeworks/python_basics/simple_analyzer/config/config.txt'

interval = 0
sequence_length = 0

try:
    with open(config_path, 'r') as f:
        lines = f.readlines()
        interval = int(lines[0].split('=')[1].strip())
        sequence_length = int(lines[1].split('=')[1].strip())
        print('Interval:', interval)
        print('Sequence length:', sequence_length)
except FileNotFoundError:
    print(config_path, 'is not found')
except Exception as e:
    print('An error occurred:', e)

analyzer = analyzer.Analyzer()

try:
    while True:
        num = random.randint(1, 100)
        analyzer.add_number(num)

        if len(analyzer._lst) > sequence_length:
            analyzer._lst.pop(0)

        print(f'\nAdded number: {num}')
        print(f'Current sequence: {analyzer._lst}')
        print(f'Total even: {analyzer.even_count()}')
        print(f'Total odd: {analyzer.odd_count()}')
        print(f'Highest number: {analyzer.highest_number()}')
        print(f'Increasing pairs: {analyzer.increasing_pairs()}')

        current_seconds = time.localtime().tm_sec
        if len(analyzer._lst) >= sequence_length and current_seconds == 0:
            print('\nConditions met — stopping program.')
            break

        time.sleep(interval)

except KeyboardInterrupt:
    print('\nStopped.')
finally:
    pass

