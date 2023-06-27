# **Alphabet Manipulator**

## **Idea**
Robotic arm that draws alphabets as per the input. (Supports A, T, H, L, E, F)
  
*This package has been created and tested on Ubuntu 22.04 with ROS2 Humble.*

## **How to build**
*Creating a workspace to build the package*
```
mkdir -p ~/alphabet_manipulator_ws/src && cd ~/alphabet_manipulator_ws/src
```
*Cloning the package*
```
git clone https://github.com/mugunthank7/alphabet_manipulator
cd ~/alphabet_manipulator_ws
```
*Installing the dependencies and building the workspace*
```
rosdep install --from-paths src -y --ignore-src
colcon build
```
## **How to use**
```
# source the workspace
source ~/alphabet_manipulator_ws/install/setup.bash

# All set to go! Run the launch file
ros2 launch alphabet_manipulator main.launch.py

# Run the controller script with the path to the image
ros2 run alphabet_manipulator controller.py {path to the image}
```
*The robot should start drawing that alphabet now*


## **SAMPLE INPUTS**

a.JPEG
![a](https://github.com/mugunthank7/alphabet_manipulator/assets/74373098/fe540047-21c9-4002-85fc-55c5a01f8617)

E.JPG
![image](https://github.com/mugunthank7/alphabet_manipulator/assets/74373098/8e2888df-eedb-40d4-85a8-c56fdd78ba12)


F.JPG
![image](https://github.com/mugunthank7/alphabet_manipulator/assets/74373098/f903f97f-92b0-49f6-9500-808b9b16e67c)




## **SAMPLE OUTPUTS**
**wRITING ALPHABET "A"**

[a.webm](https://github.com/mugunthank7/alphabet_manipulator/assets/74373098/eaac9eb3-636b-488c-b41d-87cf6c7f3c8c)


**WRITING ALPHABET "E"**

[e.webm](https://github.com/mugunthank7/alphabet_manipulator/assets/74373098/d2f1141b-7ed9-4e74-914d-eaeb2eba97a4)


**wRITING ALPHABET "F"**
[f.webm](https://github.com/mugunthank7/alphabet_manipulator/assets/74373098/8d5cc517-c8f5-467f-be8a-72f979c74e33)


## **Pre-Requiste Python Libraries**

*1) TensorFlow*
TensorFlow is a Python library for fast numerical computing created and released by Google.
```
# Requires the latest pip
pip install --upgrade pip

# Current stable release for CPU and GPU
pip install tensorflow

# Or try the preview build (unstable)
pip install tf-nightly
```

*2) Keras*
Keras is a neural network Application Programming Interface (API) for Python 
that is tightly integrated with TensorFlow, which is used to build machine learning models.
```
pip install keras
```



