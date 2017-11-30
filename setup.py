from setuptools import setup, find_packages

setup(
    name='xlprocess',
    version='0.1.13',
    description='Process excel file',
    license='MIT License',
    url='https://github.com/NTN9115/xlprocess',
    author='Ning',
    author_email='accelerato314@outlook.com',
    packages=find_packages(),
    platforms='any',
    install_requires=['xlrd>=1.0', 'xlwt>=1.0', 'openpyxl>=2.4'],
)
