from setuptools import find_packages, setup

VERSION = __import__('pomodoro').__version__
NAME = 'pomodoro'
URL = 'https://github.com/raiderrobert/pomodoro/'

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

install_requires = ['click', 'progressbar2']

setup(
    name=NAME,
    version=VERSION,
    author='Robert Roskam',
    author_email='me@robertroskam.com',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,  # declarations in MANIFEST.in
    license='MIT',
    url=URL,
    download_url=URL+'/tarball/'+VERSION,
    description="A super simple pomodoro implementation",
    long_description=read_file('README.md'),
    keywords=['pomodoro', 'time management', 'productivity'],
    entry_points={
        'console_scripts': [
            'pomodoro = pomodoro:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Office/Business',
    ],
    zip_safe=False
)
