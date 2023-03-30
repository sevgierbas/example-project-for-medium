## example-project-for-medium

## Installation

`pip install fastapi `     
`pip install "uvicorn[standard]"`       
`uvicorn main:app –reload`  
 
## Usage

- import uvicorn 

+ from fastapi import FastAPI


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
    
 
    
