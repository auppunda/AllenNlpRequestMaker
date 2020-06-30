# ALLEN NLP DEMO LOCAL SERVER

There are two ways to use this repo:

## Go to nlp8 and run request.py
The Models as of right now the server is capable of handling is named-entity-recognition, open-information-extraction, and semantic-role-labeling. If you want to run one of these models, the api call that needs to be made is at /api/MODEL_NAME/predict.

`python request.py -u "http://localhost:8080" -a "\api\MODEL\predict" -d data.json -o out.json`

-u is the endpoint for the demo (in our case it is http://localhost:8080) and -d is the data you are sending over. -o is the output file.

## Use Jupyter notebook locally
To use the jupyter notebook and run it on the server

On bash locally run 

```ssh -N -f -L localhost:PORT_OF_YOUR_CHOICE:localhost:8867 your_username@nlp8.cs.ucla.edu```

PORT_OF_YOUR_CHOICE is any port number you want to use. your_username is the way that you log into nlp8

Then on browser of your choice go to this url : ``` http://localhost:PORT_OF_YOUR_CHOICE/ ``` and go to AllenNLPDemo.ipynb.
