from TikTokApi import TikTokApi
import asyncio
import os
import io
import time
from url_generator import generate_url

ms_token = "CA4zCBVwRt4t-FCJq8v_1VOtpuDZEcrrMggaBXr32cngzvpFtFOdnQgS4epODkLpiutgLTEZLyAkh-H-upxU8XovXopDnXeY6g6df-2P6p2R9YgQLiZuORf9hSWw32c9kyfTyWq4Ov4-Yw==" # set your own ms_token, think it might need to have visited a profile

async def get_video_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        url_param = "https://www.tiktok.com/@_antunesxl/video/7352712808133446918"
        c = 1
        for i in range(10):
            video = api.video(url=url_param)
            async for related_video in video.related_videos(count=10):
                with open(f"./../videos/coleta{c}.txt", "w", encoding="utf-8") as file:
                    file.write(str(related_video.as_dict))
                    
                with open(f"./../videos/coleta{c}.txt", "r", encoding="utf-8") as file:
                    content = file.read()
                    url_param = generate_url(content)
                    with open("urls.txt", "a", encoding="utf-8") as url_file:
                        url_file.write(url_param + "\n")
                c = c + 1

            time.sleep(20)

if __name__ == "__main__":
    asyncio.run(get_video_example())
