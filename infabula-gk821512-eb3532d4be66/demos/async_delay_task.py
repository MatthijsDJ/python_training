import os
import asyncio

os.environ['PYTHONASYNCIODEBUG'] = '1'


async def do_task_with_delay(name, delay):
    print(f"Starting task '{name}' ({delay})")
    await asyncio.sleep(delay)
    print(f"Ended task '{name}' ({delay})")
    return name


async def main():
    loop = asyncio.get_event_loop()
    loop.set_debug('enabled')

    t1 = asyncio.create_task(do_task_with_delay("One", 5))
    t2 = asyncio.create_task(do_task_with_delay("Two", 3))
    t3 = asyncio.create_task(do_task_with_delay("Three", 7))

    await t1
    await t2
    await t3


asyncio.run(main())