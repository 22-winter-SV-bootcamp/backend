import React, { useEffect, useRef, useState } from 'react';
import { Box, IconButton, styled } from '@mui/material';
import BacktoTop from '../../assets/BacktoTop.png';
import doh from '../../assets/doh.png';
import SpraySimpson from '../../assets/SpraySimpson.png';
import Download from '../../assets/Download.png';
import Instagram from '../../assets/Instagram.png';
import Kakaotalk from '../../assets/Kakaotalk.png';
import { ReactComponent as Home } from '../../assets/home.svg';
import { Navigate, useLocation, useNavigate } from 'react-router-dom';
import { imageDownload } from './imageDownload';
import { BoxSprayLayout, theme } from '../utils/muiResponse';
import { Copyelement } from './Copyelement';
import testSimpson from '../../assets/customSimpsonWoman.png';
import { sendKakao } from './kakaotalk/sendKakao';

const styleContainer = {
  position: 'relative',
  height: '100vh',
  bgcolor: 'black',
  overflow: 'hidden',
  display: 'flex' /* 레이아웃 */,
  flexDirection: 'column',
};

const styleIconLayout = {
  display: 'flex',
  position: 'relative',
  flexDirection: 'row',
  justifyContent: 'flex-end',
  width: '75%',
  maxWidth: '55vmin',
  minWidth: '285px',
  mb: '10px',
};

const styleImageLayout = {
  position: 'relative',
  width: '75%',
  maxWidth: '55vmin',
  minWidth: '285px',
  // display: 'block',
  // pb: '100%',
};

const styleSprayLayout = {
  position: 'absolute',
  display: 'none',
  bottom: '-200px',
  right: '-290px',
};

export function ResultImg() {
  const [hover, setHover] = useState('false');
  const [url, setUrl] = useState('');
  const location = useLocation();
  console.log(location.state);
  const navigate = useNavigate();

  useEffect(() => {
    /* Link로 결과 페이지로 넘어갈떄 props에 state값을 주면 결과 페이지 에서 사용 가능, 나는 이걸 url 상태값에 저장 */
    setUrl(location.state.link);
  });

  const goFirstPage = () => {
    /* 첫 페이지 */
    navigate('/', { replace: true });
  };

  const download = async () => {
    /* location의 state값이 undefined이 아니라는 걸 알려주기 위해 사용 */
    url &&
      imageDownload({
        href: url,
      });
  };

  return (
    <Box className="container" sx={styleContainer}>
      <Box className="firstLayout" sx={{ height: '14%', position: 'relative' }}>
        <Box
          className="doh"
          component="img"
          sx={{
            width: '30vw',
            maxWidth: '160px',
            minWidth: '120px',
            position: 'absolute',
            top: '3vh',
            left: '5vw',
          }}
          src={doh}
          onClick={goFirstPage}
        />
      </Box>
      <Box
        className="secondLayout"
        sx={{
          height: '64%',
          position: 'relative',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Box className="iconLayout" sx={styleIconLayout}>
          {/* <IconButton
            className="instagramButton"
            sx={{
              width: '15%',
              maxWidth: '3rem',
              p: '4px',
            }}
          >
            <Box
              className="instagram"
              component="img"
              sx={{
                // '&:hover': {
                //   width: '110%',
                // },
                width: '100%',
              }}
              src={Instagram}
            />
          </IconButton> */}
          <IconButton
            className="kakaotalkButton"
            sx={{
              width: '15%',
              maxWidth: '3rem',
              p: '4px',
            }}
            onClick={() => sendKakao(url)}
          >
            <Box
              className="kakaotalk"
              component="img"
              sx={{
                width: '100%',
              }}
              src={Kakaotalk}
            />
          </IconButton>
          <Box
            className="copyButton"
            sx={{
              width: '15%',
              // height: '30px',
              maxHeight: '30px',
              maxWidth: '3rem',
            }}
          >
            <Copyelement resultImg={url} />
          </Box>
        </Box>
        <Box className="imageLayout" sx={styleImageLayout}>
          <Box
            className="resultImg"
            component="img"
            sx={{ width: '100%', height: '100%' }}
            // src={location.state.link}
            src={url}
          />
          <IconButton /* 기본 패딩이 8 인듯 */
            className="downloadButton"
            sx={{
              position: 'absolute',
              width: '15%',
              maxWidth: '3rem',
              p: '4px',
              left: '0.5rem',
              bottom: '0.5rem',
            }}
            onClick={download}
          >
            <Box
              className="download"
              component="img"
              sx={{
                '&:hover': {
                  width: '130%',
                },
                width: '100%',
              }}
              src={Download}
            />
          </IconButton>
          <BoxSprayLayout
            className="sprayLayout"
            sx={styleSprayLayout}
            theme={theme}
          >
            <Box
              className="spraySimpson"
              component="img"
              sx={{ width: '400px' }}
              src={SpraySimpson}
            />
          </BoxSprayLayout>
        </Box>
      </Box>
      <Box
        className="thirdLayout"
        sx={{
          height: '22%',
          position: 'relative',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <IconButton
          className="backtotopButton"
          sx={{ width: '60vw', maxWidth: '270px', minWidth: '260px' }}
          onClick={goFirstPage}
        >
          <Box
            className="backtotop"
            component="img"
            sx={{ width: '100%', pb: '4rem' }}
            src={BacktoTop}
          />
        </IconButton>
      </Box>
    </Box>
  );
}
