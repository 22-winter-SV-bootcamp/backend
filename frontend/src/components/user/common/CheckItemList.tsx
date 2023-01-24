import { Button, Tooltip, Typography } from '@mui/material';
import { Box, Stack } from '@mui/system';
import React from 'react';

const CheckItemList = ({ gender, title, setInfo, arr, select }: any) => {
  return (
    <Box>
      <Typography variant="h4">{title}</Typography>
      <Box
        sx={{
          display: 'flex',
          width: '100%',
          height: 'auto',
          overflow: 'auto',
          overflowY: 'hidden',
        }}
      >
        {arr.map((v: any) => (
          <Button
            sx={{ width: 'auto' }}
            key={v}
            onClick={() => {
              setInfo((pre: any) => ({ ...pre, [select]: v }));
            }}
          >
            <Tooltip title={v}>
              <Box
                width={100}
                component="img"
                alt={v}
                src={
                  select === 'background'
                    ? `src/assets/custom/background/${v}.png`
                    : `src/assets/custom/${gender}/${select}/${v}.svg`
                }
              ></Box>
            </Tooltip>
          </Button>
        ))}
      </Box>
    </Box>
  );
};

export default CheckItemList;
