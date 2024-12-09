import re

with open('input.txt', 'r') as fichier:
    disk_map = fichier.readline().strip()

def decompress(disk_map) -> list:
    result = []
    id = 0
    isSpace = False
    for c in disk_map:
        for _ in range(int(c)):
            result.append(-1 if isSpace else id)
        if not isSpace:
            id += 1
        isSpace = False if isSpace else True
    return result

def getFreeSpace(disk_map : list, nb : int, max : int) -> int:
    for i in range(max):
        for j in range(0, nb + 1):
            if disk_map[i + j] != -1:
                break
            if j + 1 >= nb:
                return i
    return -1

def getFile(disk_map : list) -> tuple[int, int, int]:
    i = len(disk_map) - 1

    while i >= 0 and disk_map[i] == -1:
        i -= 1
        disk_map.pop()
    if i < 0:
        return None
    nb = disk_map[i]
    end = i

    while i >= 0 and disk_map[i] == nb:
        i -= 1
        disk_map.pop()

    return (nb, end - i, i + 1)

def removeFile(disk_map : list, file : tuple[int, int, int]) -> list:
    for i in range(file[2], file[1]):
        disk_map[i] = -1
    return disk_map

def removeEndDot(disk_map : list) -> list:
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != -1:
            break
        disk_map.pop()
    return disk_map


def compact(disk_map : list) -> list:
    copy = disk_map.copy()
    file = getFile(copy)
    while file != None:
        removeEndDot(disk_map)
        space = getFreeSpace(disk_map, file[1], file[2] + file[1])
        if space != -1:
            for i in range(space, space + file[1]):
                disk_map[i] = file[0]
            for i in range(file[2], file[2] + file[1]):
                disk_map[i] = -1
        file = getFile(copy)
    return disk_map

def filesystem_checksum(disk_map : str) -> int:
    r = 0
    for i in range(len(disk_map)):
        if disk_map[i] == -1:
            continue
        r += i * disk_map[i]
    return r

print(filesystem_checksum(compact(decompress(disk_map))))
