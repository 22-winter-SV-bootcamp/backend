import React, { DragEvent, useEffect, useState } from 'react';
import UploadPng from '/Upload.png';
import bart from '../../assets/bart.png';
import titleone from '../../assets/titleone.png';
import titletwo from '../../assets/titletwo.png';
import { postUploadImage } from '@/apis/postUploadImage';
import loadingGif from '../../assets/loading.gif';

import { Box, Button, dividerClasses, Hidden } from '@mui/material';
import { display, height, padding, positions } from '@mui/system';
import { useMutation, useQuery } from '@tanstack/react-query';
import getAiResult from '@/apis/getAiResult';
import { useNavigate } from 'react-router-dom';

const DragDropUpload = () => {
  let [taskId, setTaskId] = useState('');

  let [isLoading, setIsLoading] = useState(false);
  let {
    data,

    refetch,

    isSuccess: Success,
  } = useQuery(['AiResult'], async () => await getAiResult(taskId), {
    enabled: false,
    staleTime: 1000 * 60 ** 60,
    refetchOnWindowFocus: false,

    onSuccess: (data: any) => {
      if (data?.status === 'not yet') setTimeout(refetch, 5000);
      else {
        setIsLoading(false);
        navigate('/custom', { state: data });
      }
    },
  });
  // console.log('data', data);

  const navigate = useNavigate();
  // console.log('success', Success);

  const {
    mutate,
    data: task_id,
    isError,
    error,
    isSuccess,
  } = useMutation(postUploadImage);
  // console.log('isS', isSuccess);

  const appendImageToFormData = (file: File) => {
    let formData = new FormData();
    formData.append('file', file);
    return formData;
  };

  const handleDragOver = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
  };
  const handleDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    let formData = appendImageToFormData(e.dataTransfer.files[0]);
    setIsLoading(true);
    mutate(formData, {
      onSuccess(task_id, variables, context) {
        // console.log('mutate', task_id.task_id);
        setTaskId(task_id.task_id);
      },
    });
  };

  useEffect(() => {
    if (taskId !== '') {
      refetch();
      // refetch().then(res=>navigate('/custom')); // 이렇게 쓰는게 나을까??
    }
  }, [taskId]);

  console.log('data', data);

  // useEffect(() => {
  //   if (Success) {
  //     navigate('/custom', { state: data });
  //   }
  // }, [Success]);

  const handleClickFileUpload = (
    e: React.ChangeEvent<HTMLInputElement> | any,
  ) => {
    e.preventDefault();
    let formData = appendImageToFormData(e.target.files[0]);

    mutate(formData, {
      onSuccess(task_id, variables, context) {
        console.log('mutate', task_id.task_id);
        setTaskId(task_id.task_id);
      },
    });
  };
  return (
    <Box
      sx={{
        backgroundColor: '#F8CD24',
        height: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Box
        sx={{
          width: '100%',
          minWidth: 400,
          maxWidth: 600,
          height: '100%',
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            flexDirection: 'column',
            width: '100%',
            height: '25%',
          }}
        >
          <Box
            component="img"
            src={titleone}
            alt="titleone"
            sx={{ width: 250, marginRight: 13 }}
          />
          <Box
            component="img"
            src={titletwo}
            alt="titletwo"
            sx={{ width: 200, marginLeft: 18 }}
          />
        </Box>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: '55%',
            marginTop: -6,
          }}
        >
          <Box
            component="label"
            sx={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              width: '50%',
              height: '70%',
              borderRadius: '10%',
              backgroundColor: 'rgba(255,255,255,0.7)',
              border: '3px dashed black',
              transition: '200ms',
              '&:hover': {
                transform: 'scale(1.1)',
              },
            }}
            onDragOver={handleDragOver}
            onDrop={handleDrop}
          >
            <input
              onChange={handleClickFileUpload}
              hidden
              multiple
              type="file"
            />

            {!isSuccess && (
              <Box component="img" src={UploadPng} alt="UploadIcon" />
            )}
            {isSuccess && (
              <Box component="img" src={loadingGif} alt="loading" />
            )}
          </Box>
        </Box>

        <Box
          component="img"
          src={bart}
          sx={{
            right: 0,
            bottom: 0,

            position: 'absolute',
            maxWidth: 300,
            maxHeight: 300,
          }}
        ></Box>
      </Box>
    </Box>
  );
};

export default DragDropUpload;
