# Hanged Man with Kivy

## Description
Basic Hanged man made with Python and to discover the GUI library Kivy:

- Create a simple user interface for desktop and mobile
- Manage user action from the interface and update it following the user actions
- Improve my Python skills

## How to launch

To launch on desktop, simply install the requirements, then execute in a console in the root
```shell
python main.py
```

The unit tests are written with unittest. As such, they can be launched from the root
```shell
python -m unittest 
```

As the project is built with Kivy, it's possible to build an .apk file for android. To do so, the tool Buildozer is used, after having installed the needed dependencies. 

**The command below are Linux specific, as the compiling can not be done on Windows**
```shell
sudo apt update
sudo apt install -y git zip unzip openjdk-13-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

pip3 install --upgrade Cython==0.29.19 virtualenv 

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/

buildozer -v android debug
```


## Useful links

Project started from [this article](https://blog.logrocket.com/build-android-application-kivy-python-framework)

[Kivy documenation](https://kivy.org/doc/stable/)

[About Buildozer](https://buildozer.readthedocs.io/en/latest/)

## What could be added
- Score board
- Call to a dictionary API to get a random word
- Improve design