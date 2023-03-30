## example-project-for-medium

## Installation

`pip install fastapi `     
`pip install "uvicorn[standard]"`       
`uvicorn main:app –reload`  
 
## Usage
Run project with
```bash
uvicorn app:app --reload  
```
or 
```
if __name__ == "__main__":
uvicorn.run(app, host="127.0.0.1", port=8000)
```

For api documentation (swagger)
```bash
http://127.0.0.1:8000/docs
```
