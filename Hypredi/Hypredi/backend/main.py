from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np
import pickle
# trained_model
loaded_model = pickle.load(open('backend\hypertension_model.sav','rb'))
# Database connection details
db_user = 'postgres'
db_password = 'proshort123'
db_host = 'localhost'
db_port = '5432'
db_name = 'ent_fapi'

# Create database engine
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
Base = declarative_base()

# Define database model
class login_details(Base):
    __tablename__ = 'login_details'
    email_id = Column(String, primary_key=True)
    password = Column(String)

# Create tables in the database
Base.metadata.create_all(engine)

# Create session maker
Session = sessionmaker(bind=engine)
session = Session()

# FastAPI instance
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Signup endpoint
@app.post("/signup")
async def signup(data: dict):
    username = data.get('username')
    password = data.get('password')
    new_user = login_details(email_id=username, password=password)
    session.add(new_user)
    session.commit()
    session.close()

# Signin endpoint
@app.post("/signin")
async def signin(data: dict):
    username = data.get('email')
    password = data.get('password')
    user = session.query(login_details).filter_by(email_id=username, password=password).first()
    return user is not None

# prediciton endpoint 
@app.post("/prediction")
async def prediction(data:dict):
    first_input = data.get("first_input")
    second_input = data.get("first_input")
    third_input = data.get("third_input")
    fourth_input = data.get("fourth_input") 
    data = (first_input,second_input,third_input,fourth_input)
    data_array = np.asarray(data)
    input_data_reshape = data_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshape)
    if(prediction[0] == 0):
        return 'No Hypertension'
    else:
        return  'Hypertension'
    
# Run the FastAPI app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
