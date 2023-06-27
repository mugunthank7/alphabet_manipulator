# **Alphabet Manipulator**

## **Idea**
Robotic arm that draws alphabets as per the input. (Supports A, T, H, L, E, F)
  
*This package has been created and tested on Ubuntu 22.04 with ROS2 Humble.*

## **How to build**
*Creating a workspace to build the package*
```
mkdir -p ~/AlphabetWritingManipulator_ws/src && cd ~/AlphabetWritingManipulator_ws/src
```
*Cloning the package*
```
git clone https://github.com/mugunthank7/AlphabetWritingManipulator
cd ~/AlphabetWritingManipulator_ws
```
*Installing the dependencies and building the workspace*
```
rosdep install --from-paths src -y --ignore-src
colcon build
```
## **How to use**
```
# source the workspace
source ~/AlphabetWritingManipulator_ws/install/setup.bash

# All set to go! Run the launch file
ros2 launch AlphabetWritingManipulator main.launch.py

# Run the controller script with the path to the image
ros2 run AlphabetWritingManipulator controller.py {path to the image}
```
*The robot should start drawing that alphabet now*

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

