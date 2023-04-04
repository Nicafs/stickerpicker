import setuptools

# from sticker.get_version import git_tag, git_revision, version, linkified_version

with open("requirements.txt") as reqs:
    install_requires = reqs.read().splitlines()

# try:
#     long_desc = open("README.md").read()
# except IOError:
#     long_desc = "Failed to read README.md"

with open("sticker/version.py", "w") as version_file:
    version_file.write(f"""# Generated in setup.py

git_tag = 1
git_revision = 1
version = 1.0.0
linkified_version = teste
""")

setuptools.setup(
    name="maunium-stickerpicker",
    version="1.0.0",
    url="https://github.com/maunium/stickerpicker",

    author="Tulir Asokan",
    author_email="tulir@maunium.net",

    description="A fast and simple Matrix sticker picker widget",
    long_description="Teste",
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),

    install_requires=install_requires,
    python_requires="~=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Framework :: AsyncIO",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": [
        "sticker-import=sticker.stickerimport:cmd",
        "sticker-pack=sticker.pack:cmd",
    ]},
)
