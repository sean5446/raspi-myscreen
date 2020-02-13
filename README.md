# raspi-myscreen

![raspberrypi with screen](https://i.imgur.com/bqWEFe3.jpg)

## Hardware setup
https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi/easy-install-2

## SSL connection problem at boot
The raspi does not have enough entropy at boot sometimes causing the error: 

`handshake error: Error([('', 'osrandom_rand_bytes', 'getrandom() initialization failed.')],)",)`

### Try installing the following: 


`apt-get install rng-tools` https://wiki.archlinux.org/index.php/Rng-tools


 `apt-get install haveged`  https://wiki.archlinux.org/index.php/Haveged
