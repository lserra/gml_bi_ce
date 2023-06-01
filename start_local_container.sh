#!/bin/bash

# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 21/03/2023
# ==============================================================================
echo ">>> Running BI container . . ."
docker run --rm \
  --network gml-cnpj \
  --publish 8501:8501 \
  --name gml_cnpj_bi \
  -i -t gml_cnpj/bi:1.0
