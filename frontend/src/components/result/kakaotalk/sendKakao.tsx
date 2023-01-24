import React from 'react';

/* props 추가해서 ResultImg로부터 이미지 링크 받아오기 */
export const sendKakao = (resultImg: string) => {
  if (window.Kakao) {
    const kakao = window.Kakao;

    if (!kakao.isInitialized()) {
      kakao.init(import.meta.env.VITE_SOME_KEY);
    }
    // 메시지 공유 함수
    kakao.Share.sendCustom({
      //requestUrl: 'http://localhost:3000/', // 페이지 url
      templateId: 88903, // 메시지템플릿 번호
      templateArgs: {
        IMAGE: resultImg,
        TITLE: '내가 입은 코디를 반영한 나만의 심슨 캐릭터 ', // 제목 텍스트 ${TITLE}
        DESC: '나의 이미지 사진을 올려 AI가 판별 후 나만의 심슨을 만들어준다! 만들어진 심슨은 색과 스타일을 바꾸어 내 입맛대로 바꿀 수 있다.', // 설명 텍스트 ${DESC}
      },
      installTalk: true,
      callback: () => {
        console.log('공유 성공!');
      },
    });
  }
};
