import random
import time

from src.logger import log_error


def predict_age(name, retry=2):

    for attempt in range(retry):

        try:

            # 模拟 timeout
            if random.random() < 0.3:
                raise TimeoutError("API timeout")

            age = random.randint(18, 60)

            return {
                "name": name,
                "age": age,
                "count": 1,
                "source": "mock_api"
            }

        except TimeoutError as e:

            print(f"[WARN] retry {attempt+1}/{retry}")

            log_error(str(e))

            time.sleep(1)

    return {
        "name": name,
        "age": 0,
        "count": 0,
        "error": "API failed"
    }