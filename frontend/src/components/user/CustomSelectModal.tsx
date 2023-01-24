import { Button, Hidden, Typography } from '@mui/material';
import { Box } from '@mui/system';
import React, { SetStateAction, useState } from 'react';
import CheckColorList from './common/CheckColorList';

import CheckItemList from './common/CheckItemList';

const CustomSelectModal = ({
  modal,
  setModal,
  select,
  setInfo,
  gender,
}: {
  setModal: React.Dispatch<SetStateAction<boolean>>;
  select: string;
  setInfo: any;
  gender: string;
  modal: boolean;
}) => {
  const colorArr = {
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

  const styles: any = {
    female: {
      hair: ['short', 'middle', 'long'],
      top: [
        'blazer',
        'blouse',
        'cardigan',
        'coat',
        'hoodi',
        'jumper',
        'mustang',
        'onepiece',
        'pkshirts',
        'shirts',
        'sweater',
        'sweatshirts',
        't_shirts',
      ],
      bottom: [
        'denim',
        'half_shortpants',
        'leggings',
        'skirt',
        'slacks',
        'sweatpants',
      ],
      background: ['background1', 'background2', 'background3'],
    },
    male: {
      hair: ['short', 'middle', 'long'],
      top: [
        'blazer',
        'blouse',
        'cardigan',
        'coat',
        'hoodi',
        'jumper',
        'mustang',
        'onepiece',
        'pkshirts',
        'shirts',
        'sweater',
        'sweatshirts',
        't_shirts',
      ],
      bottom: [
        'denim',
        'half_shortpants',
        'leggings',
        'skirt',
        'slacks',
        'sweatpants',
      ],
      background: ['background1', 'background2', 'background3'],
    },
  };

  return (
    <Box
      sx={{
        width: '100%',
        height: '100%',
        color: 'black',
        background: '#FFCE00',
        display: modal ? 'flex' : 'block',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: 4,

        // justifyContent: 'center',
        // alignItems: 'center',
      }}
    >
      <CheckItemList
        select={select}
        setInfo={setInfo}
        title="Style"
        gender={gender}
        arr={styles[gender][select]}
      ></CheckItemList>
      <CheckColorList
        select={select + 'Color'}
        setInfo={setInfo}
      ></CheckColorList>

      <Button
        sx={{ color: 'black' }}
        onClick={() => {
          setModal(false);
        }}
      >
        <Typography variant="h4">OK</Typography>
      </Button>
    </Box>
  );
};

export default CustomSelectModal;
