# Departure board servers (Python)

This repository contains the source code for the Python Departure board servers, which can be plugged into the [Python Departure module](https://pypi.org/project/departure/).

It contains the following board server back ends:

- Pygame,
- SDL2,
- LED matrix, for physical departure boards powered by Raspberry Pi and the Python bindings of the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) project.

 

### Installation

On Debian-based Linux (and similarly for other flavours of Linux), for the Pygame back end, make sure the following packages are installed:

```
$ sudo apt-get install python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion \
    libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev \
    libfreetype6-dev
```

The SDL2 back end is built on PySDL2: see https://pysdl2.readthedocs.io/en/latest/install.html#prerequisites its prerequisites.

**Note** – For this back end, before starting the server, [make sure](https://pysdl2.readthedocs.io/en/latest/integration.html#importing) that the `PYSDL2_DLL_PATH` environment directory points to the SDL2 library (e.g. [`SDL2.dll`](https://www.libsdl.org/download-2.0.php) on Windows) if it's not in the standard library directories.



The Pygame and SDL2 back ends can be installed using:

```
$ pip install departure-server-pygame
$ pip install departure-server-sdl
```

These commands will install the prerequired Python packages.



To use the LED matrix back end on a Raspberry Pi with suitable LED matrices (e.g. 3 64x32 matrices), [first install the rgbmatrix module as per the instructions](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python), then run:

```
$ pip install departure-server-led-matrix
```



### Usage

Use the `departure-server` command to start a board server with a specific back end.

Running the command without an argument will show the available back ends.

```
$ departure-server
```

![departure-server CLI](https://raw.githubusercontent.com/spujadas/departure-python/master/docs/images/departure-server.svg)

Once the board server has been started, on the client side (e.g. using the `departure` CLI or the Departure web API server), set the `DEPARTURE_BOARD_SERVER` environment variable to the IP address or hostname of the server, then start the client.

Here is an image of the board server running the Pygame back end:

![Pygame virtual departure board - SNCF (FR) - Paris Montparnasse](https://user-images.githubusercontent.com/930566/95666195-a13b2400-0b57-11eb-841d-c56e0ecbd704.gif)



### About

Written by [Sébastien Pujadas](https://pujadas.net/), released under the [MIT license](https://github.com/spujadas/departure-python/blob/master/LICENSE).