import asyncio
import json
import logging
import random
import sys
from dataclasses import asdict

from dacite import from_dict

from together_web3.computer import FinetuneRequest
from together_web3.together import ResolveOptions, TogetherWeb3

logger = logging.getLogger(__name__)


async def main():
    try:
        together_web3 = TogetherWeb3()
        result = await together_web3.resolve_inference(
            from_dict(
                data_class=FinetuneRequest,
                data={
                    "model": "FT_OPT-1.3B",
                    "dataset_url": "https://github.com/brennanem/CS324FinalProject/blob/main/combined_data.jsonl",
                    "arguments": {
                        "total_steps": 200,
                    }
                }
            ),
            ResolveOptions(
                match_callback=lambda x: logger.info("MatchEvent: %s", x)
            )
        )
        print(result)
    except Exception as e:
        logger.error("Exception: %s", e)
    finally:
        await together_web3.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())