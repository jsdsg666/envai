from setuptools import setup, find_packages


setup(
    name='envai',
    version='0.1.3',
    license='GNU GPLv3',
    author="Yuqi Wang",
    author_email='22S054041@stu.hit.edu.cn',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jsdsg666/envai',
    keywords='envai',
    install_requires=[
        'pandas',
        'openpyxl'
      ],

)
