# 웹툰 통합 커뮤니티 사이트 기획안 (MVP)

## 1) 목표
- 한국 주요 플랫폼(네이버웹툰, 카카오웹툰/페이지, 레진, 캐롯툰 등)의 작품 정보를 한곳에서 탐색.
- 작품별 커뮤니티(게시판/댓글)와 캐릭터별 커뮤니티를 제공.
- 스포일러 관리, 팬덤 문화, 작품 비교 토론에 최적화된 UX 제공.

## 2) 핵심 기능 (MVP)
1. **작품 통합 디렉토리**
   - 작품명/작가/장르/연재상태/플랫폼 태그
   - 검색, 정렬(인기/최신 토론/평점)
2. **작품별 커뮤니티**
   - 자유글, 최신화 토론, 질문, 팬아트 카테고리
   - 좋아요/댓글/신고/블라인드 처리
3. **캐릭터 위키 + 커뮤니티**
   - 캐릭터 프로필(소속, 능력, 첫 등장화)
   - 캐릭터 전용 글타래/투표
4. **스포일러 안전장치**
   - 게시글 작성 시 스포일러 플래그
   - 회차 기반 스포일러 가림
5. **회원 시스템**
   - 닉네임 기반 계정
   - 관심 작품/캐릭터 팔로우

## 3) 데이터 모델 초안
- `Platform` (id, name, url)
- `Series` (id, title, platform_id, synopsis, author, genre, status, thumbnail_url)
- `Episode` (id, series_id, episode_no, title, release_date)
- `Character` (id, series_id, name, description, first_episode_id)
- `User` (id, email, nickname, role)
- `Post` (id, user_id, series_id nullable, character_id nullable, category, title, body, spoiler_level)
- `Comment` (id, post_id, user_id, body)
- `Follow` (id, user_id, series_id nullable, character_id nullable)

## 4) 정보 수집 전략
- **원칙**: 각 플랫폼의 이용약관/robots 정책 준수.
- 공식 API가 있으면 API 우선.
- API가 없다면 수동 등록 + 운영자 큐레이션으로 시작.
- 추후 제휴/공식 데이터 제공 계약을 목표.

## 5) 기술 스택 제안
- Frontend: Next.js + TypeScript + Tailwind
- Backend: NestJS 또는 FastAPI
- DB: PostgreSQL
- Search: PostgreSQL FTS (초기) → Elasticsearch/OpenSearch (확장)
- Auth: OAuth + 이메일 로그인
- Infra: Vercel/Cloudflare + managed DB

## 6) MVP 화면 구성
1. 홈: 인기 작품/인기 캐릭터/실시간 토론
2. 작품 상세: 작품 정보 + 작품 게시판
3. 캐릭터 상세: 캐릭터 위키 + 캐릭터 게시판
4. 글 상세: 댓글, 스포일러 가림, 신고
5. 마이페이지: 팔로우 목록, 활동 이력

## 7) 운영/정책
- 명확한 커뮤니티 가이드라인(비방, 불법 공유, 스포일러 기준).
- 저작권 침해(원본 이미지/회차 불법 업로드) 즉시 차단.
- 신고/제재 정책(경고, 임시정지, 영구정지).

## 8) 개발 로드맵 (8주)
- 1~2주: 정보 구조/DB 설계, 디자인 시스템
- 3~4주: 작품/캐릭터 페이지 + 게시판 CRUD
- 5~6주: 댓글/신고/스포일러 기능
- 7주: 검색/팔로우/알림
- 8주: 운영툴/배포/초기 QA

## 9) 바로 시작할 일 (실행 체크리스트)
- [ ] 서비스 이름/도메인 확정
- [ ] 타깃 사용자(연령/장르 성향) 정의
- [ ] 우선 연동 플랫폼 2~3개 선정
- [ ] DB 스키마 v1 작성
- [ ] 와이어프레임 5개 화면 제작
