#!/bin/bash

# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 21/03/2023
# ==============================================================================
VERSION=1.0
PRODUCT=gml_cnpj
SUBPRODUCT=bi_ce
IMAGE_NAME=${PRODUCT}/${SUBPRODUCT}

echo ">>> Initializing Docker-App image for ${IMAGE_NAME} . . ."
docker build -f dockerfile-bi --tag ${IMAGE_NAME}:${VERSION} .
