import axios from 'axios';

type AiResultType = {
  status: string;
  result?: [] | string;
};

type TaskResultType = {
  top: string;
  top_color: string;
  bottom: string;
  bottom_color: string;
};

export default async function getAiResult(
  task_id: string,
): Promise<AiResultType> {
  return await axios.get(`api/v1/images/task/${task_id}`).then((res) => {
    console.log('getAiResult axios');
    console.log(res.data);
    return res.data;
  });
}
