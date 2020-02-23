#
# 1)Задача: На столі було 10 апельсинів та 3 груші. Хлопчик з'їв 3 апельсини. Скільки всього фруктів залишилось на столі? 
# Відповідь: На столі залишилось 10 фруктів.

# Якщо помилка в умові задачі, ШІ має повідомити про це в розширеному вигляді (з максимумом інформації).

# Назви фруктів потрібно вказувати в НАЗИВНОМУ ВІДМІНКУ.
# fruits = {"апельсин": ["апельсини", "апельсинів", "апельсинами"]}
fruits = ["апельсин", "мандарин", "груші", "яблука", "вишні"]
# Дії які можна проводини над речами мають в теорії лиш три вида операцій. Це додавання до кучки фруктів і речей чогось (помістив. покласти, докинути і тд.), віднімання  (з'їсти, забрати), дії які ніяк не змінюють кількість речей на столі(подивився, облизав та інше ).
action =[["з'їв","звбрав","поклав",""],[],[]]



def input():
    str = "На столі було 10 апельсинів та 3 груші. Хлопчик з'їв 3 апельсини. Скільки всього фруктів залишилось на столі?"
    return str


# end-17:23
def line_breaks(str):
    flag_pos = True
    vector_str = []
    for i in range(len(str)):
        print('str[i]', str[i], 'ord[i]', ord(str[i]))
        if ((ord(str[i]) > 1039 and ord(str[i]) <= 1065) or (ord(str[i]) > 48 and ord(str[i]) <= 57)) and (flag_pos):
            start_pos = i
            flag_pos = False
        elif ord(str[i]) == 46 or ord(str[i]) == 63 or ord(str[i]) == 33:
            end_pos = i + 1
            vector_str.append(str[start_pos:end_pos])
            flag_pos = True

    return vector_str


def proce_f_block():
    print()


def proce_s_block():
    print()


def proce_Last_block():
    print()


def start():
    str = input()
    # init vector of conditions and questions
    task = []
    print(line_breaks(str))
    # print(str)


start()
