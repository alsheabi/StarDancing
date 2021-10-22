# Dependencies:

- !pip install mediapipe opencv-python
- Simulation of dynamics:
 Numpy
, Math
, SciPy
- GUI:
 Matplotlib
 ,Matplotlib Mapping Toolkits
- Threading:
 Time
, Datetime
, Threading


# How to run:
Here we implement Demo of our project,starting with estamate motion in realtime, then send data to drones to resample same motion in sky, because we do not have drones, we use simulators, steps below:
- Starting with detect motions in real time to get coordinates point by using `StarDancing.py` . [Watch detection and Tracking body motions  ](https://vimeo.com/637641650).
- get the results of coordinates  `sample of Coordinates output.txt` file contains the data where we use in simlator.
- use the output file as input in simulators to locate the postions of drones.
- clone this repo to use simulator `https://github.com/abhijitmajumdar/Quadcopter_simulator`


# Sample of keypoints output:
Each Landmark consists of the Following:
`id` belong to the location on body such as `0` -> Nose , `8` -> Left ear, and `11` -> right Shoulder.
`x` and `y:` Landmark coordinates normalized to `[0.0, 1.0]` by the image width and height respectively.
`z:` Represents the landmark depth with the depth at the midpoint of hips being the origin, and the smaller the value the closer the landmark is to the camera. The magnitude of z uses roughly the same scale as x.
`visibility:` A value in `[0.0, 1.0]` indicating the likelihood of the landmark being visible (present and not occluded) in the image.

0 x: 0.5402820110321045
y: 0.48479801416397095
z: -1.1574974060058594
visibility: 0.9991260766983032
# More Details:

Imagine that you are having a night trip in the park and when you look up you find that the stars are dancing in imitation of the movements of a masterful dancer. Then you⋅⋅ think that it is a moving painting in the sky.
Star Dancing is elevating the discussion on the relationship between humans and AI to another level. One of the main goals is to interact with AI, to feel the presence of neural networks – in a playful way.

# StarDancing video:    [Watch StarDancing Video ](https://vimeo.com/637615941) 




![alt text](https://github.com/alsheabi/StarDancing/blob/main/Pictures/211019_stardancing.jpg)
 
 
 # References: 
 - https://google.github.io/mediapipe/solutions/pose.html#pose_landmarks
 - https://github.com/abhijitmajumdar/Quadcopter_simulator
