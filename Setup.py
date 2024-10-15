from setuptools import setup, find_packages

setup(
    name='FSeries',  # Replace with your library name
    version='0.1.0',
    author='Louis Liu',
    author_email='LiuLouis1@gmail.com',
    description='A library for computing Fourier Series made for Physics Students!',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=open('README.md').read(),
    url = 'https://github.com/KingL0ui5/FSeries-Python-Library',
)