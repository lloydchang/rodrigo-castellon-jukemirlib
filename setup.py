from setuptools import setup, find_packages

setup(
    name="jukemirlib",
    packages=["jukemirlib"],
    install_requires=[
        "jukebox @ git+https://github.com/lloydchang/rodrigo-castellon-jukebox@lloydchang-patch-1",
        "wget",
        "accelerate",
    ],
)
