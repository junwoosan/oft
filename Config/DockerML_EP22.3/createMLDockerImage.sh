#!/bin/bash
echo "Starting DockerML build..."
# configure optional the docker location for different ML image versions (default: MATLAB_RELEASE_SERVER=harbor.btc-es.local/cache_dockerhub/mathworks/matlab-deps)
# configure optional Matlab release version (default: MATLAB_RELEASE=r2022a) see https://hub.docker.com/r/mathworks/matlab-deps
# configure optional the Matlab products (default: MATLAB_PRODUCTS=Embedded_Coder MATLAB MATLAB_Coder Simulink Simulink_Coder Simulink_Coverage Simulink_Test Stateflow)
# configure optional (default: EP_RELEASE_LOCATION=harbor.btc-es.local/ep/ep-22.3p0:sprint4)
# 
# build the image with default configuration:
# docker build-t epml:local .
#
docker build --build-arg EP_RELEASE_LOCATION=harbor.btc-es.local/ep/ep-22.3p0:sprint4 --build-arg MATLAB_RELEASE_SERVER=harbor.btc-es.local/cache_dockerhub/mathworks/matlab-deps --build-arg MATLAB_RELEASE=r2022a --build-arg MATLAB_PRODUCTS="MATLAB Simulink Stateflow" --build-arg HOST_TMP_DIR=/tmp/mltmp -t epml:local .

# docker build --build-arg EP_RELEASE_LOCATION=btces/ep:latest --build-arg MATLAB_RELEASE_SERVER=mathworks-ref-arch/container-images/matlab-deps --build-arg MATLAB_RELEASE=r2022a --build-arg MATLAB_PRODUCTS="MATLAB Simulink Stateflow" --build-arg HOST_TMP_DIR=/tmp/mltmp -t epml:local .

echo "Docker build done, you can now use the image 'epml:local'!"
