# Sublime Text 3 작업 환경 설정 #


## 플러그인 ##

* *Package Control* : [설치방법 링크](https://sublime.wbond.net/installation)
* *Emmet* : HTML, CSS을 쉽고 편리하게 작성하게 도와즘.
* *AutoFileName* : 코드 작성시 이미지 등 로컬 파일 주소 작성을 도와줌.
* *Open Include* : 코드내 연결된 파일 쉽게 열수 있도록 도와줌.
* *View in Browser* : HTML 파일 브라우져로 열어줌.
* *Sidebar Enhancements* : Sidebar에 더 많은 기능을 넣어줌.정
* TagWrapper : Dreamweaver의 Ctrl+T와 비슷한 기능을 함(태그 단축키 지정 및 Wrapping). [설치방법 링크](https://github.com/ignacysokolowski/SublimeTagWrapper)
* Bracket Highlighter
* Git
* GitGutter

## 환경설정 ##

*참고사항*

super 키는 ctrl(Windows), command(MAC) 키임.


### Preferences.sublime-settings ###

* close windows when empty : false
* folder exclued patterns : .idea(webstorm)
* highlight line : true
* hot exit : false
* preview on click : false
* remember open file : false
* word wrap : true

### Default.sublime-keymap ###

* super + f12 : 현재 작성중인 html 파일 브라우져로 띄우기
* 멀티셀렉트 키 변경 : mac에서 다른 키와 중복되어 수정함(불필요할 경우 수정 or 삭)

### Emmet.sublime-settings ###

* 자동 완성 후 ":" 다음 공백 없앰
* html lang 기본 값 "ko"로 변경
* html snippet 추가
 	* !d : 개발 주석 코드 자동 완성
	* !j : 마크업 확인용 jquery 코드값 자동 완성

### Project 설정 ###

* Project > Add Folder to Project : 작업 폴더 선택
* Project > Save Project As : 프로젝트 세팅 파일 저장
* Proejct > Edit Proejct : sublimeTextWorkFolder.sublime-proejct 파일 참고하여 자신에 맞게 수정

### TagWrapper ###

단축키 사용을 위해 tag_wrapper.py 파일 수정 함.

class TagWrapperCommand() 함수의 아래 코드 주석 처리

	if s.empty():
		continue


## 단축키 ##

* super + t : tag wrapper input
* super + ctrl + p : <p\> tag insert
* super + ctrl + o : <ol\> tag insert
* super + ctrl + u : <ul\> tag insert
* super + ctrl + l : <li\> tag insert
* super + f12 : Open in browser
* alt + d : direct file open
* alt + shift + s : strip tags





