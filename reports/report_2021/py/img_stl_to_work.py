from glob import glob
from random import choice

actions = '''
Была создана
Разработана
Подготовлена
При помощи среды моделирования Blender подготовлена
Была разработана'''.split('\n')


models = '''Модель крышки для камеры
Модель держателя камеры
Модель платы корпуса драйверов
Модель крышки корпуса драйверов
Модель концевого упора x
Модель концевого упора y
Модель концевого упора z
Модель держателя лазерного датчика
Модель заднего левого правого разъема основного корпуса
Модель задней части основного корпуса
Модель левыого и правого разъемов крышки основного корпуса 
Модель крышки основного корпуса
Модель левой части основного корпуса 
Модель основного корпуса, подставки для Raspberry Pi 
Модель правой части основного корпуса 
Модель верхней части главного корпуса
Модель верхней части корпуса
Модель верхнего левого правого угла основного корпуса
Модель держателя блока питания
Модель дистанцонной шайбы'''.lower().split('\n')

i = 0
for x in sorted(glob('/tmp/dsfdsf/*stl')):
    file = x.split('/')[-1]
    png_file = file + '.png'
    model = models[i]
    print('\n', choice(actions), model, "показанная на рисунке.", '\n\n', f'![{model}](img/{png_file} "{model}")')
    i += 1
#    print("Model of", x.split('/')[-1].split('.')[0].replace('-',' '))
    