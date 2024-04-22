wsl docker run --rm --name inspector^
    -e DISPLAY=:0 ^
    -v /tmp/.X11-unix:/tmp/.X11-unix ^
    mcr.microsoft.com/playwright:v1.43.0 npx -y playwright open google.com