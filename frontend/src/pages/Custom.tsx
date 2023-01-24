import CustomInfo from '@/components/user/CustomInfo';
import CustomSelectModal from '@/components/user/CustomSelectModal';
import CustomSVG from '@/components/user/CustomSVG';
import { SettingsInputAntennaTwoTone } from '@mui/icons-material';
import { Box, createTheme, styled } from '@mui/system';
import React, { useEffect, useRef, useState } from 'react';
import { useLocation } from 'react-router-dom';
import domtoimage from 'dom-to-image';
import { saveAs } from 'file-saver';
import * as htmlToImage from 'html-to-image';
import { toPng, toJpeg, toBlob, toPixelData, toSvg } from 'html-to-image';

const theme = createTheme({
  /* custom MediaQuery */
  breakpoints: {
    values: {
      mobile: 480,
      tablet: 768,
      laptop: 0,
      desktop: 1024,
    },
  },
});

declare module '@mui/material/styles' {
  /* 타입 스크립트때문에 사용 */
  interface BreakpointOverrides {
    xs: false; // removes the `xs` breakpoint
    sm: false;
    md: false;
    lg: false;
    xl: false;
    mobile: true; // adds the `mobile` breakpoint
    tablet: true;
    laptop: true;
    desktop: true;
  }
}

const Box2 = styled('div')(({ theme }) => ({
  [theme.breakpoints.down('mobile')]: {
    flexDirection: 'column',
  },
  // [theme.breakpoints.up('tablet')]: {},
  // [theme.breakpoints.up('desktop')]: {},
}));

const Custom = () => {
  const [info, setInfo] = useState({
    gender: 'female',
    hair: 'long',
    hairColor: 'red',
    top: 'blazer',
    topColor: 'blue',
    bottom: 'jeans',
    bottomColor: 'green',
    background: 'background1',
  });
  const location = useLocation();
  const svgRef: any = useRef();
  console.log(svgRef);
  console.log(location.state.result);

  useEffect(() => {
    // TODO: 결과값 필터링 하기
    let { top, bottom } = location.state.result;

    if (top === '-blazer') top = 'blazer';
    if (top === 't-shirts') top = 't_shirts';
    if (bottom === 'Half-shortpants') top = 'half_shortpants';

    setInfo((pre: any) => ({ ...pre, top: top, bottom: bottom }));
  }, []);

  return (
    <Box2
      theme={theme}
      sx={{
        background: 'black',
        width: '100vw',
        height: '100vh',
        display: 'flex',

        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <div
        style={{
          width: '100%',
          height: '100%',
          minWidth: 300,
          minHeight: 300,
          maxHeight: 300,
          maxWidth: 500,
        }}
        ref={svgRef}
      >
        <CustomSVG ref={svgRef} info={info}></CustomSVG>
      </div>

      <CustomInfo svgRef={svgRef} info={info} setInfo={setInfo}></CustomInfo>
    </Box2>
  );
};

export default Custom;
