import time

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database')


def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f'Took {t2} seconds')
    return wrapper

@tictoc
def do_this():
    # Simulating running code ..
    time.sleep(1.3)

@tictoc
def do_that():
    # Simulating running code
    time.sleep(.4)

do_this()
do_that()
print('Done')


if __name__ == '__main__':
    """     d1 = Database()
        d2 = Database()
        print(d1 == d2) """
    pass