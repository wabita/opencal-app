from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 追加
import random
import time

app = FastAPI()

# これを追加：フロントエンド（3000番）からのアクセスを許可する
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # 全てのメソッド（GET, POSTなど）を許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)


@app.get("/")
def read_root():
    return {"message": "Hello, your backend is working with CORS!"}
