# Дана директорія. Визначити кількість файлів в ній та об’єм який вони займають, не використовуючи os.walk.
# а) Зробити рекурсивний варіант
import os


def walk_recur(paths):
    """
    Outer function of recursive os.walk analog. Was made to prevent global parameters and keep everything in inner
    scope of this function
    :param paths: a path to recursively walk
    :return: overall amount of files in the given directory 'path'
             followed by print of overall size of all files in this directory
             followed by tuple consisting of list of tuples with directories and files in them(os.walk like)

    """
    counter = 0
    size = 0.0
    path_lst = []

    def dig_dir(paths):
        """
        Inner function. Does the main work of recursive path exploration
        :param paths: a path to recursively walk(gets from outer function)
        :return: ''
        """
        path_lst.append((paths,
                         [i for i in os.listdir(paths) if os.path.isdir(os.path.join(os.path.abspath(paths), i))],
                         [i for i in os.listdir(paths) if os.path.isfile(os.path.join(os.path.abspath(paths), i))]))
        for newpath in os.listdir(paths):
            walkpath = os.path.join(os.path.abspath(paths), newpath)
            if os.path.isdir(walkpath):
                dig_dir(walkpath)
            else:
                nonlocal counter
                counter += 1
                nonlocal size
                size += os.path.getsize(walkpath)
    dig_dir(paths)
    return counter, str(size/1024)+' kbyte', path_lst


# б) Зробити нерекурсивний варіант
def walk_nonrecur(paths):
    """
    Nonrecursive os.walk analog
    :param paths:  a path to nonrecursively walk in
    :return: prints list of all the directories and files
             followed by print of overall amount of files in given directory 'path'
             followed by print of overall size of all files in this directory
    """
    counter = 0
    size = 0.0
    paths_lst = [os.path.join(os.path.abspath(paths), i) for i in os.listdir(paths)]
    for newpath in paths_lst:
        if os.path.isdir(newpath):
            for j in os.listdir(newpath):
                paths_lst.append(os.path.join(os.path.abspath(newpath), j))
        else:
            size += os.path.getsize(newpath)
            counter += 1
    print(paths_lst)
    print(counter)
    print(size/1024, 'kbyte')


if __name__ == '__main__':
    print(walk_recur('..'))
    walk_nonrecur('..')
