Setting Up EC2
---

### Starting the Instance

I'm going to use a g2.2xlarge instance which has:

* CPU: Intel Xeon E5-2670 and 15Gb of memory.

* GPU: NVIDIA GPU (1,536 CUDA cores) and 4GB of video memory.

* OS: 64-bit Ubuntu 14.04 Linux.


To do this one can navigate through the [web site](http://aws.amazon.com/). Alternatively, one could use the AWS CLI which allows you to launch instance programmatically. The CLI the appropriate command would be:

```
aws ec2 run-instances --image-id ami-c3b8d6aa --count 1 --instance-type t1.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e
```

I ran my tests as spot instances since the spot price was significantly lower than the on demand price (0.0061/hour ve 0.68/hour) (I bid 0.05/hour). 

After SSH-ing in confirm that the OS can "see" the GPU.

```sh
lscpu
sudo lshw -C display
```


### Installing dependencies

First we need to make sure that our instance OS is up to date with

```sh
sudo apt-get update
sudo apt-get -y upgrade
```

Also some other importnant stuff (most of this should have been included with the os)

```sh
sudo apt-get install -y gcc g++ gfortran build-essential git wget python-dev python-pip
```

**LAPAC**


```sh
sudo apt-get install -y libblas3gf
sudo apt-get install -y libblas-doc
sudo apt-get install -y libblas-dev
sudo apt-get install -y liblapack3gf
sudo apt-get install -y liblapack-doc
sudo apt-get install -y liblapack-dev
```

**BLAS via ATLAS**

```
apt-get source atlas
apt-get build-dep atlas
apt-get install devscripts
```

**Boost**

```
sudo apt-get -y libboost-all-dev
```

**OpenCV**

```
sudo apt-get -y install libopencv-dev build-essential cmake git libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils
```
and actually install it...

```
mkdir opencv
cd opencv
wget https://github.com/Itseez/opencv/archive/3.0.0-alpha.zip -O opencv-3.0.0-alpha.zip
unzip opencv-3.0.0-alpha.zip
cd opencv-3.0.0-alpha
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
make -j $(nproc)
sudo make install
```

Add it to ldconfig cache

```
sudo /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```
Now restart with ```sudo reboot```.


**CUDA**

This will be the most challingin dependency to get working correctly. First install some extra drivers with.

```
sudo apt-get install linux-image-extra-virtual
```

I chose “choose package maintainers version” when prompted. Now disble nouveau as if conflics with the nvidia kernel.

```
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
```

add this lines

```
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```
save and

```
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
```

reboot

```
sudo update-initramfs -u
sudo reboot
```

and isntall some headders

```
sudo apt-get install linux-source
sudo apt-get install linux-headers-3.13.0-37-generic
```

So now we ca bein to isntll CUDA.

```
wget http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_linux_64.run
chmod +x cuda_6.5.14_linux_64.run
mkdir nvidia_installers
./cuda_6.5.14_linux_64.run -extract=`pwd`/nvidia_installers
cd nvidia_installers
./NVIDIA-Linux-x86_64-340.29.run
```

launch the drive

```
sudo modprobe nvidia
```

install the samples

```
./cuda-linux64-rel-6.5.14-18749181.run
./cuda-samples-linux-6.5.14-18745345.run
```


Now we can check if we messed anyhting up. 

```
cd /usr/local/cuda/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery 
```

We should get this


```
 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GRID K520"
  CUDA Driver Version / Runtime Version          6.5 / 6.5
  CUDA Capability Major/Minor version number:    3.0
  Total amount of global memory:                 4096 MBytes (4294770688 bytes)
  ( 8) Multiprocessors, (192) CUDA Cores/MP:     1536 CUDA Cores
  GPU Clock rate:                                797 MHz (0.80 GHz)
  Memory Clock rate:                             2500 Mhz
  Memory Bus Width:                              256-bit
  L2 Cache Size:                                 524288 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(65536), 2D=(65536, 65536), 3D=(4096, 4096, 4096)
  Maximum Layered 1D Texture Size, (num) layers  1D=(16384), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(16384, 16384), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device PCI Bus ID / PCI location ID:           0 / 3
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 6.5, CUDA Runtime Version = 6.5, NumDevs = 1, Device0 = GRID K520
Result = PASS
```


















