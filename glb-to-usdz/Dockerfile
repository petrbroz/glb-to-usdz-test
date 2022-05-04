# Define function directory
ARG FUNCTION_DIR="/function"

FROM leon/usd-from-gltf:latest

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Install the runtime interface client
RUN pip install --target ${FUNCTION_DIR} awslambdaric

# Copy function code
COPY *.py ${FUNCTION_DIR}/

# Copy testing files
ADD https://petrbroz.s3.us-west-1.amazonaws.com/glb-to-usdz-issues/snowmobile.glb ${FUNCTION_DIR}/
ADD https://petrbroz.s3.us-west-1.amazonaws.com/glb-to-usdz-issues/wall-e.glb ${FUNCTION_DIR}/

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]
