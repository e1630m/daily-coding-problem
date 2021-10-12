def file_system(s):
    folders, path = {}, []
    for f in s.split('\n'):
        depth, name = f.count('\t'), f.strip('\t')
        is_file = '.' in f
        current = folders
        for parent in path[:depth]:
            current = current[parent.strip('\t')]
        current[name] = (len(''.join(path) + name) + depth) if is_file else {}
        path = path[:depth]
        path.append(name)
    return folders


def find_max_int(folders):
    maximum = 0
    for v in folders.values():
        maximum = max(maximum, v if type(v) == int else find_max_int(v))
    return maximum


s = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
ps = s.replace('\n', '\\n').replace('\t', '\\t')
expected = len('dir/subdir2/subsubdir2/file2.ext')
print(f'find_max_int(file_system({ps})): {find_max_int(file_system(s))}, '
      f'expected: {expected}')

s = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
ps = s.replace('\n', '\\n').replace('\t', '\\t')
expected = len('dir/subdir2/file.ext')
print(f'find_max_int(file_system({ps})): {find_max_int(file_system(s))}, '
      f'expected: {expected}')
