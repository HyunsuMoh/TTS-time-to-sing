# TTS(Time to Sing) -  Team SSG(Sogang & SmileGate)

## Python 환경 구축

프로젝트의 루트 디렉토리에는 anaconda 가상 환경 생성을 위한 conda_env.yaml 파일이 제공된다.

다음과 같이 이 파일을 내용을 import하여 anaconda 가상 환경을 생성하여 사용한다.

```
conda env create -f conda_env.yaml -n (name)
```

## 기본 제공 checkpoint 다운로드

학습된 모델의 상태를 저장하는 checkpoint 파일은 용량이 약 500MB로, github 업로드가 불가능하여 별도로 공유한다.

1. 아래의 링크에서 3개의 checkpoint 파일(.pt)을 다운로드한다.

https://drive.google.com/drive/folders/1nxq9F-OhZ-8pAQais38_7x2ym-6mIzEy?usp=sharing

2. 각각의 파일을 레포지토리의 루트 디렉토리(TTS-time-to-sing)에 저장한다.

3. 다운로드한 checkpoint는 노래 신호 합성 과정에서 default checkpoint로서 선택하여 사용할 수 있다.

## 프로그램 실행

(추후 업데이트)

## 음성 합성 결과 확인

CSD 데이터셋의 노래 50곡은 train set 41곡, validation set 1곡, test set 8곡으로 구성된다.

학습에 사용되지 않은 8곡의 테스트 곡 각각에 대하여, 3가지 기본 모델 3종류 음성의 원본 음성과 합성된 노래 음성을 비교할 수 있다.

아래의 링크에서 총 48개의 음성 파일을 확인할 수 있다.

https://drive.google.com/drive/folders/1hUmeV4tJBexueuSgusQ7R-nNCsumiY_D?usp=sharing
