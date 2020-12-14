with open ('numbers.txt') as file:                              #открытие файла с числами
    for line in file:                                           #запускаем цикл чтения из файла
        a = line.split(' ')                                     #создаем переменную с разбиением по пробелу строки
        fizz = int(a[0])                                        #берем первый элемент из разбитой строки
        limit = int(a[2])                                       #берем до скольки считать
        for i in range(1, limit + 1):                           #запускаем цикл по ковырянию физбаз
            new_save_from_fb = open('results.txt', 'a')         #создаем новый файл для сохранения с разрешением 'a' - append (добавление)
            if i % fizz == 0 and i % buzz == 0:
                new_save_from_fb.writelines('FB ')              #writelines записывает в файл вместо принта в консоль
                print('FB', end = ' ')
            elif i % fizz == 0:
                print('F', end = ' ')
                new_save_from_fb.writelines('F ')               #тут тоже что и выше
            elif i % buzz == 0:
                print('B', end = ' ')
                new_save_from_fb.writelines('B ')               #тут тоже
            else:
                p = print (i, end = ' ')
                new_save_from_fb.writelines(str(i)+str(' '))    #тут мы завершаем все что крутится в цикле физбаз
        print('\n Числа в строке из файла - ' + line)
        new_save_from_fb.writelines('\n Числа в строке из файла - ' + line + '\n')           # тут последнее повторение из консоли + перевод на новую строку следующей строки физбаз из цикла
        new_save_from_fb.close()                                #закрытие файлва который мы создавали

        #комментарии мы должны писать транслитом ili na angliyskom esli chto