import random

from .meters.main import meter_type
from .meters.residential import residential
from .meters.industry import industry
from .meters.feed_in import feed_in
from .meters.residential_feed_in import residential_feed_in
from .constants import METER_OCCURENCES

def main(seed):
    random.seed(seed)
    meter = random.choices(list(meter_type), METER_OCCURENCES, k=1)[0](seed)
    meter.run()
    print(meter.string())