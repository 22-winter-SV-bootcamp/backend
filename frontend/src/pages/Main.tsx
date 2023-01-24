import { Box } from '@mui/material';
import React from 'react';
import DragDropUpload from '@/components/main/DragDropUpload';
import RecentImgs from '@/components/main/RecentImgs';
import RankingImgs from '@/components/main/ranking/RankingImgs';


const Main = () => {

  return (
    <Box
      sx={{
        width: '100%',
        height: '100%',
      }}
    >
      {/* 슬라이드 그림 오는 자리 */}
      <RecentImgs></RecentImgs>
      {/* 업로드 버튼 오는 자리 */}
      <DragDropUpload></DragDropUpload>
      {/* 랭킹 보여주는 자리 */}
      <RankingImgs />
    </Box>
  );
};

export default Main;
