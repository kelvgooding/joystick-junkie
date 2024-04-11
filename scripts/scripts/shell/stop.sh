#!/bin/bash

# Find the PID of the app.py process

pid=$(ps -ef | grep "python app.py" | grep -v grep | awk '{print $2}')

# Check if the PID is found

if [ -z "$pid" ]; then
    echo "No running instance of app.py found."
else
    # Kill the process

    kill $pid
    echo "app.py process with PID $pid has been stopped."
fi

