from pathlib import Path
from setuptools import setup, find_packages


def load_requirements(fname: Path):
    reqs = []
    with fname.open('r') as reqs_file:
        for line in reqs_file:
            reqs.append(line.rstrip())
    return reqs


setup(
    name='test_loader',
    version='1.0.1',
    packages=find_packages(),
    url='',
    license='',
    author='ejgardner',
    author_email='',
    description='',
    install_requires=load_requirements(Path("requirements.txt")),
    python_requires='>=3'
)
