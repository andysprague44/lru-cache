
import functools
import time
from collections import OrderedDict


class LRUCache:
    def __init__(self, user_function, maxsize=100):
        self.user_function = user_function
        self.maxsize = maxsize
        self.items = OrderedDict()

    def __call__(self, *key):
        items = self.items
        try:
            value = items[key]
            items.move_to_end(key) #make most recent
        except KeyError:
            value = self.user_function(*key)
            if len(items) >= self.maxsize:
                items.popitem(False) #pop oldest
            items[key] = value
        return value


def get_device_configurations(*device_ids, cache: LRUCache = None):
    device_ids = device_ids if type(device_ids) is list else [device_ids]
    configurations = [get_device_configuration(device_id, cache) for device_id in device_ids]
    return configurations


def get_device_configuration(device_id, cache: LRUCache = None):
    cache = cache or LRUCache(__get_device_configuration)
    return cache(device_id)
   

def __get_device_configuration(device_id):
    time.sleep(0.1)  # TODO actual call to DB to get data here
    return {'id': device_id, 'name': f'device_{device_id}'}
