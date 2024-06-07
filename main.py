import subprocess
import asyncio


async def clear_logs():
    with open('head/values/logs.txt', 'w', encoding='utf-8') as file:
        file.truncate(0)

async def main():
    await clear_logs()

    la_start_process = subprocess.Popen(['python', 'head/la_start.py'])

    try:
        la_start_process.wait()

    except KeyboardInterrupt:
        la_start_process.terminate()

asyncio.run(main())
