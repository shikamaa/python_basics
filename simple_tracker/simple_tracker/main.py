import tracker, time

config_path = '/home/john/python_homeworks/python_basics/simple_tracker/config/config.txt'

interval_val = 0
try:
    with open(config_path, 'r') as f:
        file_content = f.read().strip()
        interval_val = int(file_content)

        print('File content:\n',interval_val)

except FileNotFoundError:
    print(config_path, 'is not found')

except Exception as e:
    print('An error occured')

Tracker1 = tracker.Tracker()

try:
    while True:
        Tracker1.increment()
        print(Tracker1)
        Tracker1.save_to_file()

        time.sleep(interval_val)
finally:
    pass      
