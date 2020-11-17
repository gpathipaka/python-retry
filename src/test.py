from retry import retry

@retry()
def make_trouble():
    '''Retry until succeed'''
    try:
        print('Hello .... inside try')
        1/0
    except Exception as e:
        print(f'Inside except {str(e)}')
        raise e

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    make_trouble()