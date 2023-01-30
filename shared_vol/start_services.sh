#!/bin/bash

# Start the first process
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token= &
  
# Start the second process
python app.py