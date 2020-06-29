# ALLENNLPDEMO LOCAL SERVER

There are two ways to use this repo:

## Go to nlp8 and run request.py

To make a request on the endpoint \predict run command: 

`python request.py -u "http://localhost:8000" -a "\predict" -d data.json -o out.json`

-u is the endpoint for the demo (in our case it is http://localhost:8000) and -d is the data you are sending over. -o is the output file.

## Use Jupyter notebook locally
To use the jupyter notebook and run it on the server

On bash locally run
```ssh -N -f -L localhost:PORT_OF_YOUR_CHOICE:localhost:8866 your_username@nlp8.cs.ucla.edu```

PORT_OF_YOUR_CHOICE is any port number you want to use. your_username is the way that you log into nlp8

Then on browser of your choice go to this url : ``` http://localhost:PORT_OF_YOUR_CHOICE/ ``` and go to AllenNLPDemo.ipynb.
