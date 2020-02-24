from difflib import SequenceMatcher


# -----------------------------------------------------------------------------------------------------------------------
# 1)Задача: На столі було 10 апельсинів та 3 груші. Хлопчик з'їв 3 апельсини. Скільки всього фруктів залишилось на столі? 
# Відповідь: На столі залишилось 10 фруктів.

# Якщо помилка в умові задачі, ШІ має повідомити про це в розширеному вигляді (з максимумом інформації).
# -----------------------------------------------------------------------------------------------------------------------


# скористаємся бібліотекою difflib для порівняня двох слів, для знаходження необхідного фрукту чи дії
def word_comparison(word1, word2):
    return SequenceMatcher(None, word1, word2).ratio()


# ділить текст на речення
def line_breaks(string):
    flag_pos = True
    vector_str = []
    for i in range(len(string)):

        if ((ord(string[i]) > 1039 and ord(string[i]) <= 1065) or (ord(string[i]) > 48 and ord(string[i]) <= 57)) and (flag_pos):
            start_pos = i
            flag_pos = False
        elif ord(string[i]) == 46 or ord(string[i]) == 63 or ord(string[i]) == 33:
            end_pos = i + 1
            vector_str.append(string[start_pos:end_pos])
            flag_pos = True

    return vector_str

def vector_add(vec1,vec2):
    vec=[]
    for i in range(len(vec1)):
            vec.append(vec1[i]+vec2[i])

    return vec
def vec_zna(vecor,zna):
    new_vect=[]
    if zna==0:
        zna=-1
    elif zna==1:
        zna=1
    elif zna==2:
        zna=0
    for i in vecor:
        new_vect.append(int(i)*zna)
    return new_vect

def list_multiplication(vect_1,vect_2):
    vec=[]
    for i in range(len(vect_1)):
        vec.append(vect_1[i]*vect_2[i])
    return vec


# processing first sentence
def proce_f_block(string, fruits):
    # ініціюємо вектор довжиною рівною кількості фруктів в масиві фруктів, він міститиме в собі кількість фруктів які були в початкових умовах
    fruits_in_table = [0] * len(fruits)
    string = string.replace(",", " ")
    vect_word = string.split()

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

                fruits_in_table[pos_max] = int(vect_word[i])

    # print(fruits_in_table)
    return fruits_in_table



# processing second sentence
def proce_s_block(string, action, fruits):
    vect_action = []
    vect_action_on_fruits = []

    string = string.replace(",", " ")
    vect_word = string.split()

    # Знаходимо і записуємо усі слова дії в тимчасовий вектор дій
    for i in range(len(vect_word)):
        max_val = 0
        pos_maxj, pos_maxk = 0, 0
        for j in range(len(action)):
            for k in range(len(action[j])):
                value = word_comparison(vect_word[i], action[j][k])
                # print("i , j ",vect_word[i+1],j ,"value",value)
                if max_val < value:
                    max_val = value
                    pos_maxj, pos_maxk = j, k
                    zna = i
                    znak_action=j

        if (max_val > 0.5):
            # print(vect_word[i], "max_value", max_val, "pos_max", pos_maxj)
            # print(pos_maxj)

            vect_action.append([action[pos_maxj][pos_maxk], zna,znak_action])


    vector_str = []
    for i in range(len(vect_action)):
        if i + 1 == len(vect_action):
            vector_str.append(vect_word[vect_action[i][1]:len(vect_word)])
        else:
            vector_str.append(vect_word[vect_action[i][1]:vect_action[i + 1][1]])

    # print(vect_word)
    # print(vector_str)

    # Додаємо до вектора дій фрукти над якими виконана дія
    for i in range(len(vector_str)):
        for k in range(len(vector_str[i])):
            max_val = 0
            pos_max = 0
            action_on_fruits = [0] * len(fruits)
            if ord(vector_str[i][k][0]) > 48 and ord(vector_str[i][k][0]) <= 57:
                # print(vector_str[i][k])
                for j in range(len(fruits)):
                    value = word_comparison(vector_str[i][k + 1], fruits[j])
                    # print("i , j ",vector_str[i][k+1],j ,"value",value)
                    if max_val < value:
                        max_val = value
                        pos_max = j
                        zna = vector_str[i][k + 1]

                if (max_val < 0.5):
                    print("warning:")
                    print('      "', zna, '"',
                          "- Дане слово не є фруктом або не додане до масиву фруктів. В даній версії завдання обчислення ведуться тільки над фруктами."
                          )
                    print()
                else:

                    action_on_fruits[pos_max] = int(vector_str[i][k])
                    vect_action_on_fruits.append([vect_action[i][0], action_on_fruits,vect_action[i][2]])


    return vect_action_on_fruits


