# Object-Detection-on-Raspberry-Pi-with-obstacle-avoiding-rover

## Steps
### 1. Update the Raspberry Pi
First, the Raspberry Pi needs to be fully updated. Open a terminal and issue:
```
sudo apt-get update
sudo apt-get dist-upgrade
```
### 2. Install TensorFlow
```
pip3 install tensorflow
```
#### TensorFlow also needs the LibAtlas package.
```
sudo apt-get install libatlas-base-dev
```
#### install other dependencies that will be used by the TensorFlow Object Detection API. 
```
sudo pip3 install pillow lxml jupyter matplotlib cython
sudo apt-get install python-tk
```

### 3. Install OpenCV
If any of the following commands don’t work, issue “sudo apt-get update” and then try again. Issue:
```
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install qt4-dev-tools libatlas-base-dev
```
Now that we’ve got all those installed, we can install OpenCV. Issue:
```
sudo pip3 install opencv-python
```

### 4. Compile and Install Protobuf

```sudo apt-get install protobuf-compiler```

Run `protoc --version` once that's done to verify it is installed. You should get a response of `libprotoc 3.6.1` or similar.

### 5. Set up TensorFlow Directory Structure and PYTHONPATH Variable

Now that we’ve installed all the packages, we need to set up the TensorFlow directory. Move back to your home directory, then make a directory called “tensorflow1”, and cd into it.
```
mkdir TensorFlow
cd TensorFlow
```
Download the tensorflow repository from GitHub by issuing:
```
git clone --depth 1 https://github.com/tensorflow/models.git
```
Next, we need to modify the PYTHONPATH environment variable to point at some directories inside the TensorFlow repository we just downloaded. We want PYTHONPATH to be set every time we open a terminal, so we have to modify the .bashrc file. Open it by issuing:
```
sudo nano ~/.bashrc
```
Move to the end of the file, and on the last line, add:
```
export PYTHONPATH=$PYTHONPATH:/home/pi/TensorFlow/models/research:/home/pi/TensorFlow/models/research/slim
```
Now, we need to use Protoc to compile the Protocol Buffer (.proto) files used by the Object Detection API. The .proto files are located in /research/object_detection/protos, but we need to execute the command from the /research directory. Issue:
```
cd /home/pi/TensorFlow/models/research
protoc object_detection/protos/*.proto --python_out=.
```
This command converts all the "name".proto files to "name_pb2".py files. Next, move into the object_detection directory:
```
cd /home/pi/TensorFlow/models/research/object_detection
```
Now, we’ll download the SSD_Lite model from the [TensorFlow detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md). The model zoo is Google’s collection of pre-trained object detection models that have various levels of speed and accuracy. The Raspberry Pi has a weak processor, so we need to use a model that takes less processing power. Though the model will run faster, it comes at a tradeoff of having lower accuracy. For this tutorial, we’ll use SSDLite-MobileNet, which is the fastest model available. 

Google is continuously releasing models with improved speed and performance, so check back at the model zoo often to see if there are any better models.

Download the SSDLite-MobileNet model and unpack it by issuing:
```
wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
```
Now the model is in the object_detection directory and ready to be used.
### 6. Detect Objects!
If you’re using a Picamera, make sure it is enabled in the Raspberry Pi configuration menu.
Download the Object_detection_picamera.py file into the object_detection directory by issuing:
```
wget https://github.com/AbhishekTyagi404/Object-Detection-on-Raspberry-Pi-with-obstacle-avoiding-rover/blob/main/Object_Detection_Pi_Camera
```
Run the script by issuing: 
```
python3 Object_detection_picamera.py 
```
The script defaults to using an attached Picamera. If you have a USB webcam instead, add --usbcam to the end of the command:
```
python3 Object_detection_picamera.py --usbcam
```
Once the script initializes (which can take up to 30 seconds), you will see a window showing a live view from your camera. Common objects inside the view will be identified and have a rectangle drawn around them. 
With the SSDLite model, the Raspberry Pi 3 performs fairly well, achieving a frame rate higher than 1FPS. This is fast enough for most real-time object detection applications.

### Final Project Images
![Final Project Images](https://github.com/AbhishekTyagi404/Object-Detection-on-Raspberry-Pi-with-obstacle-avoiding-rover/blob/main/Images/Final%20Project%20Images.png)
