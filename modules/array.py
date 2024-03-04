def package_remover(array):
    for i in range(len(array)):
        if array[i].startswith('package:'):
            array[i] = array[i][len('package:'):]

    return array
