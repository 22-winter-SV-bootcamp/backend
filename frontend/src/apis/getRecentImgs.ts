import axios from 'axios';

type CardsType = {
  id: number;
  link: string;
};

export default async function getRecentImgs(
  page: number,
): Promise<CardsType[]> {
  return await axios
    .get(`api/v1/images`, { params: { page: page } })
    .then((res) => {
      console.log('getgeget');
      console.log(res.data);
      return res.data;
    });
}
