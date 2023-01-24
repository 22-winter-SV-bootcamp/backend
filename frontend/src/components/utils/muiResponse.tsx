import { createTheme, styled } from '@mui/material';

export const BoxSprayLayout = styled('div')(({ theme }) => ({
  // [theme.breakpoints.between('laptop', 'desktop')]: {} /* 필요시 사용, 크기 조정*/,
  [theme.breakpoints.up('desktop')]: {
    display: 'inLine',
  },
}));

export const ModalLayout = styled('div')(({ theme }) => ({
  height: '100vh',
  padding: theme.spacing(1),
  [theme.breakpoints.up('desktop')]: {
    height: '50rem',
    width: '64rem',
    // fontSize: '8px',
  },
  // [theme.breakpoints.up('tablet')]: {},
  // [theme.breakpoints.up('desktop')]: {},
}));

export const EasterImgLayout = styled('div')(({ theme }) => ({
  height: '100vh',
  padding: theme.spacing(1),
  // [theme.breakpoints.between('tablet', 'desktop')]: {
  //   height: '70vh',
  //   width: '55vw',
  // },     /* 필요시 사용, 크기 조정*/

  [theme.breakpoints.up('desktop')]: {
    height: '420px',
    width: '400px',
  },

  // [theme.breakpoints.up('desktop')]: {},
}));

export const theme = createTheme({
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
