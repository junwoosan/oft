#! /bin/bash

${1}/ep \
    -clearPersistedState \
    -application ep.application.headless \
    -nosplash -console -consoleLog \
    -vmargs \
        -Dep.linux.config=${2} \
        -Dlogback.configurationFile=${3} \
        -Dep.configuration.logpath=${4} \
        -Dep.runtime.workdir=${5} \
        -Dbtc.root.temp.dir=${6} \
        -Dep.licensing.location=${7} \
        -Dep.licensing.package=${8} \
        -Dep.rest.port=${9} \
        -Dep.matlab.ip.range=127.0.0.1  2>&1 >/dev/null &

matlab
