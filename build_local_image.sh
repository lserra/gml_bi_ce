#!/bin/bash

# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 21/03/2023
# ==============================================================================
echo ">>> Creating Docker Network . . ."
docker network create gml-cnpj

VERSION=1.0
PRODUCT=gml_cnpj

SUBPRODUCT=bi
IMAGE_NAME=${PRODUCT}/${SUBPRODUCT}

sleep 5

echo ">>> Initializing Docker-App image for ${IMAGE_NAME} . . ."
docker build -f dockerfile-bi --tag ${IMAGE_NAME}:${VERSION} .
