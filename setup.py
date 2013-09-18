import os
import re

try:
    from setuptools import setup
    setup_params = {'scripts': ['tmux-chooser'],
                    'install_requires': ['paramiko'],
                   }
except ImportError:
    from distutils.core import setup
    setup_params = {'scripts': ['tmux-chooser']}


here = os.path.dirname(os.path.abspath(__file__))


def get_version():
    f = open(os.path.join(here, 'tmux-chooser'))
    version_file = f.read()
    f.close()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='tmux-chooser',
    version=get_version(),
    description="tmux session chooser for busy people",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    zip_safe=False,
    keywords='setuptools deployment installation distutils',
    author='Peter Debacker',
    author_email='peter@peterdebacker.com',
    url='https://github.com/peter-d/tmux-chooser',
    download_url='https://github.com/peter-d/tmux-chooser/tarball/%s.tar.gz' % get_version(),
    license='MIT',
    long_description=open(os.path.join(here, "README.md")).read(),
    **setup_params
)
