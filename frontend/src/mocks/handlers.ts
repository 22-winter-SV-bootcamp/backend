import { rest } from 'msw';

const dummy =
  'https://simsontest.s3.ap-northeast-2.amazonaws.com/83b17690-8e22-471b-ad3c-c8ffba67066d.jpg';

const dummyTaskId = { task_id: '1' };
const recentImgs = [
  {
    id: 1,
    link: 'https://w.namu.la/s/e33686f9d81f80bd310578b4373046f36841b7b419186077446bbcc3079f420bf6bbf5e2c8c996eba38defad7112d2bea8e8d443ca63dd067e97052ac70432163bb041fd54e014845928b66e6722f3157d47823fcd53e944353b2d640f7365d5053118970cb2c7391a842b27316c26d1',
  },
  {
    id: 2,
    link: 'https://images.justwatch.com/poster/263557090/s718/simseun-gajog.%7Bformat%7D',
  },
  {
    id: 3,
    link: 'https://img.insight.co.kr/static/2021/10/14/700/img_20211014164002_12fnlr61.webp',
  },
  {
    id: 4,
    link: 'https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2021%2F07%2Fdisney-plus-loki-the-simpsons-crossover-short-tw.jpg?w=960&cbr=1&q=90&fit=max',
  },
  {
    id: 5,
    link: 'https://www.themoviedb.org/t/p/original/ARIEA8fMTk8HLy8AyLbKyUjsqC.jpg',
  },
];

const recentImgs1 = [
  {
    id: 1,
    link: 'https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDRfMjQ4/MDAxNTg4NTY5ODM2MDEx.WyAMhYtqOIQRJ0K0ucdCUvSO4FoMrcxgTa5F7i33YbUg.Ls8hExGrAoSwTmn0oXHBU71Ar0bHoYOAHQyR2kXdCmwg.PNG.wonch888/image.png?type=w800',
  },
  {
    id: 2,
    link: 'https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDRfMjQ4/MDAxNTg4NTY5ODM2MDEx.WyAMhYtqOIQRJ0K0ucdCUvSO4FoMrcxgTa5F7i33YbUg.Ls8hExGrAoSwTmn0oXHBU71Ar0bHoYOAHQyR2kXdCmwg.PNG.wonch888/image.png?type=w800',
  },
  {
    id: 3,
    link: 'https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDVfMjgg/MDAxNTg4NjgyNTkxODYz.bujlnUzbi9J6B_IuTG70QMMkVU_nFh9gBjCO_aSG8ukg.NbHujuRj84h1nq6AiSwEsvNgnYXA4CVdWoS-zheeBuAg.PNG.wonch888/image.png?type=w800',
  },
  {
    id: 4,
    link: 'https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDRfMjQ4/MDAxNTg4NTY5ODM2MDEx.WyAMhYtqOIQRJ0K0ucdCUvSO4FoMrcxgTa5F7i33YbUg.Ls8hExGrAoSwTmn0oXHBU71Ar0bHoYOAHQyR2kXdCmwg.PNG.wonch888/image.png?type=w800',
  },
  {
    id: 5,
    link: 'http://file3.instiz.net/data/file3/2018/06/05/a/1/e/a1e8fe23fe4dc2b841cd37a0fb9e7175.jpg',
  },
];

export const handlers = [
  // 테스트 mock api
  rest.get('api/v1/test', (req, res, ctx) => {
    return res(ctx.status(200), ctx.json(dummy));
  }),
  rest.post('api/v1/styles', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({
        link: 'https://simsontest.s3.ap-northeast-2.amazonaws.com/83b17690-8e22-471b-ad3c-c8ffba67066d.jpg',
      }),
    );
  }),

  // ai task id 반환 api
  rest.post('api/v1/images', (req, res, ctx) => {
    return res(ctx.status(200), ctx.json(dummyTaskId));
  }),
  rest.get(`api/v1/images?`, (req, res, ctx) => {
    console.log('images');
    let pageNumber = req.url.searchParams.get('page');
    if (pageNumber === '0') {
      console.log('mock 0');
      return res(ctx.status(200), ctx.json(recentImgs));
    } else if (pageNumber === '1') {
      console.log('mock 1');
      return res(ctx.status(200), ctx.json(recentImgs1));
    } else {
      return res(ctx.status(200), ctx.json(recentImgs));
    }
  }),

  //AI task 완료되었는지 반환
  rest.get('api/v1/images/task/1', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({
        status: 'done',
        result: {
          top: 't-shirts',
          bottom: 'slacks',
        },
      }),
    );
  }),
];
