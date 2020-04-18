from vector import Vector

#INIT VECTOR PART

print('####### INIT VECTOR PART ######\n')
#Test:01 INIT BY LIST [OK]
print('|   TEST: 01 INIT BY LIST   |\nError : none\n')
test = Vector([1.0, 2.0, 3.0])
print(test.values, '\n', test.size)

#Test:02 INIT BY WRONG LIST [OK]
test = 0
try:
    print('|   TEST: 02 INIT BY WRONG LIST   |\nError : ErrorType\n')
    test = Vector(['1.0', '2.0', '3.0'])
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 03 INIT BY SIZE [OK]
test = 0
print('|   TEST: 03 INIT BY SIZE  |\nError : NONE\n')
test = Vector(5)
print(test.values, '\n', test.size)

#Test: 04 INIT BY RANGE [OK]
test = 0
print('|   TEST: 04 INIT BY RANGE   |\nError : NONE\n')
test = Vector((2,5))
print(test.values, '\n', test.size)

#Test:05 INIT BY WRONG RANGE [OK]
test = 0
try:
    print('|   TEST: 05 INIT BY WRONG RANGE   |\nError : ValueError\n')
    test = Vector((2,8,9))
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#Test:06 INIT BY WRONG TYPE [OK]
test = 0
try:
    print('|   TEST: 06 INIT BY WRONG TYPE   |\nError : ErrorType\n')
    test = Vector('1.0')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test:07 INIT EMPTY PARAM [OK]
test = 0
try:
    print('|   TEST: 07 BY EMPTY PARAM   |\nError : AttributeError\n')
    test = Vector('')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

#ADD RADD PART

print('####### ADD RADD PART ######\n')

vector1 = Vector((1,5))
vector2 = Vector((1,5))

#Test: 08 ADD NORMAL BOTH VECTOR [OK]
print('|   TEST: 08 ADD NORMAl BOTH VECTOR |\nError : NONE\n')
result = vector1 + vector2
print(result.values, '\n', result.size)
result = 0

#Test: 09 ADD NORMAL SECOND IS INT [OK]
print('|   TEST: 09 ADD SECOND IS INT |\nError : NONE\n')
result = vector1 + 1
print(result.values, '\n', result.size)
result = 0

#Test: 10 RADD FIRST IS INT [OK]
print('|   TEST: 10 RADD FIRST IS INT |\nError : NONE\n')
result = 1 + vector2
print(result.values, '\n', result.size)
result = 0

#Test: 11 ADD FIRST IS NOT GOOD TYPE [OK]
try:
    print('|   TEST: 11 ADD FIRST IS NOT INT |\nError : TypeError\n')
    result = 'vector1' + vector1
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 12 RADD SECOND IS NOT GOOD TYPE [OK]
try:
    print('|   TEST: 12 RADD SECOND IS NOT INT |\nError : TypeError\n')
    result = vector1 + '1'
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 13 ADD WRONG SIZE [OK]
vector3 = Vector((1,4))
try:
    print('|   TEST: 13 ADD WRONG SIZE |\nError : ValueError\n')
    result = vector1 + vector3
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#Test: 14 RADD WRONG SIZE [OK]

try:
    print('|   TEST: 14 RADD WRONG SIZE |\nError : ValueError\n')
    result = vector3 + vector1
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#SUB RSUB PART

print('####### SUB RSUB PART ######\n')

#Test: 15 SUB NORMAL BOTH VECTOR [OK]
print('|   TEST: 15 SUB NORMAL BOTH VECTOR |\nError : NONE\n')
result = vector1 - vector2
print(result.values, '\n', result.size)
result = 0

#Test: 16 SUB NORMAL SECOND IS INT [OK]
print('|   TEST: 16 SUB NORMAL SECOND IS INT |\nError : NONE\n')
result = vector1 - 1
print(result.values, '\n', result.size)
result = 0

#Test: 17 RSUB FIRST IS INT [OK]
print('|   TEST : 17 RSUB FIRST IS INT |\nError : NONE\n')
result = 1 - vector2
print(result.values, '\n', result.size)
result = 0

