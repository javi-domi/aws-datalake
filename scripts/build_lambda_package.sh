#!/usr/bin/env bash

cd infra

# Declare variables for the script
PACKAGE='package'

# Create the package directory
if [ -d "$PACKAGE" ]
then
  echo "$PACKAGE already exists. Skipping creation."
else
  echo "Creating $PACKAGE directory..."
  mkdir "$PACKAGE"
  echo "Done."
fi

# Variable with the path to the file of the lambda requirements
LAMBDA_REQUIREMENTS=./etl/lambda_requirements.txt

# Verifies if the file exists
if [ -f "$LAMBDA_REQUIREMENTS" ]
then
  echo "Installing lambda requirements found in $LAMBDA_REQUIREMENTS..."
  pip install --target ./package -r $LAMBDA_REQUIREMENTS
  echo "Dependencies installed."
fi

cd $PACKAGE

# Declare variables with the path to the lambda functions
LAMBDA_FUNCTION=../../etl/lambda_function.py

# Verifies if the file exists
if [ -f "$LAMBDA_FUNCTION" ]
then
  echo "Copying lambda function..."
  cp $LAMBDA_FUNCTION .
  echo "Compacting file lambda_function_payload.py..."
  zip -r9 ../lambda_function_payload.zip .
  echo "File compacted successfully."
fi

cd ..