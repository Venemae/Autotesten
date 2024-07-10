wsl docker run --rm -ti --name runner^
    -e DISPLAY=:0 ^
    -v /tmp/.X11-unix:/tmp/.X11-unix ^
    -v "$PWD"/mount:/test ^
    runner:playwright