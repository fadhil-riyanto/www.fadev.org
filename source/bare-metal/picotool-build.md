# picotool build

## os setup

```sh
sudo pacman -S cmake arm-none-eabi-gcc arm-none-eabi-newlib
```

## setup picosdk

```sh
git clone https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
export PICO_SDK_PATH=$PWD
```

## build picotool

```sh
git clone https://github.com/raspberrypi/picotool.git
cd picotool
mkdir build
cd build
cmake ..
make
```

if you get cmake error minimum etc..., use `cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5` instead