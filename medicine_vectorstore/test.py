from dotenv import load_dotenv
load_dotenv()
from retriever import *
from vectorstore import load_vectorstore


vectorstore = load_vectorstore()

# 검색
results = retriever(
    query="증상: 복통, 빈도: 자주, 성별:여, 나이:12",
    ingredient_code="738600ATB",
    k=3
)

print(f"검색 결과 수 : {len(results)}\n")

for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"[Document {i}]")
    print("Metadata")
    print(doc.metadata)
    print("\nContent")
    print(doc.page_content[:1000])   # 너무 길면 앞 1000자만 출력
    print()