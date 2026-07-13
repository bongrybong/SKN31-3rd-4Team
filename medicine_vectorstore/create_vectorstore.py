from dotenv import load_dotenv
import pandas as pd

from documents import documents
from vectorstore import create_vectorstore

#### 1번만 실행 ####

load_dotenv()

df = pd.read_excel("data/medicine.xlsx")

docs = documents(df)

print('시작')
create_vectorstore(docs)

print("Vector DB 생성 완료")