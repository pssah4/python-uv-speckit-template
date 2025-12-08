import datetime
import os
import sys
import asyncio
import warnings


def main() -> None:
    warnings.filterwarnings("ignore")
    now = datetime.datetime.now().isoformat(timespec="seconds")
    print(f"[{now}] Hello from the uv base container!")
    print(f"Python executable: {sys.executable}")
    print(f"Current working dir: {os.getcwd()}")


if __name__ == "__main__":
    asyncio.run(async_main()) if "async_main" in globals() else main()
