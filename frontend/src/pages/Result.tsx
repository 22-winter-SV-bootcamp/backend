import { ResultImg } from '@/components/result/ResultImg';
import React from 'react';
import { useLocation } from 'react-router-dom';

const Result = () => {
  let location = useLocation();
  console.log('location state', location.state);

  return (
    <>
      <ResultImg />
    </>
  );
};

export default Result;
