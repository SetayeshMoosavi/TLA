def check():
    incomplete = []
    if w and (q0, w[0]) in dictionary:
        for des in dictionary[(q0, w[0])]:
            incomplete.append([[(q[q0], w[0])], des, 1])
    if (q0, 'eps') in dictionary:
        for des in dictionary[(q0, 'eps')]:
            incomplete.append([[(q[q0], 'eps')], des, 0])
    while incomplete:
        path, where, alphabet = incomplete[0]
        if alphabet == len(w):
            if where in f:
                accepted.append(path + [q[where]])
            else:
                tmp = [[path, where]]
                while tmp:
                    pp, ww = tmp[0]
                    if ww in f:
                        accepted.append(pp + [q[ww]])
                        del tmp[0]
                        continue
                    if pp[-1][-1] == 'eps':
                        ind = -1
                        while pp[ind - 1][-1] == 'eps':
                            ind -= 1
                        if q.index(pp[ind][0]) == ww:
                            del tmp[0]
                            continue
                    if (ww, 'eps') in dictionary:
                        for des in dictionary[(ww, 'eps')]:
                            tmp.append([pp + [(q[ww], 'eps')], des])
                        del tmp[0]
                    else:
                        failed.append(pp + [q[ww]])
                        del tmp[0]

            del incomplete[0]
            continue

        flag = True
        if path[-1][-1] == 'eps':
            ind = -1
            while ind - 1 >= 0 and path[ind - 1][-1] == 'eps':
                ind -= 1
            if q.index(path[ind][0]) == where:
                del incomplete[0]
                continue
        if (where, w[alphabet]) in dictionary:
            flag = False
            for des in dictionary[(where, w[alphabet])]:
                incomplete.insert(1, [path + [(q[where], w[alphabet])], des, alphabet + 1])
        if (where, 'eps') in dictionary:
            flag = False
            for des in dictionary[(where, 'eps')]:
                incomplete.insert(1, [path + [(q[where], 'eps')], des, alphabet])
        if flag:
            failed.append(path + [q[where]])
        del incomplete[0]


dictionary = {}
q = input("Please enter all the states separated with space: ").split(' ')
sigma = input('Please enter the alphabets separated with space: ').split(' ')
sigma.append("eps")
q0 = int(input("Please enter the index of the first state: "))
f = list(map(int, input('Please enter the index of the final states separated with space: ').split(' ')))
w = list(input("Please enter a string: "))

for item in range(len(q)):
    for item_ in sigma:
        inp = input("Please enter the index of all the states we can go from " + str(q[item]) + " with " + str(item_) +
                    ' (space separated): ')
        if inp:
            dictionary[(item, item_)] = list(map(int, inp.split(" ")))

failed = []
accepted = []
check()
if not accepted:
    print("This NFA doesn't accept the string.")
    print('All failed paths: ')
    for line in failed:
        print(line)
else:
    print("This NFA accepts the string.")
    print('All accepted paths: ')
    for line in accepted:
        print(line)
    if not failed:
        print('No failed path.')
    else:
        print('All failed paths: ')
        for line in failed:
            print(line)
