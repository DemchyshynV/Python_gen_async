# import requests
# import time
#
#
# def time_decor(func):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         print('Time: ', round(time.time() - start, 2))
#
#     return wrap
#
#
# def get_res(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
#
# def write_file(res: requests.Response):
#     file_name = res.url.split('/')[-1]
#     with open(file_name, 'wb') as file:
#         file.write(res.content)
#
#
# @time_decor
# def main():
#     url = 'https://loremflickr.com/320/240/dog'
#     for i in range(20):
#         write_file(get_res(url))
#
#
# if __name__ == '__main__':
#     main()

##################################################################################
import asyncio
import httpx
import time


def time_decor(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('Time: ', round(time.time() - start, 2))

    return wrap


def write_file(data):
    file_name = f'file-{round(time.time() * 1000)}.jpg'
    with open(file_name, 'wb') as file:
        file.write(data)


async def get_res(url, client):
    res = await client.get(url)
    write_file(res.read())


async def start():
    url = 'https://loremflickr.com/320/240/dog'
    tasks = []
    async with httpx.AsyncClient() as client:
        for i in range(20):
            task = asyncio.create_task(get_res(url, client))
            tasks.append(task)
        await asyncio.gather(*tasks)


@time_decor
def main():
    asyncio.run(start())


if __name__ == '__main__':
    main()
