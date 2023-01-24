import React, { useEffect } from 'react';
import Simpson from '../../assets/Simpson.png';
import Simpson2 from '../../assets/Simpson2.png';
import Simpson3 from '../../assets/Simpson3.png';

import CancelPresentationIcon from '@mui/icons-material/CancelPresentation';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { EasterImgLayout, ModalLayout, theme } from '../utils/muiResponse';

const styleModal = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '80vw' /* 16x32= 500px(default값 16) */,
  height: '90vh' /* 16x25= 400px(default값 16) */,
  bgcolor: 'background.paper',
  border: '2px solid #2196f3',
  borderRadius: 5,
  boxShadow: 24 /* 그림자 효과 */,
  p: '2%' /* padding */,
  display: 'flex' /* 레이아웃 */,
  flexDirection: 'column' /* 세로 방향 */,
};

const styleRow = {
  position: 'relative',
  height: '20%',
  display: 'flex' /* 레이아웃 */,
  flexDirection: 'row' /* 가로 방향 */,
  justifyContent: 'center' /* 중앙으로 이동 */,
  pr: '30px',
  pl: '30px',
};

const styleIcon = { position: 'absolute', right: 1, top: 1 };

export function EasterEgg({
  text,
  textSize,
  img1,
  img2,
  img3,
}: {
  text: string;
  textSize: string;
  img1: string;
  img2: string;
  img3: string;
}) {
  const [open, setOpen] = React.useState(true);
  // const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  console.log(styleModal);
  useEffect(() => {
    console.log(open); /* 모달창 상태 확인 */
  }, [open]);

  const styleImg = {
    /* props 사용하기 위해 함수형 컴포넌트 안에 배치 */
    width: '46vw' /* 16x8.5= 136px(default값 16) */,
    //height: '64vh' /* 16x19.5= 312px(default값 16) */,
    height: '76%',
    alignSelf: 'center',
    objectFit:
      'contain' /* 비율유지한채, 이미지 잘리지 않게, 남는공간 비워둠 */,
    content: {
      laptop: `url(${img1})`, //img src from 0 up to mobile
      mobile: `url(${img1})`, //img src from mobile up to tablet
      tablet: `url(${img2})`, //img src from tablet up to desktop
      desktop: `url(${img3})`, //img src from desktop up to ~
    },
    alt: 'Loading...',
  };

  return (
    // <Container fixed>
    <Modal
      open={open} /* true 이면 모달창 open */
      onClose={handleClose} /* 빈 창 누르면 모달창 close */
      aria-labelledby="modal-title" /* 모달 제목 */
      aria-describedby="modal-description" /* 모달 설명 */
    >
      <ModalLayout sx={styleModal} theme={theme}>
        <Box sx={styleRow}>
          <Typography
            id="modal-title"
            variant="h2"
            component="h2"
            style={{
              textAlign: 'center' /* 텍스트(컴포넌트) 가운데 정렬 */,
              fontWeight: 'medium' /* font 두꼐 */,
              fontSize: `${textSize}em` /* font 사이즈 */,
            }}
          >
            {text}
          </Typography>
          <IconButton color="primary" onClick={handleClose} sx={styleIcon}>
            <CancelPresentationIcon fontSize="large" />
          </IconButton>
        </Box>
        {/* 자체 정렬 */}
        <EasterImgLayout sx={styleImg} theme={theme}>
          <Box component="img" id="modal-description" sx={styleImg}></Box>
        </EasterImgLayout>
      </ModalLayout>
    </Modal>
    //</Container>
  );
}
