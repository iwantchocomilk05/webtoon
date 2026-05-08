# Webtoon Community MVP

FastAPI 기반의 웹툰 커뮤니티 MVP 백엔드입니다.

## 실행 방법

```bash
python3 -m pip install -r requirements.txt
python3 -m uvicorn app.main:app --reload
```

## 확인 URL
- API 홈: http://127.0.0.1:8000/
- Swagger 문서: http://127.0.0.1:8000/docs

## 주요 엔드포인트
- `GET /`
- `GET /series`
- `GET /series/{series_id}`
- `GET /characters`
- `GET /posts`
- `POST /posts`
