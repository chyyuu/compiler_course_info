from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='slr-parser',
    version='0.5.0',
    author='Vipul Gharde',
    authon_email='vipul.gharde@gmail.com',
    description='Implementation of Simple LR (SLR) Parser for educational purposes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Vipul97/slr-parser',
    packages=find_packages(),
    install_requires=['graphviz'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'slr=slr_parser.slr_parser:main',
        ],
    },
)
