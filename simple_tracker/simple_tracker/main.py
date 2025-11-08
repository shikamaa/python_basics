config_path = '/home/john/python_homeworks/python_basics/simple_tracker/config/config.txt'

try:
    with open(config_path, 'r') as f:
        file_content = f.read()
        print('File content:\n',file_content)
except FileNotFoundError:
    print(config_path, 'is not found')
except Exception as e:
    print('An error occured')


