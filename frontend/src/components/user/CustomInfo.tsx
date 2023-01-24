import { Check } from '@mui/icons-material';
import { Button, Typography } from '@mui/material';
import { Box, height } from '@mui/system';
import axios from 'axios';
import React, { useState } from 'react';
import CheckItem from './common/CheckItem';
import CustomSelectModal from './CustomSelectModal';
import domtoimage from 'dom-to-image';
import { saveAs } from 'file-saver';
import { useNavigate } from 'react-router-dom';
const CustomInfo = ({ info, setInfo, svgRef }: any) => {
  const [modal, setModal] = useState(false);
  const [select, setSelect] = useState('hair');
  const navigate = useNavigate();

  let {
    gender,
    hair,
    hairColor,
    top,
    topColor,
    bottom,
    bottomColor,
    background,
  } = info;
  console.log('info가 바뀌었나?', info);

  const changeGender = (gender: string) => {
    let init =
      gender === 'male'
        ? {
            gender: 'male',
            hair: 'middle',
            hairColor: 'white',
            top: 't_shirts',
            topColor: 'white',
            bottom: 'slacks',
            bottomColor: 'white',
            background: 'background1',
          }
        : {
            gender: 'female',
            hair: 'long',
            hairColor: 'white',
            top: 't_shirts',
            topColor: 'white',
            bottom: 'slacks',
            bottomColor: 'white',
            background: 'background1',
          };

    setInfo(init);
  };

  return (
    <Box
      sx={{
        color: '#FFCE00',
        width: '100%',
        maxWidth: '400px',
        height: '400px',
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      <Box
        sx={{
          padding: 2,
          background: '#95989b',
          width: '90%',
          height: '100%',
          marginLeft: 'auto',
          display: modal ? 'none' : 'flex',
          flexDirection: 'column',

          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <Box
          sx={{
            width: '100%',
            height: 50,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <Typography variant="h4">gender</Typography>
          <Box>
            <Button
              onClick={() => {
                changeGender('female');
              }}
            >
              <Box
                sx={{ width: 50, height: 50 }}
                component="img"
                src={`src/assets/custom/gender/female.png`}
                alt="male"
              ></Box>
            </Button>
            <Button
              onClick={() => {
                changeGender('male');
              }}
            >
              <Box
                sx={{ width: 50, height: 50 }}
                component="img"
                src="src/assets/custom/gender/male.png"
                alt="female"
              ></Box>
            </Button>
          </Box>
        </Box>
        {['hair', 'top', 'bottom', 'background'].map((title) => (
          <CheckItem
            key={title}
            info={info}
            title={title}
            setModal={setModal}
            setSelect={setSelect}
          ></CheckItem>
        ))}
        <Button
          variant="contained"
          sx={{ alignSelf: 'end', background: '#D9D9D9', color: 'black' }}
          onClick={async () => {
            const svg = svgRef.current;
            console.log(svg);
            let d = new FormData();

            await domtoimage
              .toBlob(svg, {
                width: svg.clientWidth * 4,
                height: svg.clientHeight * 4,
                style: {
                  transform: 'scale(' + 4 + ')',
                  transformOrigin: 'top left',
                },
              })
              .then((blob) => {
                d.append('file', blob);
                console.log(d);
                saveAs(blob, 'card.png');
                for (const i of d) {
                  console.log(i);
                }
              });
            await axios
              .post('api/v1/styles', {
                file: d,
                gender: gender,
                top: top,
                top_color: topColor,
                bottom: bottom,
                bottom_color: bottomColor,
              })
              .then((res) => {
                console.log(res.data);
                navigate('/result', { state: res.data });
              });
          }}
        >
          <Typography variant="h4">Done</Typography>
        </Button>
      </Box>
      {modal && (
        <CustomSelectModal
          gender={info.gender}
          select={select}
          setInfo={setInfo}
          modal={modal}
          setModal={setModal}
        ></CustomSelectModal>
      )}
    </Box>
  );
};

export default CustomInfo;
