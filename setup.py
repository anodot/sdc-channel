import datetime
import os

from setuptools import setup, find_packages

app_version = '0.1.0'


def build_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


with open(os.path.join(os.path.dirname(__file__), 'sdc_channel/version.py'), 'w') as f:
    f.write(f'__version__ = "{app_version}"\n')
    f.write(f'__build_time__ = "{build_time()}"\n')

setup(
    name='sdc_channel',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        sdc-channel=sdc_channel.cli:cli_entry_point
    ''',
    zip_safe=False,
    version=app_version,
)
