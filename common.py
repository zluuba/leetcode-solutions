from string import ascii_lowercase, digits


def get_solution_url(level, title):
    """
    Makes url for solution in following format:
    https://github.com/zluuba/leetcode/blob/main/[level]/%5B[task_num]%5D-[task_name].py
    """

    levels = {1: 'easy-level', 2: 'medium-level', 3: 'hard-level', 4: 'SQL'}
    correct_chars = ascii_lowercase + digits + '-'

    url = f'https://github.com/zluuba/leetcode/blob/main/{levels[level]}/'

    task_num, task_name = title.split('. ')
    url += f'%5B{task_num}%5D'

    new_name = '-'.join(map(lambda word: word.lower(), task_name.split()))
    filtered_name = ''.join(filter(lambda char: char in correct_chars, new_name))
    url += f'-{filtered_name}.py'

    url = url.replace("'", "").replace("---", "-")

    return url


level = 2
name = ""
print(get_solution_url(level, name))
