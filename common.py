from string import ascii_lowercase, digits
import subprocess


BASE = 'https://github.com/zluuba/leetcode/blob/main/'
LEVELS = {1: 'easy-level', 2: 'medium-level', 3: 'hard-level', 4: 'SQL'}
CHARS = ascii_lowercase + digits + '-'
EXTENSION = '.py'


def get_filtered_word(word):
    return ''.join(filter(lambda char: char in CHARS, word.lower()))


def get_solution_url(problem_level, title):
    """ Makes url for solution in following format:
    https://github.com/zluuba/leetcode/blob/main/[level]/%5B[task_num]%5D-[task_name].py
    """

    url = BASE + LEVELS[problem_level] + '/'

    task_num, task_name = title.split('. ')
    url += f'%5B{task_num}%5D-'

    processed_task_name = filter(
        lambda word: word,
        map(lambda word: get_filtered_word(word), task_name.split()),
    )
    url += '-'.join(processed_task_name) + EXTENSION

    return url


level = 2
name = ""
solution_url = get_solution_url(level, name)

# copy solution_url to clipboard (MacOS)
subprocess.run("pbcopy", text=True, input=solution_url)
