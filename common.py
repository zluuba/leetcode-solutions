def get_solution_url(level, title):
    """
    Makes url for solution in following format:
    https://github.com/zluuba/leetcode/blob/main/[level]/%5B[task_num]%5D-[task_name].py
    """

    levels = {1: 'easy-level', 2: 'medium-level', 3: 'hard-level', 4: 'SQL'}

    url = 'https://github.com/zluuba/leetcode/blob/main/'
    url += levels[level] + '/'

    task_num, task_name = title.split('. ')
    url += f'%5B{task_num}%5D'

    new_name = '-'.join(map(lambda word: word.lower(), task_name.split()))
    url += f'-{new_name}.py'

    return url


level = 2
name = '235. Lowest Common Ancestor of a Binary Search Tree'
print(get_solution_url(level, name))
