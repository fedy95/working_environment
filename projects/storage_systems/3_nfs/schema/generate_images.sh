#!/usr/bin/env bash

if [[ -z "${PROJECT_PATH}" ]]; then
  PROJECT_PATH=$(pwd)
fi

PLANTUML=${PROJECT_PATH}/vendor/bin/plantuml
SCHEMA=projects/storage_systems/3_nfs/schema/

$PLANTUML $SCHEMA/puml/*.puml -o "../png/"