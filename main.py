print('***************Задача №1***************')

from random import randint as rand

nums = [''] * 20
nums = list(map(lambda x: rand(1, 9), nums))
nums_square = list(map(lambda x: x ** 2, nums))
print('Массив случайных чисел:', end='\t')
for i in nums:
    print(i, end='\t')
print()
print('Массив их квадратов:', end='\t')
for i in nums_square:
    print(i, end='\t')



print('\n\n***************Задача №2***************')
nums = [''] * 100
nums = list(map(lambda x: rand(10, 100), nums))

# вывод массива по 20 элементов в строке
def print20(arr):
    for i in range(1, len(arr) + 1):
        print(arr[i - 1], end='\t')
        if i % 20 == 0 or i == len(arr):
            print()
    print()

# функция для фильтрации кратных 5
def f5(i):
    return i % 5 != 0

# функция для удаления повторов
def rep_del(arr):
    i = 0
    while i < len(arr):
        if arr.index(arr[i]) != i:
            arr.pop(i)
        else:
            i += 1
    return arr

# функция для фильтрации чисел с одинаковыми цифрами
def numb(i):
    s = str(i)
    if s[-1] != s[-2]:
        return True



print('Массив 100 случайных чисел:')
print20(nums)

nums = list(filter(f5, nums))
print('Массив случайных чисел без кратных 5:')
print20(nums)

nums = rep_del(nums)
print('Массив случайных чисел без кратных 5 и повторов:')
print20(nums)

nums = list(filter(numb, nums))
print('Массив случайных чисел без кратных 5, повторов и чисел с одинаковыми цифрами:')
print20(nums)

# вывод получившегося массива в 3 столбика
print('Получившийся массив в 3 столбика:')
for i in range(1, len(nums) + 1):
    print(nums[i - 1], end='\t')
    if i % 3 == 0 or i == len(nums):
        print()

print('\n\n***************Задача №3***************')

from random import randint as rand

marks = ['audi', 'bmw', 'lada', 'tesla', 'toyota']
numbers = ['qqq111', 'www222', 'eee333', 'rrr444', 'ttt555']
people = ['Ivan', 'John', 'Antonio', 'Hideo', 'Hans']
owners = []

# генерация случайного списка владельцев
for i in range(len(numbers)):
    num_owners = rand(1, 5)
    own = []
    while len(own) < num_owners:
        rand_owner_num = rand(0, 4)
        rand_owner = people[rand_owner_num]
        if rand_owner not in own:
            own.append(rand_owner)
    owners.append(own)


registry = list(zip(marks, numbers, owners))


# вывод ассортимента машин со списком владельцев
def print_cars():
    print('Вот что есть в наличии:')
    for i in registry:
        print('\tМарка:', i[0], '\n\t', 'Регистрационный номер:', i[1], '\n\t', 'Список владельцев:', ', '.join(i[2]))


# вывод одного авто
def print_car():
    print('Информация о выбранном авто:')


# найти авто по номеру
def find_by_number(num):
    pass

# def buy_car():
#     ('Введите регистрационный номер авто, который хотите купить:')

print('Добро пожаловать в наш автосалон')
while True:
    try:
        ans = int(input('Что вас интересует?\n'
                  '\t1 - посмотреть ассортимент авто\n'
                  '\t2 - купить\n'
                  '\t3 - продать\n'
                  '\t4 - найти по номеру\n'
                  '\t0 - покинуть салон\n'))
        match ans:
            case 0:
                break
            case 1:
                print_cars()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                print('Повторите, я вас не понял')
    except:
        print('Повторите, я вас не понял')



