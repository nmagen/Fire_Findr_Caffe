Setting Up EC2
---

### Starting the Instance

I'm going to use a g2.2xlarge instance which has:

* CPU: Intel Xeon E5-2670 and 15Gb of memory.

* GPU: NVIDIA GPU (1,536 CUDA cores) and 4GB of video memory.

* OS: 64-bit Ubuntu 14.04 Linux.


To do this one can navigate throught the [web site](aws.amazon.com). Alternatily, one could use the AWS CLI which allows you to launch instance programatically. The CLI the appropriate command would be:

```
aws ec2 run-instances --image-id ami-c3b8d6aa --count 1 --instance-type t1.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e
```

I ran my tests as spot isntances since the spot price was significantly lower than the on demand price (0.0061/hour ve 0.68/hour) (I bid 0.05/hour). 

After SSH-ing in confirm that the OS can "see" the GPU.

```sh
lscpu
sudo lshw -C display
```


### Installing dependancyies

I should also note that one could load one of the pre-built machine instances which would have a lot of these dependencyed allready installed. I'm doing it here mosly for eudicaitonal purpces. 






