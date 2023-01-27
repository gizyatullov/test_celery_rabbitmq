from celery import Celery

broker_url = 'pyamqp://user:1234@rabbit:5672//'

app = Celery(
    'fib',
    broker=broker_url
)


def calc_fib(num):
    n1 = 0
    n2 = 1
    if num < 0:
        print('Incorrect input')
        return 0
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        for i in range(2, num):
            n1, n2 = n2, n1 + n2
        return n2


@app.task(bind=True,
          default_retry_delay=10,
          ignore_result=True)
def fib_task(self, num):
    try:
        num = int(num)
    except (ValueError, TypeError):
        print('Not int!')

    result = calc_fib(num)
    print(f'RESULT FROM {num}={result}')

# celery -A celery_app worker --loglevel=INFO
