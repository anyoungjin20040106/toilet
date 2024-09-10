from fastapi import FastAPI, Form
import joblib

# FastAPI 애플리케이션 생성
app = FastAPI()

# 모델 로드
model = joblib.load('toiletmodel.pkl')

@app.post("/toilet")
def predict(longitude: str=Form(...), latitude: str=Form(...)):
    X_new = [[float(longitude), float(latitude)]]
    prediction = model.predict(X_new)
    return {"prediction": prediction[0]}