# processing all other sentence
def proce_Last_block(string, mas_fru, vector_action, fruits, action):
    # додатковий вектор слів які необхідні для складання відповіді, а також для осмислення деяких питаннь
    vect_extra_word = ["залишилось", "фрукти", "хлопчик"]
    vec_a = []
    vec_obj = []


    string = string.replace(",", " ")
    vect_word = string.split()

    if string[0] != "С":
        print("Запитальті речення можуть починатись тільки із слова Скількі ")
        return 0

    else:
        for i in range(len(vect_word)):
            # Дії які виконав хлопчик над множиною фруктів
            if word_comparison(vect_word[i], vect_extra_word[0]) > 0.5:
                vec_a.append(vect_extra_word[0])

            for j in range(len(action)):
                for k in range(len(action[j])):
                    if word_comparison(action[j][k], vect_word[i]) > 0.5:
                        vec_a.append(vect_word[i])

            # Тепер знаходимо об'єкти над якими треба виконати дії
            if word_comparison(vect_word[i], vect_extra_word[1]) > 0.5:
                vec_obj.append("фрукти")
            else:
                for k in range(len(fruits)):
                    if word_comparison(vect_word[i],fruits[k])>0.5:
                        vec_obj.append(vect_word[i])


    str_answer = ''


    if len(vec_a) == 0:
        print("error:")
        print("      В питанні для задачі немає дієслова або воно не додано до списку ймовірних дієслів, питання неможливо скласти без дієслова")
        return 1
    if len(vec_a) > 1:
        print("error:")
        print("      В питанні для задачі може бути тільки дієслово, додайте ще одне питання з необхідним вам дієсловом",' "',vec_a[1],'"')
        return 1
    else:
        str1 = ''
        vec_wanted_f = [0] * len(fruits)
        if vec_a[0]==vect_extra_word[0]:

            for j in vector_action:
                mas_fru = vector_add(mas_fru, vec_zna(j[1], int(j[2])))


            for i in range(len(vec_obj)):
                if word_comparison(vec_obj[i], vect_extra_word[1]) > 0.5:
                    val=0
                    for s in mas_fru:
                        val=val+s

                    str1 = str1 +str(val) +" всіх фруктів "
                else:

                    for j in range(len(fruits)):
                       if word_comparison(vec_obj[i],fruits[j])>0.5:

                           vec_wanted_f[j]=1


            mas_fru=list_multiplication(mas_fru, vec_wanted_f)

            for k in range(len(fruits)):
                if mas_fru[k]!=0:

                    str1=str1+","+str(mas_fru[k])+" "+fruits[k]+' '

            print("Залишилось",str1,".")

        else:
            vect_ansver=[0]*len(fruits)

            for j in range(len(vector_action)):
                if word_comparison(vec_a[0],vector_action[j][0])>0.5:
                    vect_ansver=vector_add(vect_ansver,vector_action[j][1],)



            for i in range(len(vec_obj)):
                if word_comparison(vec_obj[i], vect_extra_word[1]) > 0.5:
                    val = 0
                    for s in vect_ansver:
                        val = val + s

                    str1 = str1 + str(val) + " всіх фруктів "

                else:
                    for j in range(len(fruits)):
                       if word_comparison(vec_obj[i],fruits[j])>0.5:

                           vec_wanted_f[j]=1


            vect_ansver=list_multiplication(vect_ansver,vec_wanted_f)
            for k in range(len(fruits)):
                if vect_ansver[k] != 0:
                    str1 = str1 + "," + str(vect_ansver[k]) + " " + fruits[k] + ' '

            print("Хлопчик", vec_a[0],str1, ".")
    # Перевірка на кількість дієслів в рядку, оскільки по завданню для одного питання 1 дієслово і безліч іменників





def input_task():
    print("Введіть текст завдання :")
    str=input()


    return str


def start():
    # Назви фруктів потрібно вказувати в НАЗИВНОМУ ВІДМІНКУ.

    fruits = ["апельсин", "мандарин", "груші", "яблука", "вишні","диня","кавун"]
    # Дії які можна проводини над речами мають в теорії лиш три вида операцій. Це додавання до кучі фруктів і речей чогось (помістив. покласти, докинути і тд.), віднімання  (з'їсти, забрати), дії які ніяк не змінюють кількість речей на столі(подивився, облизав та інше ).
    action = [["з'їсти", "забрати"], ["покласти","додати"], ["облизати", "подивитись"]]

    str = input_task()
    # init vector of conditions and questions
    task = []
    print("Умова:")
    print(str)
    task=line_breaks(str)

    vector = proce_f_block(task[0], fruits)
    vector_action = proce_s_block(task[1], action, fruits)
    # print(vector_action)
    for i in range(2,len(task),+1):
        print("Питання під номером:",i-1)
        print(task[i])

        print("Відповідь:")
        resalt=proce_Last_block(task[i], vector, vector_action, fruits,action)
        if resalt==1:
            print("Виправте питання під номером ",i-1)
        print()

start()

