import os
with open('README.md', 'w+') as f_:
    if not f_.read():
        for i in os.listdir(os.getcwd()):
            if os.path.join(os.getcwd(), i) != __file__ and os.path.splitext(i)[1] == '.py':
                print(i)
                with open(i, 'r') as f:
                    content = f.read()
                print(content)
                f_.write(f'{i}:\n```python\n{content}\n```\n')