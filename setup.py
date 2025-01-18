from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme_text = readme_file.read()


setup_args = dict(
    name='crypto-cloud-py',
    version='0.1',
    description="",
    keywords=[],
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License',
    packages=find_packages(),
    author="Leo Ertuna",
    author_email="leo.ertuna@gmail.com",
    url="https://github.com/jpleorx/crypto-cloud-py",
    download_url='https://pypi.org/project/crypto-cloud-py/'
)


install_requires = [
    'requests',
    'pydantic',
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
