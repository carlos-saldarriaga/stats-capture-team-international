from app.utils.exceptions import OutOfRangeException

def validate_number(func):
    def wrapper_validate_number( *args, **kwargs):
        for x in args:
            if isinstance(x,int) and (x < 0 or x > 1000):
                raise OutOfRangeException('Number out of boundaries (0-1000)')
        res = func(*args, **kwargs)
        return res
    return wrapper_validate_number