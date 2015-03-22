Setting Up EC2
---

### Starting the Instance

I'm going to use a g2.2xlarge instance which has:

* CPU: Intel Xeon E5-2670 and 15Gb of memory.

* GPU: NVIDIA GPU (1,536 CUDA cores) and 4GB of video memory.

* OS: 64-bit Ubuntu 14.04 Linux.


To do this one can navigate through the [web site](www.aws.amazon.com). Alternatively, one could use the AWS CLI which allows you to launch instance programmatically. The CLI the appropriate command would be:

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
sudo apt-get install -y gcc g++ gfortran build-essential git wget python-dev python-pip python-nose python-numpy python-scipy
```

***Installing LAPAC***


```sh
sudo apt-get install -y libblas3gf
sudo apt-get install -y libblas-doc
sudo apt-get install -y libblas-dev
sudo apt-get install -y liblapack3gf
sudo apt-get install -y liblapack-doc
sudo apt-get install -y liblapack-dev

```

***BLAS via ATLAS***

```sh
apt-get source atlas
apt-get build-dep atlas
apt-get install devscripts
```










