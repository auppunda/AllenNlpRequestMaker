# sample_request

There are two ways to use this repo:

## Go to nlp8 and run request.py

To make a request on the endpoint \predict run command: 

`python request.py -u "http://localhost:8000" -a "\predict" -d data.json -o out.json`

-u is the endpoint for the demo (in our case it is http://localhost:8000) and -d is the data you are sending over. -o is the output file.

## Use Jupyter notebook locally
To use the jupyter notebook and run it on the server

On bash locally run
```ssh -N -f -L localhost:8888:localhost:8866 your_username@nlp8.cs.ucla.edu```

Then on browser of your choice go to this url : ``` http://localhost:8888/ ``` and go to AllenNLPDemo.ipynb.