#Test: 18 SUB FIRST IS NOT GOOD TYPE [OK]
try:
    print('|   TEST : 18 SUB FIRST IS NOT GOOD TYPE |\nError : TypeError\n')
    result = 'vector1' - vector1
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 19 RSUB SECOND IS NOT GOOD TYPE [OK]
try:
    print('|   TEST: 19 RSUB SECOND IS NOT GOOD TYPE |\nError : TypeError\n')
    result = vector1 - '1'
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 20 SUB WRONG SIZE [OK]
try:
    print('|   TEST: 20 SUB WRONG SIZE |\nError : ValueError\n')
    result = vector1 - vector3
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#Test: 21 RSUB WRONG SIZE [OK]

try:
    print('|   TEST : 21 RSUB WRONG SIZE |\nError : ValueError\n')
    result = vector3 - vector1
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#TRUEDIV RTRUEDIV PART

print('####### TRUE PART ######\n')

#Test: 22 TRUEDIV NORMAL BOTH VECTOR [OK]
print('|   TEST: 22 TRUEDIV NORMAL BOTH VECTOR |\nError : NONE\n')
result = vector1 / vector2
print(result.values, '\n', result.size)
result = 0

#Test: 23 TRUEDIV NORMAL SECOND IS INT [OK]
print('|   TEST: 23 TRUEDIV NORMAL SECOND IS INT |\nError : NONE\n')
result = vector1 / 1
print(result.values, '\n', result.size)
result = 0

#Test: 24 RTRUEDIV FIRST IS INT [OK]
print('|   TEST : 24 RTRUEDIV FIRST IS INT |\nError : NONE\n')
result = 1 / vector2
print(result.values, '\n', result.size)
result = 0

#Test: 25 TRUEDIV FIRST IS NOT GOOD TYPE [OK]
try:
    print('|   TEST : 25 TRUEDIV FIRST IS NOT GOOD TYPE |\nError : TypeError\n')
    result = 'vector1' / vector1
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 26 RTRUEDIV SECOND IS NOT GOOD TYPE [OK]
try:
    print('|   TEST: 26 RTRUEDIV SECOND IS NOT GOOD TYPE |\nError : TypeError\n')
    result = vector1 / '1'
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 27 TRUEDIV WRONG SIZE [OK]
try:
    print('|   TEST: 27 TRUEDIV WRONG SIZE |\nError : ValueError\n')
    result = vector1 / vector3
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#Test: 28 RTRUEDIV WRONG SIZE [OK]

try:
    print('|   TEST : 28 RTRUEDIV WRONG SIZE |\nError : ValueError\n')
    result = vector3 / vector1
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#RMUL MUL PART

print('####### RMUL MUL PART ######\n')

#Test: 29 MUL NORMAL BOTH VECTOR [OK]
print('|   TEST: 29 MUL NORMAL BOTH VECTOR |\nError : NONE\n')
result = vector1 * vector2
print(result, '\n', result)
result = 0

#Test: 30 MUL NORMAL SECOND IS INT [OK]
print('|   TEST: 30 MUL NORMAL SECOND IS INT |\nError : NONE\n')
result = vector1 * 2
print(result.values, '\n', result.size)
result = 0

#Test: 31 RMUL FIRST IS INT [OK]
print('|   TEST : 31 RMUL FIRST IS INT |\nError : NONE\n')
result = 2 * vector2
print(result.values, '\n', result.size)
result = 0

#Test: 32 MUL FIRST IS NOT GOOD TYPE [OK]
try:
    print('|   TEST : 32 MUL FIRST IS NOT GOOD TYPE |\nError : TypeError\n')
    result = 'vector1' * vector1
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 33 RMUL SECOND IS NOT GOOD TYPE [OK]
try:
    print('|   TEST: 33 RMUL SECOND IS NOT GOOD TYPE |\nError : TypeError\n')
    result = vector1 * '1'
    result = 0
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

#Test: 34 MUL WRONG SIZE [OK]
try:
    print('|   TEST: 34 MUL WRONG SIZE |\nError : ValueError\n')
    result = vector1 * vector3
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#Test: 35 RMUL WRONG SIZE [OK]

try:
    print('|   TEST : 35 RMUL WRONG SIZE |\nError : ValueError\n')
    result = vector3 * vector1
    result = 0
    print('CHECK: [KO]\n')
except ValueError:
    print('CHECK: [OK]\n')

#Test: 37 str et repr [OK]

print('STR:', str(vector1))
print('REPR:', repr(vector1))