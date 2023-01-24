import { Box, Theme, useMediaQuery, useTheme } from '@mui/material';
import React from 'react';
import { ImageComponent } from './component';
import { ImageState, ImageType } from './types';

export default function RankingImgs() {
  const theme = useTheme();

  const isSmallScreen = useMediaQuery((theme: Theme) =>
    theme.breakpoints.down('laptop'),
  );

  const [imageState, setImageState] = React.useState<ImageState>({
    firstImage: {
      url: 'public/image 96.png',
      count: 123,
    },
    secondImage: {
      url: 'public/image 96.png',
      count: 222,
    },
  });

  const fetchFunc = async () => {
    const res = await fetch('/image').then((res) => res.json());
    setImageState(res);
  };

  React.useEffect(() => {
    fetchFunc();
  }, []);

  React.useEffect(() => {
    console.log(theme);
  }, [theme]);

  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: 'black',
        color: 'white',
      }}
    >
      <Box>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            //mobile
            [theme.breakpoints.between('mobile', 'tablet')]: {
              py: 4,
            },
            //tablet
            [theme.breakpoints.between('tablet', 'laptop')]: {
              py: 4,
            },
            //pc
            [theme.breakpoints.up('laptop')]: {
              py: 8,
            },
          }}
        >
          {!isSmallScreen && (
            <Box component={'img'} src="/image 104.png" sx={{ width: 1 }} />
          )}
          {isSmallScreen && (
            <Box component={'img'} src="/Group 58.png" sx={{ width: 0.6 }} />
          )}
        </Box>
        <Box sx={{ display: 'flex', justifyContent: 'center', pb: 8 }}>
          <Box sx={{ display: 'flex' }}>
            {Object.keys(imageState).map((v) => {
              return (
                <ImageComponent
                  imageState={imageState[v as ImageType]}
                  isEnd={v === 'secondImage'}
                />
              );
            })}
          </Box>
        </Box>
      </Box>
    </Box>
  );
}
