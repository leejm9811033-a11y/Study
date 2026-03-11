# 기본 자료형 : int, float, bool, complex

# 묶음 자료셩 : str, list, tuple, set, dict

# 1) str : 문자열, 묶음 자료형. 순서O, 수정X

s= 'sequence'
print(s)
print(s, id(s) )
print('길이 : ', len(s) )
print(s[0], s[2] )
print('길이 : ', s.find(s), s.find('e', 3), s.rfind('e') )

# 인덱싱 / 슬라이싱

print(s[5]) #변수명[순서], index는 0부터 출발
print(s[:], ' ', s[0:len(s)], s[::2])  # s[ start: end : slicing ]


print(s)


# 2) List : 다양한 종류의 자료 묶음형. 순서o, 수정o, 중복o

a = [1, 2, 3]
print(a, a[0], a[0:2])

b = [10, a, 10, 20.5, True, '문자열']

print(b, b[1], b[1][0])

family = ['엄마', '아빠', '나', '여동생']
print(id(family))
family.append('남동생')
print(family)
family.extend(['형', '삼초', '조카'])
print(family)
family.remove('나')
print(family)
family.insert(1, '할머니')
print(family)
family += ['이모']
print(family)
print(family.index('아빠'))
print('엄마' in family, '나' in family)
family.remove('아빠')
del family[2] # 순서에 의한 삭제
print(family)



print()
kbs = ['123', '34', '234']
kbs.sort()
print(kbs)

mbc = [123, 34, 234]
mbc.sort(reverse = True)
print(mbc)


name = ['tom', 'james', 'oscar']
name2 = name

import copy
name3 = copy.deepcopy(name)
print(name3, id(name3))

name[0] = '길동'
print(name)
print(name2)
print(name3)


# 3) tuple : 리스트와 유사. 읽기 전형

t = (1,2,3,4)
t = 1,2,3,4

print(t, type(t))
k = (1, )
print(k, type(k))
print(t[0], ' ', t[0:2])

imsi = list(t)
imsi[0] = 77
t = tuple(imsi)
print(t)

# 4) set : 순서 없음, 수정 가능, 중복 불가

ss = {1, 2, 1, 3}
print(ss)
ss2 = {3,4}

print(ss.union(ss2))
print(ss.intersection(ss2))
print(ss - ss2, ss | ss2, ss & ss2)
# print(ss[0])     에러 발생

ss.update({6,7})
print(ss)
ss.discard(7)
# ss.remove(6)  6이 없으면, 에러 발생할 수 도 있음 

li = ['aa', 'aa','bb' ,'cc','aa','aa']
imsi = set(li)
li= list(imsi)
print(li)


#5 dict : 사전 자료형 {'키': 값} 형태

# 방법1

mydic = dict(k1 = 1, k2 = 'ok', k3 = 123.4)
print(mydic, type(mydic))

# 방법2
dic = {'파충류': '보아뱀', '커피': '아메리카노', '인사': 'hi'}

print(dic)
print(len(dic))
print(dic['커피'])  # 인덱싱 불가, 키로 값을 찾는다.
print(dic['인사'])    # 인덱싱이 없음

ff = dic.get('자바')
print(ff)

dic['금요일'] = '와우'    # 추가
print(dic)

del dic['인사']
print(dic)

print(dic.keys())
print(dic.values())


