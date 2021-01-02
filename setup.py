import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alexserd_brain_games",
    version="0.2.4",
    author="Aleksandr Serdyuk",
    author_email="a.galko83@gmail.com",
    description="Brain-games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexSerdyuk83/python-project-lvl1.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
