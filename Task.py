from difflib import SequenceMatcher

# -----------------------------------------------------------------------------------------------------------------------
# 1)Задача: На столі було 10 апельсинів та 3 груші. Хлопчик з'їв 3 апельсини. Скільки всього фруктів залишилось на столі? 
# Відповідь: На столі залишилось 10 фруктів.

# Якщо помилка в умові задачі, ШІ має повідомити про це в розширеному вигляді (з максимумом інформації).
# -----------------------------------------------------------------------------------------------------------------------
# Назви фруктів потрібно вказувати в НАЗИВНОМУ ВІДМІНКУ.

fruits = ["апельсин", "мандарин", "груші", "яблука", "вишні"]
# Дії які можна проводини над речами мають в теорії лиш три вида операцій. Це додавання до кучки фруктів і речей чогось (помістив. покласти, докинути і тд.), віднімання  (з'їсти, забрати), дії які ніяк не змінюють кількість речей на столі(подивився, облизав та інше ).
action = [["з'їсти", "забрати"], ["покласти"], ["облизати", "подивитись"]]


# скористаємся бібліотекою difflib для порівняня двох слів, для знаходження необхідного фрукту чи дії
def word_comparison(word1, word2):
    return SequenceMatcher(None, word1, word2).ratio()


# ділить текст на речення
def line_breaks(str):
    flag_pos = True
    vector_str = []
    for i in range(len(str)):

        if ((ord(str[i]) > 1039 and ord(str[i]) <= 1065) or (ord(str[i]) > 48 and ord(str[i]) <= 57)) and (flag_pos):
            start_pos = i
            flag_pos = False
        elif ord(str[i]) == 46 or ord(str[i]) == 63 or ord(str[i]) == 33:
            end_pos = i + 1
            vector_str.append(str[start_pos:end_pos])
            flag_pos = True

    return vector_str


# processing first sentence
def proce_f_block(str, fruits):
    # ініціюємо вектор довжиною рівною кількості фруктів в масиві фруктів, він міститиме в собі кількість фруктів які були в початкових умовах
    fruits_in_table = [0] * len(fruits)
    str = str.replace(",", " ")
    vect_word = str.split()



    # знаходиму число і за ним шукаємо слово в списку фруктів якщо слово не в списку фруктів то ідем далі

    for i in range(len(vect_word)):
        max_val = 0
        pos_max = 0
        if ord(vect_word[i][0]) > 48 and ord(vect_word[i][0]) <= 57:
            for j in range(len(fruits)):
                value = word_comparison(vect_word[i + 1], fruits[j])
                # print("i , j ",vect_word[i+1],j ,"value",value)
                if max_val < value:
                    max_val = value
                    pos_max = j
                    zna = vect_word[i + 1]

            if (max_val < 0.5):
                print("warning:")
                print('      "', zna, '"',
                      "- Дане слово не є фруктом або не додане до масиву фруктів. В даній версії завдання обчислення ведуться тільки над фруктами.")
                print()
            else:

                fruits_in_table[pos_max] = vect_word[i]

    print(fruits_in_table)
    return fruits_in_table


# processing second sentence
# Хлопчик з'їв 4 мандарини та 2 апельсини
def proce_s_block(str, action,fruits):
    vect_action = []
    vect_action_on_fruits=[]

    str = str.replace(",", " ")
    vect_word = str.split()





    # Знаходимо і записуємо усі слова дії в тимчасовий вектор дій
    for i in range(len(vect_word)):
        max_val = 0
        pos_maxj,pos_maxk = 0,0
        for j in range(len(action)):
            for k in range(len(action[j])):
                value = word_comparison(vect_word[i], action[j][k])
                # print("i , j ",vect_word[i+1],j ,"value",value)
                if max_val < value:
                    max_val = value
                    pos_maxj,pos_maxk = j,k
                    zna = i


        if (max_val > 0.5):
            # print(vect_word[i], "max_value", max_val, "pos_max", pos_maxj)
            # print(pos_maxj)
            vect_action.append([action[pos_maxj][pos_maxk],zna])
    # print(vect_action)

    vector_str = []
    for i in range(len(vect_action)):
        if i+1==len(vect_action):
            vector_str.append(vect_word[vect_action[i][1]:len(vect_word)])
        else:
            vector_str.append(vect_word[vect_action[i][1]:vect_action[i+1][1]])


    # print(vect_word)
    print(vector_str)



    for i in range(len(vector_str)):
        for k in range(len(vector_str[i])):
            max_val = 0
            pos_max = 0
            action_on_fruits = [0] * len(fruits)
            if ord(vector_str[i][k][0]) > 48 and ord(vector_str[i][k][0]) <= 57:
                # print(vector_str[i][k])
                for j in range(len(fruits)):
                    value = word_comparison(vector_str[i][k+1], fruits[j])
                    # print("i , j ",vector_str[i][k+1],j ,"value",value)
                    if max_val < value:
                        max_val = value
                        pos_max = j
                        zna = vector_str[i][k+1]

                if (max_val < 0.5):
                    print("warning:")
                    print('      "', zna, '"',"- Дане слово не є фруктом або не додане до масиву фруктів. В даній версії завдання обчислення ведуться тільки над фруктами."
                          )
                    print()
                else:

                    action_on_fruits[pos_max] = vector_str[i][k]

                    vect_action_on_fruits.append([vect_action[i][0],action_on_fruits])


    print(vect_action_on_fruits)
    return vect_action_on_fruits


# processing all other sentence
def proce_Last_block(str, mas_fru):
    mas = []
    if str[0] != "С":
        print("Запитальті речення можуть починатись тільки із слова Скількі ")
        return 0
    for i in str:
        print(i)

    return


def input():
    str = "3 апельсини 5 яблук,10 мандарин та 4 олівці лежали на столі. Хлопчик з'їв 4 мандарини та 2 апельсини. Скільки всього фруктів з'їв хлопчик? Скільки залишилось мандарин на столі?"
    return str


def start():
    str = input()
    # init vector of conditions and questions
    task = []
    # print(line_breaks(str))
    # print(str)
    vector=proce_f_block("5 апельсини 5 яблук,10 мандарин та 4 олівця лежали на столі.", fruits)
    proce_s_block("Хлопчик поклав на стіл 4 мандарини та з'їв 2 апельсини.", action, fruits)



start()


# proce_Last_block("Скільки всього фруктів з'їв хлопчик?",[])
# print(word_comparison("яблук","яблука"))
