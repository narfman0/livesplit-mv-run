from setuptools import setup, find_packages


setup(
    name="livesplit-mv-run",
    version="0.1.0",
    description=("Move a particular run from one split file to another"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="livesplit-mv-run",
    author="Jon Robison",
    author_email="narfman0@gmail.com",
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["xml-dataclasses"],
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'livesplit-mv-run = livesplit_mv_run.main:main'
        ],
    },
)
