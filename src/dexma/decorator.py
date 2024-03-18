def dexma_parser(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code != 200:
            raise Exception(response.reason)
        else:
            return response.json()
    return wrapper

