import { Button, ButtonGroup, Typography } from '@mui/material';
import { Box } from '@mui/system';
import React from 'react';
import Tooltip from '@mui/material/Tooltip';
type ColorArrType = {
  [key: string]: string;
};

const CheckColorList = ({ setInfo, select }: any) => {
  const colorArr: ColorArrType = {
    white: '#f9f6f6',
    coolGray: '#d4d4d4',
    gray: '#a6a6a6',
    darkGray: '#4b5053',
    charcoal: '#444444',
    red: '#900000',
    orange: '#d98200',
    yellow: '#ffcb00',
    navy: '#2c376f',
    purple: '#8a00ac',
    green: '#0a7c00',
    black: '#000000',
    neonBlue: '#02abcf',
    peach: '#DF5353',
    darkBrown: '#362710',
    brown: '#4A3A2A',
    darkBagie: '#A3907B',
    bagie: '#A3907B',
    ligthBegie: '#A3907B',
    lightIvory: '#F5EFEF',
    ivory: '#DED3AA',
    kaki: '#3C492A',
    ligthBlue: '#CCE7FF',
    middleBlue: '#417797',
    darkBlue: '#165690',
    denim: '#1A2B47',
    sora: '#5C71C9',
    skyBlue: '#9CB0FF',
    pink: '#FFB6B6',
  };

  return (
    <Box>
      <Typography variant="h4">Color</Typography>
      <Box
        sx={{
          display: 'flex',
          width: '100%',
          height: 70,
          overflow: 'auto',
          overflowY: 'hidden',
        }}
      >
        {Object.keys(colorArr).map((color: string) => (
          <Button>
            <Tooltip
              title={color}
              arrow
              placement="top"
              sx={{ width: 60 }}
              onClick={() => {
                setInfo((pre: any) => ({ ...pre, [select]: color }));
              }}
            >
              <Box
                sx={{
                  borderRadius: '100%',
                  width: 40,
                  height: 40,
                  backgroundColor: colorArr[color],
                }}
              ></Box>
            </Tooltip>
          </Button>
        ))}
      </Box>
    </Box>
  );
};

export default CheckColorList;
