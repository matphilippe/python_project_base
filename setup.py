from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

setup(
    name="dummy",
    version="0.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=requires,
)
