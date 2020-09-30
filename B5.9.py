import time
class Timer:
#     import time
    # Определяем класс
    # Пишем конструктор класса
    def __init__(self, num_runs = 1):
        self.num_runs = num_runs
        # Конструктор принимает аргумент num_runs - количество запусков функции при замере
    def __enter__(self):
        self.t_start = time.time()
        return self
    def __exit__(self,*args, **kwargs):
        t_end = time.time()
        total = (t_end - self.t_start)
        print('[*] время выполнения функции в контекстном менеджере: {} секунд.'.format(total))
        return self
        # Конструктор
    def __call__(self, func):
        # декоратор
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(self.num_runs):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения с помощью объекта класса: {} секунд.'.format(total/self.num_runs))
            return return_value
        return wrapper 
       
# Создаём объект класса
timer_10 = Timer(num_runs = 10)
# Используем объект, как декоратор
@timer_10
def f():
    for i in range(10000):
        pass
# Вызываем функцию
f()

# Вызываем контекстный менеджер
with Timer() as t:
    # Тут какой-то код, у которого мы хотим замерить время работы
    a = list(range(100000, 1, -1))
    a.sort()

