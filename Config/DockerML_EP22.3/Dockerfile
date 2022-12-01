# To specify which EP release is used to copy EP into the new image
ARG EP_RELEASE_LOCATION=btces/ep

# To specify which location is used to download the matlab image
ARG MATLAB_RELEASE_SERVER=mathworks/matlab-deps
# To specify which MATLAB release to install in the container, edit the value of the MATLAB_RELEASE argument.
# Use lower case to specify the release, for example: ARG MATLAB_RELEASE=r2021b
ARG MATLAB_RELEASE=r2022a

# ----------------------------------------------------------------
# needs to be adapted to the customer environment
# ----------------------------------------------------------------
# location of the EP image btces/ep:tagname
FROM ${EP_RELEASE_LOCATION} as ep

# When you start the build stage, this Dockerfile by default uses the Ubuntu-based matlab-deps image.
# To check the available matlab-deps images, see: https://hub.docker.com/r/mathworks/matlab-deps
FROM ${MATLAB_RELEASE_SERVER}:${MATLAB_RELEASE}

# Declare the global argument to use at the current build stage
ARG MATLAB_RELEASE=r2022a

ARG HOST_TMP_DIR=F:\Docker\tmp

# Declare the global argument for desired Matlab products which have to be installed
ARG MATLAB_PRODUCTS="Embedded_Coder MATLAB MATLAB_Coder Simulink Simulink_Coder Simulink_Coverage Simulink_Test Stateflow"


# Install mpm dependencies & tini
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && \
    apt-get install --no-install-recommends --yes \
        wget \
        unzip \
        ca-certificates \
        curl \
        gcc \
        g++ && \
    apt-get clean && apt-get autoremove

# Run mpm to install MATLAB in the target location and delete the mpm installation afterwards.
# If mpm fails to install successfully then output the logfile to the terminal, otherwise cleanup.
RUN wget -q https://www.mathworks.com/mpm/glnxa64/mpm \ 
    && chmod +x mpm \
    && ./mpm install \
    --release=${MATLAB_RELEASE} \
    --destination=/opt/matlab \
    --products ${MATLAB_PRODUCTS} \
    || (echo "MPM Installation Failure. See below for more information:" && cat ${HOST_TMP_DIR}/mathworks_root.log && false) \
    && rm -f mpm ${HOST_TMP_DIR}/mathworks_root.log \
    && ln -s /opt/matlab/bin/matlab /usr/local/bin/matlab

# Add "matlab" user and grant sudo permission.
RUN adduser --shell /bin/bash --disabled-password --gecos "" matlab \
    && echo "matlab ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/matlab \
    && chmod 0440 /etc/sudoers.d/matlab

# One of the following 2 ways of configuring the license server to use must be
# uncommented.

ARG LICENSE_SERVER
# Specify the host and port of the machine that serves the network licenses 
# if you want to bind in the license info as an environment variable. This 
# is the preferred option for licensing. It is either possible to build with 
# something like --build-arg LICENSE_SERVER=27000@MyServerName, alternatively
# you could specify the license server directly using
#       ENV MLM_LICENSE_FILE=27000@flexlm-server-name
ENV MLM_LICENSE_FILE=$LICENSE_SERVER

# Alternatively you can put a license file into the container.
# You should fill this file out with the details of the license 
# server you want to use and uncomment the following line.
# COPY network.lic /opt/matlab/licenses/

# The following environment variables allow MathWorks to understand how this MathWorks 
# product (MATLAB Dockerfile) is being used. This information helps us make MATLAB even better. 
# Your content, and information about the content within your files, is not shared with MathWorks. 
# To opt out of this service, delete the environment variables defined in the following line. 
# See the Help Make MATLAB Even Better section in the accompanying README to learn more: 
# https://github.com/mathworks-ref-arch/matlab-dockerfile#help-make-matlab-even-better
ENV MW_DDUX_FORCE_ENABLE=true MW_CONTEXT_TAGS=MATLAB:DOCKERFILE:V1

# Set user and work directory
USER matlab
WORKDIR /home/matlab

# EP installation directory
ARG EP_INSTALL_PATH=/opt/ep
ENV EP_INSTALL_PATH=${EP_INSTALL_PATH}

# EP working root directory
ARG EP_WORK_DIR_ROOT=/tmp/ep
ENV EP_WORK_DIR_ROOT=${EP_WORK_DIR_ROOT}

# Linux registry file
ARG EP_REGISTRY=/opt/Configuration/eplinuxregistry
ENV EP_REGISTRY=${EP_REGISTRY}

# Logging configuration
ARG EP_LOG_CONFIG=${EP_INSTALL_PATH}/configuration/logback_linux.xml
ENV EP_LOG_CONFIG=${EP_LOG_CONFIG}

# Copy for installation of EP
COPY --chown=1000 --from=ep /opt/jres /opt/jres
COPY --chown=1000 --from=ep /opt/Configuration/eplinuxregistry ${EP_REGISTRY}
COPY --chown=1000 --from=ep /root/.BTC/ep/22.3p0/config/compiler_pref/compiler_setup.xml /root/.BTC/ep/22.3p0/config/compiler_pref/compiler_setup.xml
COPY --chown=1000 --from=ep /opt/ep ${EP_INSTALL_PATH}

COPY --chown=1000 addMLIntegration.bash /tmp/
COPY --chown=1000 startMatlab.bash /tmp/
RUN sudo chmod +x /tmp/addMLIntegration.bash
RUN sudo chmod +x /tmp/startMatlab.bash

RUN sudo /tmp/addMLIntegration.bash && rm /tmp/addMLIntegration.bash

# REST port
ARG REST_PORT
ENV REST_PORT=${REST_PORT:-8080}
EXPOSE ${REST_PORT}

# Location of license source, comma separated list of license files and license servers (<port>@<host>)
ARG LICENSE_LOCATION
ENV LICENSE_LOCATION=${LICENSE_LOCATION:-27000@flexlm-linux-1.btc-es.local}

# Activated marketing package (for licensing). Supported: EP_BASE and EP_COMPLETE
ARG LICENSE_PACKAGES
ENV LICENSE_PACKAGES=${LICENSE_PACKAGES:-ET_COMPLETE}

# Root directory for temporary files
ARG TMP_DIR
ENV TMP_DIR=${TMP_DIR:-${EP_WORK_DIR_ROOT}/tmp}

# Root directory for log files
ARG LOG_DIR
ENV LOG_DIR=${LOG_DIR:-${EP_WORK_DIR_ROOT}/logs}

# Working directory (for profile data)
ARG WORK_DIR
ENV WORK_DIR=${WORK_DIR:-${EP_WORK_DIR_ROOT}/workdir}

# Health check to test if the container is ready for requests
HEALTHCHECK CMD curl --fail -X GET "http://localhost:${REST_PORT}/ep/test" -H "Cache-Control: no-cache" || exit 1

# https://github.com/docker-library/official-images#consistency
# Set default command that can be overwritten on container startup
CMD /tmp/startMatlab.bash ${EP_INSTALL_PATH} ${EP_REGISTRY} ${EP_LOG_CONFIG} ${LOG_DIR} ${WORK_DIR} ${TMP_DIR} ${LICENSE_LOCATION} ${LICENSE_PACKAGES} ${REST_PORT}
