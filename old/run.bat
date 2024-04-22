@REM vscode openen
start vscode://file/C:/test

@REM Headed test runnen in docker
wsl docker run --rm -ti --name runtest -e DISPLAY=:0 -v /mnt/c/test/tweakers.py:/test/test_run_test.py -v /tmp/.X11-unix:/tmp/.X11-unix menzis:test_runner /bin/bash

