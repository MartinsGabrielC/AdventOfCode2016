data = 'abbhdwsy'
from hashlib import md5
import sys

def part1(seed, cn):
  seq = 0
  count = 0
  while True:
    if count == cn:
      break
    hsh = md5( (seed + str(seq)).encode('utf-8') ).hexdigest()
    if hsh[0:5] == '00000':
      count += 1
      yield hsh[5]
    seq += 1

def part2(data, cn):
    seq = 0
    count = 0
    passw = [None] * 8
    while True:
        if count == cn:
            break
        hsh = md5( (data + str(seq)).encode('utf-8') ).hexdigest()
        if hsh[0:5] == '00000':
            if hsh[5].isdigit() and 0 <= int(hsh[5]) <=7:
                if(passw[int(hsh[5])] == None):
                    count += 1
                    passw[int(hsh[5])] = hsh[6]
                print(passw)

        seq += 1
    return passw

if __name__ == '__main__':
    try:
        if sys.argv[1] == '1':
            print('|'.join([c for c in part1(data, 8)]))
        else:
            print(part2(data,8))
    except IndexError:
        print("Need to input which part")
