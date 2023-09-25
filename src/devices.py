import functools
import time


def get_device_configurations(*device_ids):
    device_ids = device_ids if type(device_ids) is list else [device_ids]
    configurations = [get_device_configuration(device_id) for device_id in device_ids]
    return configurations


@functools.lru_cache(maxsize=100)
def get_device_configuration(device_id):
    #TODO actual call to DB to get data here
    time.sleep(0.1)
    return {'id': device_id, 'name': f'device_{device_id}'}
