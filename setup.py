import platform
import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

install_requires = []

match platform.system():
    case "Darwin":
        install_requires.append("pyobjc")
        install_requires.append("PyCocoa")
    case "Windows":
        install_requires.append("pywin32")
    case "Linux":
        install_requires.append("xcffib")

setuptools.setup(
    name="qframelesswindow",
    version="0.4.3",
    keywords="pyqt6 pyside6 frameless",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A cross-platform frameless window based on qt6, support Win32, X11, Wayland and macOS.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/Flippo24/qframelesswindow/tree/PySide6",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ]
)
