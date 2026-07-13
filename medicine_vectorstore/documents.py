import re
import pandas as pd
from langchain_core.documents import Document

df = pd.read_excel("data/medicine.xlsx")

def documents(df):
    docs = []  # 매 실행 시 초기화되도록 함수 내부로 이동
    
    for _, row in df.iterrows():
        # 주성분코드 결측치 처리
        code = str(row["주성분코드"]) if not pd.isna(row["주성분코드"]) else ""
        
        # 사용상의주의사항 결측치 처리
        text_val = row["사용상의주의사항"]
        if pd.isna(text_val):
            continue
        text = str(text_val).strip()

        # 줄 시작점(^)에 오는 '숫자. 제목' 패턴만 타겟팅 (re.MULTILINE 필수)
        pattern = r'^(\d+\.\s+[^\n]+)'
        matches = list(re.finditer(pattern, text, re.MULTILINE))

        # 매칭되는 제목이 아예 없는 텍스트 예외 처리
        if not matches:
            docs.append(
                Document(
                    page_content=text,
                    metadata={"ingredient_code": code, "section": "전체"}
                )
            )
            continue

        # 첫 번째 제목(1. 경고 등) 이전에 도입 문구가 있을 때 누락 방지
        first_match_start = matches[0].start()
        if first_match_start > 0:
            intro_chunk = text[:first_match_start].strip()
            if intro_chunk:
                docs.append(
                    Document(
                        page_content=intro_chunk,
                        metadata={"ingredient_code": code, "section": "개요"}
                    )
                )

        # 제목별 분할 및 Document 생성
        for i, match in enumerate(matches):
            start = match.start()
            
            if i + 1 < len(matches):
                end = matches[i + 1].start()
            else:
                end = len(text)

            chunk = text[start:end].strip()
            title = match.group().strip()

            docs.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "ingredient_code": code,
                        "section": title
                    }
                )
            )
            
    print(f"생성된 Document 수 : {len(docs)}")
    return docs