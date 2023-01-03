# Project_Zomboid_MOD_Crawler

프로젝트 좀보이드 모드 모음집 링크를 통하여 자동으로 MOD ID, MOD NAME, MAP FOLDER를 수집합니다.

수집된 정보는 DockerCompose를 위한 .env파일로 생성됩니다.

## 사용방법

1. 가상환경 생성 및 실행

2. !pip install requirements.txt

3. python main.py -u URL -p PATH

### 사용예시

```
python main.py -u https://steamcommunity.com/sharedfiles/filedetails/?id=2904181752 -p ./
```

## 매개변수

`-u, --url:` 프로젝트 좀보이드 모드 모음집 링크

`-p, --env_path:` 저장될 .env의 경로

## TODO

- 가상환경 생성 후 requirements.txt로 모듈 설치, 파이썬 스크립트 실행까지 자동으로 마칠 수 있는 쉘 스크립트 제작하기.

- 최종목표는 DockerFile 혹은 docker-compose를 사용하여 실행까지 이루어질 수 있도록 하는 것.

- (new) 크롤링이 아닌 steamworks api를 사용하여 DB에 넣고 crontab 비교하기

## COMPLETE

- requirements.txt 로 필요한 모듈 바로 설치 할 수 있음.

- main.py에 파라미터 적용 완료.

- 파이썬 스크립트로만 .env 파일 생성 가능.

## Reference

https://hub.docker.com/r/renegademaster/zomboid-dedicated-server
